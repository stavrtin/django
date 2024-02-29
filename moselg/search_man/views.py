from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# from .forms_search import BedsForm, ZayavkaForm, EditBedsForm, AuthUserForm, AuthenticationForm
from .forms_search import AuthUserForm, AuthenticationForm

# from .models import ReportBeds
# from .models import MedOrgMod
from .models import Contacts, Pacient, Hospices, Kis
from .filters import FilterKis

# from .tables import BedsTable
# from django.core.cache import cache
from openpyxl import Workbook

from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import User

# --------------------------- пагинация ----------
from django.core.paginator import Paginator







# Create your views here.

def v_about(request):
    return render(request, "search_man/base_moselg1.html")


def v_maine_page(request):
    return render(request, "search_man/main.html")


def v_start_page(request):
    # table_bed = ReportBeds.objects.raw('select * from '
    #                                                    '(SELECT *  from wait_list_app_reportbeds rep_beds '
    #                                                     'JOIN wait_list_app_hospis hosp on  rep_beds.filial_id = hosp.id '
    #                                                     'ORDER BY create_at DESC )'
    #                                    ' GROUP BY filial_id'
    #                                    )
    table_bed = ReportBeds.objects.raw('select distinct on (filial_id) filial_id, id, wait.id as id_w, '
                                       'create_at, beds_remont, beds_dop,  m_free,  f_free,  m_busy,    f_busy,    note '
                                       'from '
                                      '(select * from wait_list_app_reportbeds order by filial_id, create_at desc) wait'
                                       ' GROUP BY filial_id, '
                                       '  id,  id_w,    create_at, beds_remont,beds_dop, m_free, f_free, m_busy, f_busy, note '
                                       'order by filial_id, create_at desc;' )

    for i in table_bed:
        table_gzm =  3
        print(i)
    context = {"table_bed": table_bed}
    return render(request, "search_man/main_table_bed.html", context)


def v_medorg_info(request):
    # - просто вывод сведений об Мед орг

    meds = Hospis.objects.all()

    # ---------------  пагинация, классная ссылка https://www.youtube.com/watch?v=pDB9GSlQ7iY --
    paginator = Paginator(meds, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
               'page_obj': page_obj,

    }


    return render(request, "search_man/beds_info.html", context)

def v_message_beds(request):
    # --------запись данных из формы коек в БД РАПОРТ по КОЙКАМ  (через связку с ФОРМОЙ сразу)--
    if request.method == 'POST':
        form = BedsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')  # --- переход на ГЛАВНУЮ--
    else:
        form = BedsForm()
        page = 'beds1'
        context = {
                    'form': form,
                    'page' : page
                  }
    return render(request, 'search_man/bed_message_form.html', context=context)

def v_zayavka(request):
    # --------запись данных из формы коек в БД РАПОРТ по КОЙКАМ  (через связку с ФОРМОЙ сразу)--
    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/') # --- переход на ГЛАВНУЮ--
    else:
        form = ZayavkaForm()
        page = 'zayavka'
        context = {
                    'form': form,
                    'page' : page
                  }
    return render(request, 'search_man/zayavka.html', context=context)

def v_beds_info(request):
    # - просто вывод сведений об beds от Мед

    beds = ReportBeds.objects.all()

    # ---------- фильтры ---------------
    myFilter = OrderFilter(request.GET, queryset=beds)
    beds = myFilter.qs

    # ---- пагинация ----------
    # pagination = Paginator(beds, 5)
    #
    # page_number = request.GET.get('page')
    # page_obj = pagination.get_page(page_number)
    page = 'beds_info'
    context = {"beds": beds,
              'myFilter':myFilter,
              'page': page
               }
    return render(request, "search_man/beds_info.html", context)

