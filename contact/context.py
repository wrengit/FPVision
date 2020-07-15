from .forms import SubscriptionForm

"""
Context processor for the subscription form
which is presented on every page
"""
def sub_form_context(request):
    sub_form = SubscriptionForm()
    context = {"sub_form": sub_form}
    return context
