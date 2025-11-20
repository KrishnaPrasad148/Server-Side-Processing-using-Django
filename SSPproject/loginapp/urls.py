from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("home/", views.home, name="home"),
]
