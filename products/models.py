from django.db import models
from .utils import create_sku
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="category",
        null=True,
        blank=True,
        default="/static/media/default/default_category.jpg",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])


class SubCategory(models.Model):
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("products_by_subcategory", args=[self.category.slug, self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.CASCADE
    )
    sub_category = models.ForeignKey(
        "SubCategory", null=True, blank=True, on_delete=models.CASCADE
    )
    sku = models.CharField(max_length=10, unique=True, blank=True, default=create_sku())
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField(blank=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to="product",
        null=True,
        blank=True,
        default="/static/media/defaults/default_product.jpg",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse(
            "product_details",
            args=[self.category.slug, self.sub_category.slug, self.slug],
        )
