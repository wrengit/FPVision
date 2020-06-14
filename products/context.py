from .models import SubCategory, Category


def all_products_all_categories(request):
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()

    context = {"all_subcategories": all_subcategories, "all_categories": all_categories}

    return context
