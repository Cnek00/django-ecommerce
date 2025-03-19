import iyzipay
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PaymentForm
from orders.models import Order
from .models import Payment

def process_payment(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_request = {
                "locale": "tr",
                "conversationId": str(order.id),
                "price": str(order.items.aggregate(total=models.Sum("price"))["total"]),
                "paidPrice": str(order.items.aggregate(total=models.Sum("price"))["total"]),
                "installment": int(form.cleaned_data["installment"]),
                "paymentCard": {
                    "cardHolderName": form.cleaned_data["card_name"],
                    "cardNumber": form.cleaned_data["card_number"],
                    "expireMonth": form.cleaned_data["expiry_month"],
                    "expireYear": form.cleaned_data["expiry_year"],
                    "cvc": form.cleaned_data["cvv"],
                    "registerCard": "0",
                },
            }

            response = iyzipay.Payment().create(payment_request, options={
                "apiKey": settings.IYZICO_API_KEY,
                "secretKey": settings.IYZICO_SECRET_KEY,
                "baseUrl": settings.IYZICO_BASE_URL
            })

            if response["status"] == "success":
                Payment.objects.create(order=order, status="completed", transaction_id=response["paymentId"])
                return redirect("orders:order_create")
            else:
                Payment.objects.create(order=order, status="failed")
                return render(request, "payment/payment_failed.html", {"error": response["errorMessage"]})
    else:
        form = PaymentForm()

    return render(request, "payment/payment_form.html", {"form": form, "order": order})
