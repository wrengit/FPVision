from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib import messages
from products.models import Category, SubCategory, Product
from django.db.models import Q
from django.core import serializers


def search_result(request):
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()
    products = None
    query = None
    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            messages.error(request, "Please enter a search criteria")
            return redirect(reverse("all_products"))
        products = Product.objects.all().filter(
            Q(name__contains=query)
            | Q(description__contains=query)
            | Q(category__name__contains=query)
            | Q(sub_category__name__contains=query)
        )
    context = {
        "query": query,
        "products": products,
        "all_categories": all_categories,
        "all_subcategories": all_subcategories,
    }
    return render(request, "search/search.html", context)


def js_search(request):
    products = None
    filter_products = None
    query = None
    if "q" in request.GET:
        query = request.GET["q"]
        products = Product.objects.all().filter(
            Q(name__contains=query)
            | Q(description__contains=query)
            | Q(category__name__contains=query)
            | Q(sub_category__name__contains=query)
        )
        filter_products = products.values(
            "name",
            "price",
            "category",
            "sub_category",
            "image",
            "image_url",
            "id",
            "slug",
        ).filter(available=True)

    return JsonResponse(list(filter_products), safe=False)