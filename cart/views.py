from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from shop.models import Product
from .cart import Cart
from django.contrib import messages


@require_POST


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data["quantity"]
        if not cart.add(product=product, quantity=quantity, override_quantity=False):
            messages.error(request, "Stok yetersiz! Maksimum alabileceğiniz adet: {}".format(product.stock))
            return redirect("shop:product_detail", product_slug=product.slug)

    return redirect("cart:cart_detail")



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")
