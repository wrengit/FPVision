from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .forms import ContactForm, SubscriptionForm
from .models import SubscriptionList
from django.contrib import messages


def contact(request):
    """
    Contact form to leave a message for shop admin
    Does not require a logged in user. Can be accessed
    from the admin dashboard.
    """
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ContactForm(request.POST, instance=request.user)
        else:
            form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "We have recieved your message. "
                + "You can expect to hear from us soon",
            )
        return redirect(reverse("all_products"))
    else:
        if request.user.is_authenticated:
            form = ContactForm(instance=request.user)
        else:
            form = ContactForm()

        return render(request, "contact/contact.html", {"form": form})


def subscribe(request):
    """
    Adds an email address to a list. Model data is currently
    saved, but no subscriber list is set up
    """
    sub_form = SubscriptionForm()
    if request.method == "POST":
        next = request.POST.get("next", "/")
        sub_form = SubscriptionForm(request.POST)
        if SubscriptionList.objects.filter(email=request.POST.get("email")).exists():
            messages.info(request, "You are aleady subscribed to the mailing list")
            return HttpResponseRedirect(next)
        else:
            if sub_form.is_valid():
                sub_form.save()
                messages.success(request, "You've joined our mailing list!")
    return HttpResponseRedirect(next)
