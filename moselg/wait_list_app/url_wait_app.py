from django.urls import path
from .views import v_start_page
from .views import v_about
from .views import v_message_beds
from .views import v_medorg_info
from .views import v_beds_info
from .views import v_zayavka
from .views import books
from .views import edit_report_beds
from .views import v_zayavka_info
from .views import cool_forms



urlpatterns = [
    path('', v_start_page, name='v_start_page'),
    path('about/', v_about, name='about'),
    path('beds/', v_message_beds, name='v_message_beds'),
    path('mo/', v_medorg_info, name='v_medorg_info'),
    path('bedsinfo/', v_beds_info, name='v_beds_info'),
    path('books/', books, name='books'),
    path('zayavka/', v_zayavka, name='v_zayavka'),
    # --------------- правки в докладах по койкам ---
    path('edit_report_beds/<int:report_beds_id>', edit_report_beds, name='edit_report_beds'),
    # --------лист 1.1 ЕЛГ ---
    path('zayavki/', v_zayavka_info, name='v_zayavka_info'),

#     ------- тест кул_форм-----
    path('cool/', cool_forms, name='cool_forms'),
]