from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem


def view_cart(request):
    """
    Display all products in the shopping cart, including total cost.
    """
    cart_items = []
    total = 0

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.subtotal() for item in cart_items)
    else:
        cart = request.session.get('cart', {})
        for key, item in cart.items():  # key is like "41_S"
            product = get_object_or_404(Product, pk=item['product_id'])
            quantity = item['quantity']
            size = item.get('size')
            subtotal = product.price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'size': size,
                'subtotal': subtotal,
                'key': key,  # if needed for update/remove
            })

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'sizes': ['XS', 'S', 'M', 'L', 'XL'],
    })



def add_to_cart(request, product_id):
    """
    Add a product to the shopping cart.
    If logged in, store in DB. If guest, store in session.
    """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('size', None)

    if request.user.is_authenticated:
        # Logged-in user: Save to DB
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            size=size
        )
        cart_item.quantity += quantity
        cart_item.save()
    else:
        # Guest: store in session-based cart (dict-based, by product_id+size)
        cart = request.session.get('cart', {})

        # Unique key for each product and size combination
        key = f"{product.id}_{size}" if size else str(product.id)

        if key in cart:
            cart[key]['quantity'] += quantity
        else:
            cart[key] = {
                'product_id': product.id,
                'quantity': quantity,
                'size': size,
            }

        request.session['cart'] = cart

    return redirect('view_cart')


def update_cart(request, product_id):
    """
    Update quantity and size for a product in the cart.
    """
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('size', None)

    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(user=request.user, product_id=product_id, size=size).first()
        if cart_item:
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
    else:
        cart = request.session.get('cart', {})
        # Use same key structure as in add_to_cart
        key = f"{product_id}_{size}" if size else str(product_id)

        if key in cart:
            if quantity > 0:
                cart[key]['quantity'] = quantity
            else:
                del cart[key]
        request.session['cart'] = cart

    return redirect('view_cart')


def remove_from_cart(request, product_id):
    """
    Remove a single product (with optional size) from the cart.
    Works for both authenticated users (DB) and guests (session).
    """
    size = request.POST.get('size', None)

    if request.user.is_authenticated:
        # Remove matching CartItem from database
        CartItem.objects.filter(user=request.user, product_id=product_id, size=size).delete()
    else:
        # Remove item from session-based cart
        cart = request.session.get('cart', {})

        # Check both keys: with and without size
        key_with_size = f"{product_id}_{size}" if size else None
        key_plain = str(product_id)

        if key_with_size and key_with_size in cart:
            del cart[key_with_size]
        elif key_plain in cart:
            del cart[key_plain]

        request.session['cart'] = cart

    return redirect('view_cart')



def clear_cart(request):
    """
    Completely empty the cart by clearing the session data.
    """
    request.session['cart'] = {}
    return redirect('view_cart')
