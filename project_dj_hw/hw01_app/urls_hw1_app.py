from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_index, name="hwgame1"),
    path("about/", views.about, name="hwgame1"),
    # path("hwgame3", views.hwgame3, name="hwgame1"),
    # path("about/", views.about, name="about"),
    # path("new/", views.new, name="new"),
]