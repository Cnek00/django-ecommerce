from django.urls import path
from .views import product_list, product_detail, favorite_list, add_to_favorites, remove_from_favorites

app_name = "shop"

urlpatterns = [
    path("", product_list, name="product_list"),  # Ana sayfa
    path("favorites/", favorite_list, name="favorites"),  # ✅ Favori listesi
    path("favorites/add/<int:product_id>/", add_to_favorites, name="add_to_favorites"),  # ✅ Favori ekleme
    path("favorites/remove/<int:product_id>/", remove_from_favorites, name="remove_from_favorites"),  # ✅ Favori kaldırma
    path("product/<slug:product_slug>/", product_detail, name="product_detail"),  # Ürün detay
    path("<slug:category_slug>/", product_list, name="product_list_by_category"),  # ✅ En sona alındı (kategori çakışmasını önlemek için)
]