from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.list_all_positions, name="list_positions"),
    path("add_option/", views.add_option, name="add_option"),
    path("add_trade/", views.add_trade, name="add_trade"),
]