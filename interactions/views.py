from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Like, Rating, Comment
from .forms import RatingForm, CommentForm

@login_required
def submit_rating_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    rating_instance = Rating.objects.filter(user=request.user, product=product).first()
    comment_instance = None  # Comments are always new entries

    if request.method == 'POST':
        rating_form = RatingForm(request.POST, instance=rating_instance)
        comment_form = CommentForm(request.POST)

        if rating_form.is_valid() and comment_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.product = product
            rating.save()

            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()

            return redirect('product_detail', product.id)
    else:
        rating_form = RatingForm(instance=rating_instance)
        comment_form = CommentForm()

    return render(request, 'interactions/rate_comment.html', {
        'product': product,
        'rating_form': rating_form,
        'comment_form': comment_form,
    })


@login_required
def like_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    like, created = Like.objects.get_or_create(user=request.user, product=product)

    if not created:
        like.delete()  # Toggle like off
    return redirect('product_detail', product.id)
