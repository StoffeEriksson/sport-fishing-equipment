from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category
from interactions.forms import RatingForm, CommentForm
from interactions.models import Like, Rating, Comment


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

    rating_form = RatingForm()
    comment_form = CommentForm()
    user_like = None
    user_rating = None
    comments = Comment.objects.filter(product=product).order_by('-created_at')

    if request.user.is_authenticated:
        user_like = Like.objects.filter(user=request.user, product=product).first()
        user_rating = Rating.objects.filter(user=request.user, product=product).first()

    context = {
        'product': product,
        'related_products': related_products,
        'rating_form': rating_form,
        'comment_form': comment_form,
        'user_like': user_like,
        'user_rating': user_rating,
        'comments': comments,
    }
    return render(request, 'products/product_detail.html', context)


def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'products/products.html', {
        'products': products,
        'search_term': query,
    })