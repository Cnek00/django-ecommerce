from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"]
                )
            cart.clear()  # Sipariş verildiğinde sepeti temizle
            return render(request, "orders/order_success.html", {"order": order})
    else:
        form = OrderForm()

    return render(request, "orders/order_create.html", {"cart": cart, "form": form})
