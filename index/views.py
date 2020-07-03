from django.shortcuts import render
from django.conf import settings


def index(request):

    return render(
        request,
        "index/index.html",
        context={"free_delivery": settings.FREE_DELIVERY_THRESHOLD},
    )
