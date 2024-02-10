from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes_app.models import Recipe

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username',
                  # 'email',
                  # 'password1',
                  # 'password2'
                  )
        widgets = {
        'username' :  forms.TextInput(),
        'password1':  forms.PasswordInput(attrs={'class': 'form-input'}),
        'password2' : forms.PasswordInput(attrs={'class': 'form-input'}),

        }

class ReceptForm(forms.ModelForm):
    # ----- форма ввода данных для передачи инф по КОЙКАМ -------------

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields["med_org"].empty_label='Не выбран стационар'
        # self.fields["rec_name"].label='Выберите стационар'

        # self.fields["m_employ"].label='Занято коек (м)'
        # self.fields["f_employ"].label='Занято коек (ж)'
        # self.fields["m_free"].label='Свободно коек (м)'
        # self.fields["f_free"].label='Свободно коек (ж)'

        # self.fields["f_remont"].widget = forms.NumberInput(attrs={'class': 'form-control', 'size': '10'})
        # self.fields["m_remont"].widget = forms.NumberInput(attrs={
        #     'class': 'form-special',
        #     'title': 'Your name',
        #     # 'style' :
        #         'color':'blue',
        #     'size': '5'})
        # self.fields["m_free"].widget = forms.NumberInput(attrs={'class': 'form-control', 'size': '10'})
        # self.fields["f_free"].widget = forms.NumberInput(attrs={'class': 'form-control', 'size': '10'})

    class Meta:
        model = Recipe
        fields = '__all__'
        # fields =  ['rec_name',
        #           'rec_description', 'rec_time',
        #          ]
        # widgets = {'med_org': forms.Select(attrs={'id':'select_mo', 'class': 'form-control form-control-lg  select' })}



