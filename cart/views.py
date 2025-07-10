from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_cart(request):
    """
    Display all products in the shopping cart, including total cost.
    """
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        subtotal = product.price * quantity
        total += subtotal
        products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'cart/cart.html', {
        'cart_items': products,
        'total': total
    })

