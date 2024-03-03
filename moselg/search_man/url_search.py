from django.urls import path
from .views import v_start_page, v_maine_page, v_elg
from .views import v_about
from .views import v_message_beds
from .views import v_medorg_info
from .views import v_beds_info
from .views import v_zayavka
# from .views import books
from .views import edit_report_beds
from .views import v_zayavka_info
from .views import cool_forms
from .views import v_login
from .views import MyprojectLoginView
from .views import MyprojectLogout
from .views import v_medorg_search
from .views import v_table_bed
from .views import v_results
# from .views import v_kis_page
from .views import v_kis_dead_contacts




urlpatterns = [
    # path('', v_start_page, name='v_start_page'),
    path('', v_maine_page, name='v_start_page'),
    path('about/', v_about, name='about'),
    path('beds/', v_message_beds, name='v_message_beds'),
    path('mo/', v_medorg_info, name='v_medorg_info'), # ----- beds_info.html
    path('bedsinfo/', v_beds_info, name='v_beds_info'),
    # path('books/', books, name='books'),
    path('zayavka/', v_zayavka, name='v_zayavka'),
    # --------------- правки в докладах по койкам ---
    path('edit_report_beds/<int:report_beds_id>', edit_report_beds, name='edit_report_beds'),
    # --------лист 1.1 ЕЛГ ---
    path('zayavki/', v_zayavka_info, name='v_zayavka_info'),
        #     ------- тест кул_форм-----
    path('cool/', cool_forms, name='cool_forms'),
        #     ------- login-----
    path('login1/', MyprojectLoginView.as_view(), name='login_page'),
    # path('login/', v_login, name='v_login'),
        #     ------- logout-----
    path('logout/', MyprojectLogout.as_view(), name='logout_page'),
        #     ------- search-----
    path('medorg_search/', v_medorg_search, name='medorg_search'),
    # path('tablbeds/', v_table_bed, name='table_beds'),
    path('results/', v_results, name='results'),
    # path('kis/', v_kis_page, name='kis_page'),
    path('kis_dead_contacts/', v_kis_dead_contacts, name='kis_page'),
    path('elg/', v_elg, name='v_elg'),
    # path('button_view/', button_view, name='button_view'),


]