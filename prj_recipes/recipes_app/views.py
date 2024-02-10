from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.http import HttpResponse, HttpResponseRedirect

from .models import Recipe, Category, Ingredients
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .utils import DataMixin
from .forms import RegisterUserForm, ReceptForm


def v_start(request):
    page = 'start'
    categoryes = Category.objects.all()
    context = {'page': page,
                   'categoryes': categoryes}
    return render(request, "recipes_app/start.html", context=context)


def v_page_recepts(request):
    recipe = Recipe.objects.all()
    ingreds = Ingredients.objects.all()
    page = 'page_recepts'
    context = {'page': page,
               'recipe': recipe,
               'ingreds': ingreds,
                              }
    return render(request, "recipes_app/recepts.html", context=context)


class RegisterUser(DataMixin, CreateView):
    # --------------------- регистрация -----------
    form_class = RegisterUserForm
    template_name = 'recipes_app/register.html'
    success_url = reverse_lazy('start')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация", page='register')

        return dict(list(context.items()) + list(c_def.items()))

def v_add_recept(request):
    # --------запись данных из формы рецепт БД  (через связку с ФОРМОЙ сразу)--
    if request.method == 'POST':
        form = ReceptForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')  # --- переход на ГЛАВНУЮ--
    else:
        form = ReceptForm()
        page = 'add_recept'
        context = {
                    'form': form,
                    'page' : page
                  }
    return render(request, 'recipes_app/add_recept_form.html', context=context)