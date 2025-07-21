from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile_view(request):
    """
    Show and update the logged-in user's profile.
    """
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profiles/profile.html', {
        'form': form,
    })


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'profiles/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_number):
    """
    Display a single past order in detail.
    Only accessible to the user who owns the order.
    """
    order = get_object_or_404(Order,
                              order_number=order_number,
                              user=request.user
                              )
    return render(request, 'profiles/order_detail.html', {'order': order})
