from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms_moselg import BedsForm, ZayavkaForm, EditBedsForm, AuthUserForm, AuthenticationForm

from .models import ReportBedsMod
from .models import MedOrgMod
from .models import ZayavkaNaGospit

from django.views.generic import CreateView, ListView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import User



from .filters import OrderFilter, FilterZayavki

from .tables import BedsTable




# Create your views here.

def v_about(request):
    return render(request, "wait_list_app/base_moselg.html")

def v_start_page(request):
    page = 'main'
    context = {
        'page': page
            }
    return render(request, "wait_list_app/base_moselg.html",context=context)



def v_medorg_info(request):
    # - просто вывод сведений об Мед орг

    meds = MedOrgMod.objects.all()
    context = {"meds": meds}
    return render(request, "wait_list_app/test.html", context)

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
    return render(request, 'wait_list_app/bed_message_form.html', context=context)

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
    return render(request, 'wait_list_app/zayavka.html', context=context)

def v_beds_info(request):
    # - просто вывод сведений об beds от Мед

    beds = ReportBedsMod.objects.all()

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
    return render(request, "wait_list_app/test.html", context)

def v_zayavka_info(request):
    # - просто вывод сведений о PATIENT

    zayavki = ZayavkaNaGospit.objects.all()

    # ---------- фильтры ---------------
    myFilterZayv = FilterZayavki(request.GET, queryset=zayavki)
    zayavki = myFilterZayv.qs
    page = 'zayav_info'
    context = {"zayavki": zayavki,
              'myFilter':myFilterZayv,
              # 'page_obj':page_obj,
               'page': page
               }
    return render(request, "wait_list_app/zayavki_list.html", context)

def books(request):
    table = BedsTable(ReportBedsMod.objects.all())
    return render(request, 'wait_list_app/test.html', {'table': table})


def edit_report_beds(request, report_beds_id: int):
    # ------- изменение значений полей из РАПОРТА по койкам -------
    # ------- тут  правим только   report.m_free и report.f_free---

    report = ReportBedsMod.objects.get(id=report_beds_id)
    report_namemo = report.med_org
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
                            'med_org': report.med_org,
                            'm_employ': report.m_employ,
                            'f_employ': report.f_employ,
                            'm_free': report.m_free,
                            'f_free': report.f_free,
                                                },
                            name_edited_med_org=report.med_org   )

        message = 'Заполните форму'
    context = {
    'message': message,
        'report_namemo': report_namemo,
        'report_m_free': report_m_free,
        'report_f_free': report_f_free,
        'form': form,
        }
    return render(request, 'wait_list_app/report_bed_edit.html', context=context)

def cool_forms(request):
    context = {'form': BedsForm()}
    return render(request, 'wait_list_app/test_cool_form.html', context=context)


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
    return render(request, 'wait_list_app/login.html', context=context)





# ------------ авторизация ---------
class MyprojectLoginView(LoginView):
    template_name = 'wait_list_app/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('v_start_page') # - - куда переходим после авториз
    def get_success_url(self):
        return self.success_url


class MyprojectLogout(LogoutView):
    next_page  = reverse_lazy('v_start_page')
