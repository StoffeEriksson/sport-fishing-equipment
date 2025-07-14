from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

import stripe

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('view_cart')

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.original_cart = str(cart)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()

            for key, item in cart.items():
                try:
                    product = Product.objects.get(id=item['product_id'])
                    quantity = item['quantity']
                    size = item.get('size')  # Can be None
                    order_line = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                        product_size=size,
                    )
                    order_line.save()
                except Product.DoesNotExist:
                    messages.error(request, "A product in your cart was not found.")
                    order.delete()
                    return redirect('view_cart')

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, "There was an error with your form. Please check again.")

    else:
        # Prepare Stripe payment intent
        total = 0
        for item in cart.values():
            try:
                product = Product.objects.get(id=item['product_id'])
                total += product.price * item['quantity']
            except Product.DoesNotExist:
                continue

        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            delivery = 0
        grand_total = round((total + delivery), 2)
        stripe_total = int(grand_total * 100)

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        product_count = sum(item['quantity'] for item in cart.values())

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'cart_items': _get_cart_items_from_session(request),
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
        'product_count': product_count,
    }
    
    return render(request, template, context)


def _get_cart_items_from_session(request):
    """
    Helper function to rebuild cart_items list from session-based cart
    (used in checkout view).
    """
    cart = request.session.get('cart', {})
    items = []

    for key, item in cart.items():
        try:
            product = Product.objects.get(id=item['product_id'])
            items.append({
                'product': product,
                'quantity': item['quantity'],
                'size': item.get('size'),
                'subtotal': product.price * item['quantity'],
            })
        except Product.DoesNotExist:
            continue

    return items


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully placed! \
        Your order number is {order_number}. Confirmation sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    return render(request, 'checkout/checkout_success.html', {'order': order})
