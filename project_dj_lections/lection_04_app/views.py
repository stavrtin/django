import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms_app4 import UserForm
from .forms_app4 import ManyFieldsForm
from .forms_app4 import ManyFieldsFormWidget
from .forms_app4 import ImageForm
from .models import User

logger = logging.getLogger(__name__)


# Create your views here.

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'----------Отправлено {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'lection_04_app/user_form.html', {'form': form})


def user_manyform(request):
    if request.method == 'POST':
        # form = ManyFieldsForm(request.POST)
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'----------Отправлено {form.cleaned_data=}.')
    else:
        # form = ManyFieldsForm()
        form = ManyFieldsFormWidget()
    return render(request, 'lection_04_app/user_manyfield_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'lection_04_app/user_form.html', {'form': form, 'message': message})



def upload_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()

    return render(request, 'lection_04_app/upload_img.html', {'form': form})
