from .views import hello, HelloView, df_year, MonthPost, my_view, TemplIf, view_for
from django.urls import path

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', df_year, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('start/<str:name_adres>/', my_view, name='my_view'),
    path('if/<int:post>', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='view_for'),
    # path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
]
