from django import forms
# from django.forms import ModelForm
from .models import MedOrgMod
from .models import ReportBedsMod
from .models import ZayavkaNaGospit
import datetime


class BedsForm(forms.ModelForm):
    # ----- форма ввода данных для передачи инф по КОЙКАМ -------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["med_org"].empty_label='Не выбран стационар'
        self.fields["med_org"].label='Выберите стационар'
    class Meta:
        model = ReportBedsMod
        fields = ['med_org',  'm_employ', 'f_employ',
                'm_free' ,        'f_free',
                 ]

class EditBedsForm(forms.ModelForm):
# -- форма ввода данных по ИЗМЕНЕНИЮ инф по уже переданным КОЙКАМ ----
    def __init__(self, name_edited_med_org, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["med_org"].empty_label= name_edited_med_org
        self.fields["med_org"].label='Выберите стационар'
    class Meta:
        model = ReportBedsMod
        fields = ['med_org',  'm_employ', 'f_employ',
                'm_free' ,        'f_free',
                 ]

class ZayavkaForm(forms.ModelForm):
    # ----- форма ввода данных для передачи инф по ПАЦИЕНТУ -------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["quickly_categor"].empty_label='Не выбран признак срочности'
        self.fields["gender"].empty_label='Не выбран пол'
        self.fields["fio"].label='Введите фио'
    class Meta:
        model = ZayavkaNaGospit
        fields = '__all__'



# class BedsForm(forms.Form):
#     # ----- форма ввода данных для передачи инф по КОЙКАМ -------------
#
#     medorg = forms.ModelMultipleChoiceField(queryset=MedOrgMod.objects.all()
#     # medorg = forms.ModelChoiceField(queryset=MedOrgMod.objects.all()
#                                             , label="Укажите стационар"
#                                             , required=False
#                                             , widget=forms.SelectMultiple
#                                             , help_text="Unselect the photos you want to delete",
#                                             )
#                                             # empty_label="(Nothing)")
#
#
#
#     # medorg = forms.ModelMultipleChoiceField(queryset=MedOrgMod.objects.none())
#     m_employ = forms.IntegerField(min_value=0, max_value=50)
#     f_employ = forms.IntegerField(min_value=0, max_value=50)
#     m_free = forms.IntegerField(min_value=0, max_value=50)
#     f_free = forms.IntegerField(min_value=0, max_value=50)


