from django.urls import path
from .views import user_form
from .views import user_manyform
from .views import add_user
from .views import upload_img
from .views import lec4_start
from .views import edit_user



urlpatterns = [
    path('', lec4_start, name='lec4_start'),
    path('user/add/', user_form, name='user_form'),
    path('forms/', user_manyform, name='user_manyform'),
    path('add_user/', add_user, name='add_user'),
    path('upload_img/', upload_img, name='upload_img'),
    path('edit_user/<int:user_id>', edit_user, name='edit_user'),
]