# @login_required(login_url='/login/')
@login_required(login_url='/login1/')
def v_zayavka_info(request):
    # - просто вывод сведений о PATIENT

    zayavki = Kis.objects.all()

    # ---------- фильтры ---------------
    myFilterZayv = FilterKis(request.GET, queryset=zayavki)
    zayavki = myFilterZayv.qs
    page = 'zayav_info'

    # ---------------  пагинация, классная ссылка https://www.youtube.com/watch?v=pDB9GSlQ7iY --
    paginator = Paginator(zayavki, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {"zayavki": zayavki,
              'myFilter':myFilterZayv,
              'page_obj':page_obj,
               'page': page
               }


    return render(request, "search_man/zayavki_list.html", context)

@login_required(login_url='/login1/')
def v_elg(request):
    return render(request, 'search_man/elg_info.html', )


def edit_report_beds(request, report_beds_id: int):
    # ------- изменение значений полей из РАПОРТА по койкам -------
    # ------- тут  правим только   report.m_free и report.f_free---

    report = ReportBeds.objects.get(id=report_beds_id)
    report_namemo = report.filial
    report_m_free = report.m_free
    report_f_free = report.f_free

    if request.method == 'POST':
        form = BedsForm(request.POST)

        if form.is_valid():

            m_free = form.cleaned_data['m_free']
            f_free = form.cleaned_data['f_free']
            # logger.info(f'Получили {name=}, {email=}, {age=}.')
            report.m_free = m_free
            report.f_free = f_free
            report.save()
            message = 'Пользователь сохранён'
            context = {
                'message': message,
                'report_namemo':report_namemo,
                'report_m_free': m_free,
                'report_f_free': f_free,
            }
    else:
        # ----- передаем парметры для заполнения полей в форме -----
        form = EditBedsForm(initial={
                            'med_org': report.filial,
                            # 'm_employ': report.m_employ,
                            # 'f_employ': report.f_employ,
                            'm_free': report.m_free,
                            'f_free': report.f_free,
                                                },
                            name_edited_med_org=report.filial   )

        message = 'Заполните форму'
    context = {
    # 'message': message,
        'report_namemo': report_namemo,
        'report_m_free': report_m_free,
        'report_f_free': report_f_free,
        'form': form,
        }
    return render(request, 'search_man/report_bed_edit.html', context=context)

def cool_forms(request):
    context = {'form': BedsForm()}
    return render(request, 'search_man/test_cool_form.html', context=context)


def v_login(request):
    page = 'author'
    context = { 'page': page
               }
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/') # --- переход на ГЛАВНУЮ--
    else:
        form = AuthUserForm()

        page = 'author'
        context = {'form': form,
                   'page': page
                   }
    return render(request, 'search_man/login.html', context=context)





# ------------ авторизация ---------
class MyprojectLoginView(LoginView):
    template_name = 'search_man/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('v_start_page') # - - куда переходим после авториз
    def get_success_url(self):
        return self.success_url


class MyprojectLogout(LogoutView):
    next_page  = reverse_lazy('v_start_page')

# -----------тест поиск----
def v_medorg_search(request):
    # - просто вывод сведений об Мед орг
    meds = Hospis.objects.all()
    context = {"meds": meds}

    return render(request, "search_man/test_search.html", context)

# ------------ вывод коечнызх таблиц------------
def v_table_bed(request):
    # - просто вывод сведений об Мед орг
    table_bed = Hospis.objects.all()

    # for i in table_bed:
    #     table_gzm =  3
    # ---------------  пагинация, классная ссылка https://www.youtube.com/watch?v=pDB9GSlQ7iY --
    paginator = Paginator(table_bed, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
               'page_obj': page_obj,
               # 'table_kis' : table_kis,

    }
    return render(request, "search_man/test_table_bed.html", context)

def v_results(request):
    # - просто вывод дашбордов -
    page = 'results'
    context = { 'page': page
               }
    return render(request, "search_man/base_results.html", context)


    return render(request, "search_man/base_results.html")

def v_kis_page(request):
    page = 'kis'
    table_kis = Kis.objects.all()
# ---------------- фильтры в кис ------
    myFilterKis = FilterKis(request.GET, queryset=table_kis)
    table_kis_f = myFilterKis.qs


# ---------------  пагинация, классная ссылка https://www.youtube.com/watch?v=pDB9GSlQ7iY --
    paginator = Paginator(table_kis_f, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)


    context = { 'page': page,
                'myFilter': myFilterKis,
                'page_obj' : page_obj,
                'table_kis' : table_kis_f,
               }
    return render(request, 'search_man/search_kis.html', context=context)

import pandas as pd
from django.db.models import Count
from itertools import chain
from django.db.models.query import RawQuerySet
from django.db import connection
def v_kis_page_test(request):
    page = 'kis_2'

    # table_kis = Kis.objects.select_related().all()# ---------------- фильтры в кис ------
    table_kis = Kis.objects.all().filter(ishod='Умер в стационаре')# ---------------- фильтры в кис ------
    # table_kis = Kis.objects.all()# ---------------- фильтры в кис ------
    myFilterKis = FilterKis(request.GET, queryset=table_kis)
    table_kis_f = myFilterKis.qs   # --- результат применения фильтра
    table_kis_start_date = myFilterKis.data.get('start_date')
    table_kis_end_date = myFilterKis.data.get('end_date1')
    str_test = f'start_date={table_kis_start_date}&end_date1={table_kis_end_date}'

    # kis_tel = Contacts.objects.select_related().filter(kont_pac__in=[p.pacient.kod_p for p in table_kis_f])

# ---------------  пагинация, классная ссылка https://www.youtube.com/watch?v=pDB9GSlQ7iY --
    paginator = Paginator(table_kis_f, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)


    context = { 'page': page,
                'myFilter': myFilterKis,
                'page_obj' : page_obj,
                # 'cont_all' : cont_all,
                # 'test_con' : test_con,
                'table_kis_f' : table_kis_f, # --- результат применения фильтра
                'table_kis_start_date' : table_kis_start_date,
                'table_kis_end_date' : table_kis_end_date,
                'str_test' : str_test,
                }


    # # ------------- Эксель ----------
    # # submitbutton = request.POST.get("submit ")
    if request.method == 'POST':
        form = FilterKis(request.POST)
        if form.is_valid():
            print(table_kis_start_date)

            response = HttpResponse(content_type='application/ms-excel')
            file_name = f'"dead_{table_kis_start_date}_{table_kis_end_date}.xlsx"'
            print(file_name)
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            wb = Workbook()
            ws = wb.active
            ws.title = "Products"
            # Add headers
            headers = ["ФИО_пациента", "Дата_рождения",
                       "Дата_смерти", "ФИО_контактного_лица", "Телефон_конт."]
            ws.append(headers)
            # Add data from the model
            table_kis = Kis.objects.all()            # ---------------- фильтры в кис ------
            myFilterKis = FilterKis(request.GET, queryset=table_kis)
            table_kis_f = myFilterKis.qs

            result = table_kis_f

            for res_ in result:
                for cont in res_.pacient.cont.all():
                    ws.append([res_.pacient.pacient,
                               res_.data_rozhd,
                               res_.data_vipiski,
                               cont.kont_fio,
                               cont.kont_tel,
                               ])

            # Save the workbook to the HttpResponse
            wb.save(response)
            # print(table_kis_f)
            return response # ------------- Эксель ----------

    return render(request, 'search_man/search_kis_test.html',
                  context=context)




