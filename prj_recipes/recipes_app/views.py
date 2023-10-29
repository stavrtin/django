from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Recipe, Category, Ingredients




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




