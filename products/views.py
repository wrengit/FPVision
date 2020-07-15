from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Category, SubCategory, Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


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


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added product")
            return redirect(reverse("add_products"))
        else:
            messages.error(
                request, "Failed to add product. Please ensure form is valid"
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {"form": form}

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated product")
            return redirect(
                reverse(
                    "product_details",
                    args=[
                        product.category.slug,
                        product.sub_category.slug,
                        product.slug,
                    ],
                )
            )
        else:
            messages.error(
                request, "Failed to update product. Please ensure form is valid"
            )
    else:
        form = ProductForm(instance=product)

    template = "products/edit_product.html"
    context = {"form": form}

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, f"{product.name} was deleted")
    return redirect(reverse("all_products"))
