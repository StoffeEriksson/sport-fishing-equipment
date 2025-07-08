from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    deals = Product.objects.filter(category__name='deals')
    return render(request, 'products/home.html', {'deals': deals})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def category_view(request, category_name):
    if category_name == "all":
        products = Product.objects.all()
        category = None
    else:
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)

    return render(request, 'products/products.html', {
        'products': products,
        'selected_category': category,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products
    })


def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'products/products.html', {
        'products': products,
        'search_term': query,
    })