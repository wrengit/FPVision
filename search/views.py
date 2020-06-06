from django.shortcuts import render
from products.models import Category, SubCategory, Product
from django.db.models import Q


def search_result(request):
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()
    products = None
    query = None
    if "q" in request.GET:
        query = request.GET.get("q")
        products = Product.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query)
        )
    context = {
        "query": query,
        "products": products,
        "all_categories": all_categories,
        "all_subcategories": all_subcategories,
    }
    return render(request, "search/search.html", context)

