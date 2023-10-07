from django.urls import path
from sem01_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    # path("new/", views.new, name="new"),
]
