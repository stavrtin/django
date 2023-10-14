from django.urls import path
from .views import v_start_page
from .views import v_about
from .views import v_message_beds
from .views import v_medorg_info
from .views import v_beds_info
from .views import v_zayavka



urlpatterns = [
    path('', v_start_page, name='v_start_page'),
    path('about/', v_about, name='about'),
    path('beds/', v_message_beds, name='v_message_beds'),
    path('mo/', v_medorg_info, name='v_medorg_info'),
    path('bedsinfo/', v_beds_info, name='v_medorg_info'),
    path('zayavka/', v_zayavka, name='v_zayavka'),

]