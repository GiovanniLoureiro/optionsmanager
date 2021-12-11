from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.list_all_positions, name="list_positions"),
    path("add/", views.add_position, name="add_position"),
]