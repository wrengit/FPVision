from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {"form": form, "orders": orders}

    return render(request, "profiles/profile.html", context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

