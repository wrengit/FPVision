from django.db import models
from django.utils.text import slugify
from .utils import create_sku
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="category",
        null=True,
        blank=True,
        default="defaults/default_category.jpg",
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
        "Category",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="category",
        null=True,
        blank=True,
        default=settings.MEDIA_URL + "defaults/default_subcategory.jpg",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        name = self.name
        parent_name = [self.category.name]
        parent_name.append(name)
        return " --> ".join(parent_name)

    def get_url(self):
        return reverse("products_by_subcategory", args=[self.category.slug, self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.CASCADE, to_field="name"
    )
    sub_category = models.ForeignKey(
        "SubCategory", null=True, blank=True, on_delete=models.CASCADE, to_field="name"
    )
    sku = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    full_slug = models.CharField(max_length=254, unique=True, blank=True)
    description = models.TextField(blank=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to="product",
        null=True,
        blank=True,
        default="defaults/default_product.jpg",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "product"
        verbose_name_plural = "products"

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = create_sku()
        self.slug = slugify(self.name)
        self.full_slug = (
            self.category.slug + "/" + self.sub_category.slug + "/" + self.slug
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse(
            "product_details",
            args=[self.category.slug, self.sub_category.slug, self.slug],
        )
