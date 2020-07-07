from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages


def contact(request):
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
