from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms_moselg import BedsForm, ZayavkaForm
from .models import ReportBedsMod
from .models import MedOrgMod


# Create your views here.

def v_about(request):
    return render(request, "wait_list_app/base_moselg.html")


def v_start_page(request):
    return render(request, "wait_list_app/base_moselg.html")



def v_medorg_info(request):
    # - просто вывод сведений об Мед орг

    meds = MedOrgMod.objects.all()
    context = {"meds": meds}
    return render(request, "wait_list_app/test.html", context)

def v_beds_info(request):
    # - просто вывод сведений об beds от Мед

    beds = ReportBedsMod.objects.all()
    context = {"beds": beds}
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
    return render(request, 'wait_list_app/bed_message_form.html', {'form': form})


def v_zayavka(request):
    # --------запись данных из формы коек в БД РАПОРТ по КОЙКАМ  (через связку с ФОРМОЙ сразу)--
    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/') # --- переход на ГЛАВНУЮ--
    else:
        form = ZayavkaForm()
    return render(request, 'wait_list_app/zayavka.html', {'form': form})


# -------------- это - просто к форме (без связки модель-форма) --------
# def v_message_beds(request):
#     # --------запись данных из формы коек в БД РАПОРТ по КОЙКАМ ------
#     if request.method == 'POST':
#         form = BedsForm(request.POST)
#         if form.is_valid():
#             name_med_org = form.cleaned_data['medorg'][0]
#             # name_medorg_id = form.cleaned_data['medorg'][0].id
#             m_employ = form.cleaned_data['m_employ']
#             f_employ = form.cleaned_data['f_employ']
#             m_free = form.cleaned_data['m_free']
#             f_free = form.cleaned_data['f_free']
#             # Делаем что-то с данными
#             # logger.info(f'----------Отправлено {name=}, {email=}, {age=}.')
#             report_bed = ReportBedsMod(med_org=name_med_org,
#                                        m_employ=m_employ,
#                                        f_employ=f_employ,
#                                        m_free=m_free,
#                                        f_free=f_free
#                                        )
#             report_bed.save()
#             print(form.cleaned_data['medorg'])
#             print(form.cleaned_data['medorg'][0].id)
#     else:
#         form = BedsForm()
#     return render(request, 'wait_list_app/bed_message_form.html', {'form': form})
