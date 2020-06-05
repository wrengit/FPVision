from django.shortcuts import render
from products.models import *


def index(request):
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()
    context = {
        "all_categories": all_categories,
        "all_subcategories": all_subcategories,
    }
    return render(request, "index/index.html", context)
