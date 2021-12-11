from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.list_all_positions, name="list_positions")
]