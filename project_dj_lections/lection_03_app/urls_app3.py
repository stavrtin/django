from django.urls import path
from .views import hello
from .views import HelloView
from .views import df_year
from .views import MonthPost
from .views import my_view
from .views import TemplIf
from .views import view_for
from .views import index
from .views import about
from .views import post_full
from .views import author_posts


urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', df_year, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('my_view/<str:name_adres>/', my_view, name='my_view'),
    path('if/<int:post>', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='view_for'),
    path('index', index, name='start_page'),
    path('about', about, name='start_page'),
    path('post/<int:post_id>/', post_full, name='post_full'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
]
