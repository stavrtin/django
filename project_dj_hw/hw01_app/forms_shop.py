from django import forms


class ProdFieldsForm(forms.Form):
    prodname = forms.CharField()
    email = forms.EmailField()
    description = forms.CharField()
    price = forms.DecimalField()
    amount = forms.FloatField()


class UserFieldsForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    phone = forms.CharField()
    adres = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class UserEditFieldsForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    phone = forms.CharField()

class ImageForm(forms.Form):
    image = forms.ImageField()
