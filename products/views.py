from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product


def all_products(request, category_slug=None, subcategory_slug=None):
    category = None
    subcategory = None
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()
    if category_slug != None:
        if subcategory_slug != None:
            category = Category.objects.get(slug=category_slug)
            subcategory = SubCategory.objects.get(slug=subcategory_slug)
            products_list = Product.objects.filter(sub_category=subcategory.name)
        else:
            category = Category.objects.get(slug=category_slug)
            products_list = Product.objects.filter(category=category.name)
    else:
        products_list = Product.objects.filter(available=True)

    context = {
        "products": products_list,
        "subcategory": subcategory,
        "category": category,
        "all_categories": all_categories,
        "all_subcategories": all_subcategories,
    }
    return render(request, "products/products.html", context)


def product_details(request, category_slug, subcategory_slug, product_slug):
    category = Category.objects.get(slug=category_slug)
    subcategory = SubCategory.objects.get(slug=subcategory_slug)
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()
    product = Product.objects.get(
        category__slug=category_slug,
        sub_category__slug=subcategory_slug,
        slug=product_slug,
    )
    context = {
        "product": product,
        "subcategory": subcategory,
        "category": category,
        "all_categories": all_categories,
        "all_subcategories": all_subcategories,
    }
    return render(request, "products/product_details.html", context)
