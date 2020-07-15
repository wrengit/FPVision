from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from checkout.models import Order
from contact.models import ContactList
from django.contrib.auth.decorators import login_required


@login_required
def my_account(request):
    """
    'my account' dashboard view
    """
    return render(request, "profiles/my_account.html")


@login_required
def order_history(request, order_number=None):
    """
    Details a list of previous user orders if no
    order number is given, or the order details
    if an order number is given
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by("-date")
    all_orders = Order.objects.all().order_by("-date")
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
        context = {"order": order, "from_profile": True}
        return render(request, template, context)

    else:
        template = "profiles/order_history.html"
        context = {"orders": orders, "all_orders": all_orders}
        return render(request, template, context)


@login_required
def update_address(request):
    """
    Allows users to update their address. Checkout
    information will be pulled from this UserProfile
    """
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


@login_required
def update_account_details(request):
    """
    Allows users to change username, and password
    """
    form = UserForm(instance=request.user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "We have updated your account details")
    template = "profiles/update_account_details.html"
    context = {"form": form}
    return render(request, template, context)


@login_required
def customer_messages(request):
    """
    Admin view that lists all customer orders
    """
    customer_messages = ContactList.objects.all()
    return render(
        request,
        "profiles/messages_list.html",
        context={"customer_messages": customer_messages},
    )

