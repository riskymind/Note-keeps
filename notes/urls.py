from django.urls import path
import django.contrib.auth.views as auth_views
from . import views

app_name="notes"
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", auth_views.LoginView.as_view(template_name="notes/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="notes/logout.html"), name="logout"),
    path("home", views.home, name="home"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("settings", views.settings, name="settings")
]