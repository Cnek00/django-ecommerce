
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

from django.db import models
from django.db.models import Avg

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Stok: {self.stock})"  # ✅ String formatı düzeltilmiş hali

    def average_rating(self):
        avg = self.reviews.aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return avg if avg else 0  # ✅ Eğer ortalama yoksa sıfır döndür

    

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 arası puan
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating}) "

from django.contrib.auth.models import User
from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")  # Aynı ürünü tekrar favorilere eklemeyi engeller

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
