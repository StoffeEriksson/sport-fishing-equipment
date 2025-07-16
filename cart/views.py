from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import CartItem
from decimal import Decimal
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def view_cart(request):
    """
    Display all products in the shopping cart, including total cost.
    """
    cart_items = []
    total = Decimal('0.00')

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.subtotal() for item in cart_items)
    else:
        cart = request.session.get('cart', {})
        for key, item in cart.items():
            product = get_object_or_404(Product, pk=item['product_id'])
            quantity = item['quantity']
            size = item.get('size') or None
            subtotal = product.price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'size': size,
                'subtotal': subtotal,
                'key': key,
            })

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'sizes': ['XS', 'S', 'M', 'L', 'XL'],
    })


@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('size') or None

    if request.user.is_authenticated:
        cart_item, _ = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            size=size
        )
        cart_item.quantity = quantity
        cart_item.save()

        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart = request.session.get('cart', {})
        key = f"{product_id}_{size}" if size else str(product_id)
        cart[key] = {
            'product_id': product.id,
            'quantity': quantity,
            'size': size,
        }
        request.session['cart'] = cart

        cart_items = []
        for item in cart.values():
            p = get_object_or_404(Product, pk=item['product_id'])
            cart_items.append({
                'product': p,
                'quantity': item['quantity'],
                'size': item.get('size')
            })

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        items = []
        total = Decimal('0.00')

        for item in cart_items:
            if request.user.is_authenticated:
                p = item.product
                q = item.quantity
                s = item.size
            else:
                p = item['product']
                q = item['quantity']
                s = item['size']

            subtotal = p.price * q
            total += subtotal

            items.append({
                'name': p.name,
                'image_url': p.image.url if p.image else '',
                'quantity': q,
                'size': s,
                'price': f"{p.price:.2f}"
            })

        return JsonResponse({
            'items': items,
            'total': f"{total:.2f}"
        })

    messages.success(request, f"{product.name} added to your cart.")
    return redirect('view_cart')


def update_cart(request, product_id):
    """
    Update the quantity and size of a product in the cart.
    Works for both authenticated users and guests.
    """
    quantity = int(request.POST.get('quantity', 1))
    new_size = request.POST.get('size') or None
    original_size = request.POST.get('original_size') or None

    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(
            user=request.user,
            product_id=product_id,
            size=original_size
        ).first()

        if cart_item:
            if new_size != original_size:
                existing = CartItem.objects.filter(
                    user=request.user,
                    product_id=product_id,
                    size=new_size
                ).first()

                if existing:
                    existing.quantity += quantity
                    existing.save()
                    cart_item.delete()
                else:
                    cart_item.size = new_size
                    cart_item.quantity = quantity
                    cart_item.save()
            else:
                if quantity > 0:
                    cart_item.quantity = quantity
                    cart_item.save()
                else:
                    cart_item.delete()
    else:
        cart = request.session.get('cart', {})
        old_key = f"{product_id}_{original_size}" if original_size else str(product_id)
        new_key = f"{product_id}_{new_size}" if new_size else str(product_id)

        if old_key in cart:
            item = cart[old_key]
            if quantity > 0:
                if new_key != old_key:
                    if new_key in cart:
                        cart[new_key]['quantity'] += quantity
                    else:
                        cart[new_key] = {
                            'product_id': product_id,
                            'quantity': quantity,
                            'size': new_size,
                        }
                    del cart[old_key]
                else:
                    cart[old_key]['quantity'] = quantity
                    cart[old_key]['size'] = new_size
            else:
                del cart[old_key]

        request.session['cart'] = cart

    return redirect('view_cart')


def remove_from_cart(request, product_id):
    """
    Remove a single product (with optional size) from the cart.
    Works for both authenticated users and guests.
    """
    size = request.POST.get('size')

    # Normalize to Python None if the value is empty string or the string 'None'
    if not size or size == 'None':
        size = None

    print(f"Attempting to remove product_id={product_id}, size={size!r}")

    if request.user.is_authenticated:
        if size is None:
            deleted, _ = CartItem.objects.filter(
                user=request.user,
                product_id=product_id,
                size__isnull=True
            ).delete()
        else:
            deleted, _ = CartItem.objects.filter(
                user=request.user,
                product_id=product_id,
                size=size
            ).delete()

        print(f"Authenticated user: Deleted {deleted} item(s)")
    else:
        cart = request.session.get('cart', {})
        key = f"{product_id}_{size}" if size else str(product_id)
        if key in cart:
            del cart[key]
        request.session['cart'] = cart

    return redirect('view_cart')


def clear_cart(request):
    """
    Completely empty the cart.
    """
    if request.user.is_authenticated:
        CartItem.objects.filter(user=request.user).delete()
    else:
        request.session['cart'] = {}
    return redirect('view_cart')