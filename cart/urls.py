from django.urls import path
from .views import cart_add, cart_remove, cart_detail, cart_clear

app_name = "cart"

urlpatterns = [
    path("", cart_detail, name="cart_detail"),  # 🛒 Sepet sayfası
    path("add/<int:product_id>/", cart_add, name="cart_add"),  # ➕ Sepete ekleme
    path("remove/<int:product_id>/", cart_remove, name="cart_remove"),  # ❌ Sepetten çıkarma
    path("clear/", cart_clear, name="cart_clear"),  # 🔄 Sepeti temizleme
]
