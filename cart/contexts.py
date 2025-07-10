from django.conf import settings
from .models import CartItem
from products.models import Product


def cart_totals(request):
    total = 0
    delivery = 0
    free_delivery_delta = 0
    grand_total = 0
    cart_items_count = 0

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            total += item.subtotal()
            cart_items_count += item.quantity
    else:
        cart = request.session.get('cart', {})
        for key, item in cart.items():
            product = Product.objects.get(pk=item['product_id'])
            total += product.price * item['quantity']
            cart_items_count += item['quantity']

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'cart_items_count': cart_items_count,
    }
