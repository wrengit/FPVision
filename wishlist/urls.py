from django.urls import path
from . import views


urlpatterns = [
    path("", views.view_wishlist, name="view_wishlist"),
    path(
        "add_to_wishlist/<product_id>/",
        views.add_to_wishlist,
        name="add_to_wishlist"
    ),
    path(
        "adjust_wishlist/<product_id>/",
        views.adjust_wishlist,
        name="adjust_wishlist"
    ),
    path(
        "remove_from_wishlist/<product_id>/",
        views.remove_from_wishlist,
        name="remove_from_wishlist",
    ),
    path(
        "add_wishlist_to_basket/",
        views.add_wishlist_to_basket,
        name="add_wishlist_to_basket",
    ),
]
