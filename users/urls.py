from django.urls import path, include, reverse_lazy
from users import views
from django.contrib.auth import views as auth_views

# from django.contrib.

# app_name = "users"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # path(
    #     "accounts/password_change/",
    #     auth_views.PasswordChangeView.as_view(success_url="done/"),
    #     name="password_change",
    # ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]

# from django.contrib.auth.urls import urlpatterns
