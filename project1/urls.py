from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),  # Sepet URL'leri
    path('', include('shop.urls', namespace='shop')),  # Ana sayfa ve ürünler
    path('accounts/', include('accounts.urls', namespace='accounts')),  # Kullanıcı işlemleri
    path('orders/', include('orders.urls', namespace='orders')),  # 📌 Sipariş URL'leri
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)