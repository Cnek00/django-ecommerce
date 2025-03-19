from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[("pending", "Beklemede"), ("completed", "Tamamlandı"), ("failed", "Başarısız")])
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ödeme {self.order.id} - {self.status}"
