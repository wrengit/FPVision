from .forms import SubscriptionForm


def sub_form_context(request):
    sub_form = SubscriptionForm()
    context = {"sub_form": sub_form}
    return context
