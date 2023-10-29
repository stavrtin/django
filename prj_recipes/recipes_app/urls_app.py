from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.v_start, name='start'),
    path('start/', views.v_start, name='v_start'),
    path('page_recepts/', views.v_page_recepts, name='page_recepts'),

]
