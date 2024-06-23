from django.apps import AppConfig
from django.urls import path
from . import views


class UserlistappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UserListApp'



urlpatterns = [
    path("", views.index, name="index"),
]