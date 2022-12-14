from django.urls import path
from .views import OwnerView, ShopView, ProductView

urlpatterns = [
    path("owners", OwnerView.as_view()),
    path("shops", ShopView.as_view()),
    path("products", ProductView.as_view()),
]
