from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("index.urls")),
    path("products/", include("products.urls")),
    path("search/", include("search.urls")),
    path("basket/", include("basket.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("profiles.urls")),
    path("wishlist/", include("wishlist.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
