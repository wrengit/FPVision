from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def my_account(request):
    return render(request, "profiles/my_account.html")


def order_history(request, order_number=None):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by("-date")
    if order_number is not None:
        order = get_object_or_404(Order, order_number=order_number)
        date = order.date
        formatted_date = date.strftime(" %d-%m-%Y ")
        formatted_time = date.strftime(" %H:%M ")

        messages.info(
            request,
            f"This is a past confirmation for order \
            number {order_number} placed on \
            {formatted_date} at {formatted_time}",
        )

        template = "checkout/checkout_success.html"
        context = {"order": order}
        return render(request, template, context)

    else:
        template = "profiles/order_history.html"
        context = {"orders": orders}
        return render(request, template, context)


def update_address(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "We have updated your address")
    template = "profiles/update_address.html"
    context = {"form": form}
    return render(request, template, context)
