from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)  # Kullanıcıyı otomatik giriş yap
            return redirect("shop:product_list")  # Ana sayfaya yönlendir
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("shop:product_list")  # Giriş sonrası ana sayfaya yönlendir
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("shop:product_list")  # Çıkış sonrası ana sayfaya yönlendir

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from orders.models import Order


from .models import UserProfile


@login_required
def profile(request):
    # Eğer kullanıcı için bir profil kaydı yoksa, oluştur
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    orders = Order.objects.filter(email=request.user.email)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "accounts/profile.html", {"form": form, "orders": orders})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required
def update_profile(request):
    user_profile = request.user.userprofile
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "accounts/update_profile.html", {"form": form})

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Kullanıcının oturumunu açık tut
            return redirect("accounts:profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/change_password.html", {"form": form})

