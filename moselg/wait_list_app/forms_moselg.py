from django import forms
# from django.forms import ModelForm
# from .models import MedOrgMod
from .models import ReportBeds
from .models import ZayavkaNaGospit
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import User

class BedsForm(forms.ModelForm):
    # ----- форма ввода данных для передачи инф по КОЙКАМ -------------


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["filial"].empty_label='Не выбран стационар'
        self.fields["filial"].label='Выберите стационар'

        # self.fields["m_employ"].label='Занято коек (м)'
        # self.fields["f_employ"].label='Занято коек (ж)'
        # self.fields["m_free"].label='Свободно коек (м)'
        # self.fields["f_free"].label='Свободно коек (ж)'

        # self.fields["f_remont"].widget = forms.NumberInput(attrs={'class': 'form-control', 'size': '10'})
        self.fields["beds_remont"].widget = forms.NumberInput(attrs={
            'class': 'form-special',
            'title': 'Your name',
            # 'style' :
                'color':'blue',
            'size': '5'})
        # self.fields["m_free"].widget = forms.NumberInput(attrs={'class': 'form-control', 'size': '10'})
        # self.fields["f_free"].widget = forms.NumberInput(attrs={'class': 'form-control', 'size': '10'})

    class Meta:
        model = ReportBeds
        fields = '__all__'
            # ['med_org',
            #       # 'm_employ', 'f_employ',     'm_free' ,
            #       # 'f_free',
            #      ]
        widgets = {'filial': forms.Select(attrs={'id':'select_mo', 'class': 'form-control form-control-lg  select' })}





class EditBedsForm(forms.ModelForm):
# -- форма ввода данных по ИЗМЕНЕНИЮ инф по уже переданным КОЙКАМ ----
    def __init__(self, name_edited_med_org, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["filial"].empty_label= name_edited_med_org
        self.fields["filial"].label='Выберите стационар'
        # self.fields["m_employ"].label='Занято коек (м)'
        # self.fields["f_employ"].label='Занято коек (ж)'
        # self.fields["m_free"].label='Свободно коек (м)'
        # self.fields["f_free"].label='Свободно коек (ж)'

    class Meta:
        model = ReportBeds
        fields = ['filial',
                #   'm_employ', 'f_employ',
                # 'm_free' ,        'f_free',
                 ]

class ZayavkaForm(forms.ModelForm):
    # ----- форма ввода данных для передачи инф по ПАЦИЕНТУ -------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["filial"].empty_label='Не выбран источник заявки'

        self.fields["quickly_categor"].empty_label='Не выбран признак срочности'
        self.fields["gender"].empty_label='Не выбран пол'

        self.fields["fio"].label='Введите фио'
        self.fields["fio"].widget = forms.TextInput(attrs={'class': 'special',
                                                           'size': '50'})

        self.fields["quickly_categor"].label='Введите катег'
        # self.fields["quickly_categor"].widget = forms.ChoiceField(attrs={'class': 'form-control'})
        # self.fields["quickly_categor"].widget = forms.RadioSelect(attrs={'class': 'form-check-input'})

        self.fields["birthday"].label='Введите ДР'
        self.fields["birthday"].widget = forms.DateInput(attrs={'class': 'form-control', 'type':'date'})
        self.fields["dateVk"].widget = forms.DateInput(attrs={'class': 'form-control', 'type':'date'})


    class Meta:
        model = ZayavkaNaGospit
        fields = '__all__'
        widgets = {'filial': forms.Select(attrs={'id': 'select_mo', 'class': 'form-control form-control-lg  select'})}


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'





# class BedsForm(forms.Form):
#     # ----- форма ввода данных для передачи инф по КОЙКАМ c CRISPY-------------
#
#
#     # medorg = forms.ModelMultipleChoiceField(queryset=MedOrgMod.objects.all()
#     # # medorg = forms.ModelChoiceField(queryset=MedOrgMod.objects.all()
#     #                                         , label="Укажите стационар"
#     #                                         , required=False
#     #                                         , widget=forms.SelectMultiple
#     #                                         , help_text="Unselect the photos you want to delete"
#     #                                         , empty_label="(Nothing)")
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('submit','Submit' ))
#
#     MO = (
#         (1, '1. ГКБ-15'),
#         (2, '2. ГКБ-16'),
#         (3, '3. ГКБ-17'),
#         (4, '4. ГКБ-165'),
#         (5, '15. 1 ОПМП'),
#         (6, '21. 2 ОПМП'),
#            )
#     med_org = forms.ChoiceField(choices=MO)
#     m_employ = forms.IntegerField(min_value=0, max_value=50)
#     f_employ = forms.IntegerField(min_value=0, max_value=50)
#     m_free = forms.IntegerField(min_value=0, max_value=50)
#     f_free = forms.IntegerField(min_value=0, max_value=50)
#


