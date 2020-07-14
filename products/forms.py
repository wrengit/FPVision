from django import forms
from products.models import Product, Category, SubCategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "category",
            "sub_category",
            "name",
            "description",
            "stock",
            "price",
            "available",
            "image_url",
            "image",
        }
