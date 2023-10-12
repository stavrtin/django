from django.urls import path
from .views import user_form
from .views import user_manyform
from .views import add_user
from .views import upload_img
# from .views import HelloView
# from .views import df_year
# from .views import MonthPost
# from .views import my_view
# from .views import TemplIf
# from .views import view_for
# from .views import index
# from .views import about
# from .views import post_full
# from .views import author_posts


urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', user_manyform, name='user_manyform'),
    path('add_user/', add_user, name='add_user'),
    path('upload_img/', upload_img, name='upload_img'),
]
