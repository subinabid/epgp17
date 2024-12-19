"""URL configuration for APIs."""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("auth/login/", views.login),
    path("auth/logout/", views.logout),
    path("users/", views.get_users),
    path("users/create/", views.create_user),
    path("users/<int:id>/", views.get_user),
    path("users/<int:id>/update", views.update_user),
    path("users/<int:id>/delete", views.delete_user),
]
