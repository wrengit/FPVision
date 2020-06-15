from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_basket(request):
    return render(request, "basket/basket.html")


def add_to_basket(request, product_id):
    """Add products to the basket"""

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    basket = request.session.get("basket", {})

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
        messages.success(
            request, f"Updated {product.name} quantity to {basket[product_id]}"
        )
    else:
        basket[product_id] = quantity
        messages.success(request, f"Added {product.name} to your basket")

    request.session["basket"] = basket
    return redirect(redirect_url)


def adjust_basket(request, product_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get("quantity"))
    basket = request.session.get("basket", {})

    if quantity > 0:
        basket[product_id] = quantity
        messages.success(
            request, f"Updated {product.name} quantity to {basket[product_id]}"
        )
    else:
        basket.pop(product_id)
        messages.success(request, f"Removed {product.name} from your basket")

    request.session["basket"] = basket
    return redirect(reverse("view_basket"))


def remove_from_basket(request, product_id):
    """Remove the product from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        basket = request.session.get("basket", {})

        basket.pop(product_id)
        messages.success(request, f"Removed {product.name} from your basket")

        request.session["basket"] = basket
        return redirect(reverse("view_basket"))

    except Exception as e:
        messages.error(request, f"Error removing product: {e}")
        return HttpResponse(status=500)
