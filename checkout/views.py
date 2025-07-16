from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

import stripe
import json

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.models import CartItem

# Set Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY


@require_POST
def cache_checkout_data(request):
    """
    Caches cart and user data in Stripe PaymentIntent metadata.
    Helps match payment to order in webhook handling.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Payment could not be processed at this time. Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Checkout view:
    - Loads cart from DB or session
    - Calculates totals and delivery cost (USD)
    - Handles order submission and Stripe payment
    """
    # Build cart from DB (authenticated) or session (guest)
    if request.user.is_authenticated:
        db_items = CartItem.objects.filter(user=request.user)
        if not db_items.exists():
            messages.error(request, "Your cart is empty.")
            return redirect('view_cart')
        cart = {
            f"{item.product.id}_{item.size}" if item.size else str(item.product.id): {
                'product_id': item.product.id,
                'quantity': item.quantity,
                'size': item.size,
            } for item in db_items
        }
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect('view_cart')

    cart_items = []
    total = Decimal('0.00')

    for item_data in cart.values():
        product = get_object_or_404(Product, pk=item_data['product_id'])
        quantity = item_data['quantity']
        size = item_data.get('size')
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'size': size,
        })

    # Delivery cost: 10% fee if total under $50
    delivery = Decimal('0.00')
    if total < Decimal('50.00'):
        delivery = total * Decimal('0.10')

    grand_total = total + delivery

    # Handle POST (form submission)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.original_cart = json.dumps(cart)
            order.user = request.user if request.user.is_authenticated else None
            order.order_total = total
            order.delivery_cost = delivery
            order.grand_total = grand_total
            order.save()

            # Save line items
            for item in cart_items:
                OrderLineItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    product_size=item['size'],
                )

            # Clear cart
            if request.user.is_authenticated:
                CartItem.objects.filter(user=request.user).delete()
            else:
                request.session['cart'] = {}

            return redirect('checkout_success', order_number=order.order_number)
        else:
            messages.error(request, "There was an error with your form. Please check your details.")
    else:
        form = OrderForm()

    # Create Stripe PaymentIntent (Stripe expects cents)
    intent = stripe.PaymentIntent.create(
        amount=int(grand_total * 100),
        currency='usd',
    )

    context = {
        'order_form': form,
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
        'client_secret': intent.client_secret,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'product_count': len(cart_items),
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts.
    Clears cart and shows success message and summary.
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully placed! '
                     f'Your order number is {order_number}. Confirmation sent to {order.email}.')

    if request.user.is_authenticated:
        CartItem.objects.filter(user=request.user).delete()
    else:
        if 'cart' in request.session:
            del request.session['cart']

    return render(request, 'checkout/checkout_success.html', {'order': order})
