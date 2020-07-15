from django.shortcuts import render
from django.conf import settings
from products.models import Product


def index(request):
    """
    Main landing page
    """
    return render(
        request,
        "index/index.html",
        context={"free_delivery": settings.FREE_DELIVERY_THRESHOLD,}
    )
