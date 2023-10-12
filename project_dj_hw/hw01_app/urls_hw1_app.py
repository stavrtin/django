from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_index, name="hwgame1"),
    path("about/", views.about, name="hwgame1"),
    path("user_ords/<int:user_id>", views.users_orders, name="user_ords"),
    path("users_prods/<int:user_id> <int:period>", views.users_prods, name="users_prods"),
]