from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Category, SubCategory, Product
from .forms import ProductForm


def all_products(request, category_slug=None, subcategory_slug=None):
    category = None
    subcategory = None
    if category_slug is not None:
        if subcategory_slug is not None:
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
    }
    return render(request, "products/products.html", context)


def product_details(request, category_slug, subcategory_slug, product_slug):
    category = Category.objects.get(slug=category_slug)
    subcategory = SubCategory.objects.get(slug=subcategory_slug)
    product = Product.objects.get(
        category__slug=category_slug,
        sub_category__slug=subcategory_slug,
        slug=product_slug,
    )
    context = {
        "product": product,
        "subcategory": subcategory,
        "category": category,
    }
    return render(request, "products/product_details.html", context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added product")
            return redirect(reverse("add_products"))
        else:
            messages.error(
                request, "Failed to add product. Please ensure form in valid"
            )
    else:
        form = ProductForm()
    
    template = "products/add_product.html"
    context = {"form": form}

    return render(request, template, context)
