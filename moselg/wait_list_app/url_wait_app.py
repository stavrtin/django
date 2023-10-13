from django.urls import path
from .views import v_start_page
from .views import v_about
# from .views import user_manyform



urlpatterns = [
    path('', v_start_page, name='v_start_page'),
    path('about/', v_about, name='about'),
    # path('forms/', user_manyform, name='user_manyform'),
    # path('add_user/', add_user, name='add_user'),
    # path('upload_img/', upload_img, name='upload_img'),
]