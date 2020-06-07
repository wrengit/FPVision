from django.urls import path
from . import views


urlpatterns = [
    path("", views.search_result, name="search_result"),
    path("js_search/", views.js_search, name="js_search"),
]
