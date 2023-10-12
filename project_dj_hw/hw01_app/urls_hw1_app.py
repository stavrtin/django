from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_index, name="hwgame1"),
    path("about/", views.about, name="hwgame1"),
    path("user_ords/<int:user_id>", views.users_orders, name="user_ords"),
    path("users_prods/<int:user_id> <int:period>", views.users_prods, name="users_prods"),
    path("add_user", views.add_user, name="add_user"),
    path("edit_user/<int:user_id>", views.edit_user, name="edit_user"),
]