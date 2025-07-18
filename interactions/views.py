from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Like, Rating, Comment
from .forms import RatingForm, CommentForm


@login_required
def submit_rating(request, product_id):
    """Save or update only rating."""
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST' and 'score' in request.POST:
        score = int(request.POST.get('score'))
        if 1 <= score <= 5:
            rating, created = Rating.objects.get_or_create(
                user=request.user,
                product=product,
                defaults={'score': score}
            )
            if not created:
                rating.score = score
                rating.save()

    return redirect('product_detail', pk=product.id)


@login_required
def submit_comment(request, product_id):
    """Save a commen (without effecting rating)."""
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()

    return redirect('product_detail', pk=product.id)


@login_required
def like_product(request, product_id):
    """Like a product"""
    product = get_object_or_404(Product, id=product_id)
    like, created = Like.objects.get_or_create(user=request.user, product=product)

    if not created:
        like.delete()  # Toggle like off
    return redirect('product_detail', product.id)
