from django.urls import path
from . import views

urlpatterns = [
    path("game1", views.game1, name="game1"),
    path("game2", views.game2, name="game1"),
    path("game3/<int:count_drop>", views.game3, name="game1"),
    path("select_all_n <int:n>", views.select_all_n, name="select_all_n"),
    path("start/<str:name>/", views.view_start, name="view_start"),
    path("author/<int:author_id>", views.view_author_art, name="view_author_art"),
    path("articl_full/<int:articl_id>", views.articl_full, name="articl_full"),
    ]