from django.contrib import admin
from .models import Category, SubCategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    ordering = ["name",]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    ordering = ["category",]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(SubCategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "sub_category",
        "sku",
        "price",
        "stock",
        "full_slug",
        "available",
    ]
    list_editable = ["price", "stock", "available", ]
    prepopulated_fields = {"slug": ("name",), }
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
