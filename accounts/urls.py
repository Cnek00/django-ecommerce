from django.urls import path
from .views import register, user_login, user_logout, profile, update_profile, change_password

app_name = "accounts"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/update/", update_profile, name="update_profile"),
    path("profile/change-password/", change_password, name="change_password"),
]
