from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from products.models import Product
from .models import Like, Rating, Comment
from .forms import RatingForm, CommentForm
from django.db.models import Avg



@login_required
def submit_rating(request, product_id):
    """Save or update only rating, then update product's average rating."""
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

            # Uppdatera produktens genomsnittsbetyg
            avg = Rating.objects.filter(product=product).aggregate(Avg('score'))['score__avg']
            product.rating = round(avg or 0, 1)
            product.save()

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


@login_required
def liked_products(request):
    liked = Like.objects.filter(user=request.user).select_related('product')
    liked_products = [like.product for like in liked]
    return render(request, 'interactions/liked_products.html', {
        'liked_products': liked_products
    })


@login_required
def remove_like(request, product_id):
    like = get_object_or_404(Like, user=request.user, product_id=product_id)
    like.delete()
    return redirect('liked_products')


@login_required
def user_comments(request):
    comments = Comment.objects.filter(user=request.user).select_related('product')
    return render(request, 'interactions/comments.html', {'comments': comments})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('user_comments')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'interactions/edit_comment.html', {
        'form': form,
        'comment': comment
    })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == "POST":
        comment.delete()
        return redirect('user_comments')
    return HttpResponseForbidden()
