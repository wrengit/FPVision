from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Category, SubCategory, Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def all_products(request, category_slug=None, subcategory_slug=None):
    """
    Displays all products, or products filtered by either
    category or subcategory
    """
    category = None
    subcategory = None
    sort = None
    direction = None

    if category_slug is not None:
        if subcategory_slug is not None:
            category = Category.objects.get(slug=category_slug)
            subcategory = SubCategory.objects.get(slug=subcategory_slug)
            if "sort" in request.GET:
                sortkey = request.GET["sort"]
                sort = sortkey
                if "direction" in request.GET:
                    direction = request.GET["direction"]
                    if direction == "desc":
                        sortkey = f"-{sortkey}"
                products_list = Product.objects.filter(
                    available=True, sub_category=subcategory.name
                ).order_by(sortkey)
            else:
                products_list = Product.objects.filter(
                    available=True, sub_category=subcategory.name
                )
        else:
            category = Category.objects.get(slug=category_slug)
            if "sort" in request.GET:
                sortkey = request.GET["sort"]
                sort = sortkey
                if "direction" in request.GET:
                    direction = request.GET["direction"]
                    if direction == "desc":
                        sortkey = f"-{sortkey}"
                products_list = Product.objects.filter(
                    available=True, category=category.name
                ).order_by(sortkey)
            else:
                products_list = Product.objects.filter(
                    available=True, category=category.name
                )
    else:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products_list = Product.objects.filter(available=True).order_by(sortkey)
        else:
            products_list = Product.objects.filter(available=True)

    context = {
        "products": products_list,
        "subcategory": subcategory,
        "category": category,
    }
    return render(request, "products/products.html", context)


def product_details(request, category_slug, subcategory_slug, product_slug):
    """
    Displays the product detail page
    """
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
    """
    Allows users with admin perms to add a product
    """
    if request.user.has_perm("products.add_product"):
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
    else:
        return redirect(reverse("index"))


@login_required
def edit_product(request, product_id):
    """
    Allows users with admin perms to edit an
    exisiting product
    """
    if request.user.has_perm("products.change_product"):
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
    else:
        return redirect(reverse("index"))


@login_required
def delete_product(request, product_id):
    """
    Allows users with admin perms to delete and
    existing product
    """
    if request.user.has_perm("products.delete_product"):
        product = Product.objects.get(id=product_id)
        product.delete()
        messages.success(request, f"{product.name} was deleted")
        return redirect(reverse("all_products"))
    else:
        return redirect(reverse("index"))
