# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from lection_03_app.models import Author, Post


# Create your views here.

def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def df_year(request, year):
    text = "asdasdad"
    return HttpResponse(f"Posts from {year} <br> {text=}")

class MonthPost(View):
    def get(self, request, year, month):
        text = "asdasdad"
        return HttpResponse(f"Posts from {year}-{month} <br> {text=}")

def my_view(request, name_adres):
    name_iz_adr = name_adres
    context = {"name": name_iz_adr}
    return render(request, "lection_03_app/index3.html", context)


class TemplIf(TemplateView):
    template_name = "lection_03_app/temp_if.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = kwargs.get('post')
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
    'каждый': 'красный',
    'охотник': 'оранжевый',
    'желает': 'жёлтый',
    'знать': 'зелёный',
    'где': 'голубой',
    'сидит': 'синий',
    'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'lection_03_app/temp_for.html', context)

def index(request):
    # context = {'qqq': 123}
    return render(request, "lection_03_app/index.html")


def about(request):
    return render(request, "lection_03_app/about.html")

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts =  Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'lection_03_app/author_posts.html', {'author':  author, 'posts': posts})

def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'lection_03_app/post_full.html', {'post':   post})