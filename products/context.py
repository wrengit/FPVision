from .models import SubCategory, Category, Product


def all_products_all_categories(request):
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()
    featured_products = Product.objects.all().filter(available=True, featured=True)

    context = {
        "all_subcategories": all_subcategories,
        "all_categories": all_categories,
        "featured_products": featured_products,
    }

    return context
