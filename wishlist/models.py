from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="Wishlist",
    )
    wishlist_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )

    def update_total(self):
        self.wishlist_total = (
            self.wishlistitems.aggregate(Sum("wishlistitem_total"))[
                "wishlistitem_total__sum"
            ]
            or 0
        )
        self.save()


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="wishlistitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    wishlistitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        self.wishlistitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} on wishlist"
