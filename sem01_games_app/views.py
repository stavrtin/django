from django.http import HttpResponse
from django.shortcuts import render
import random
import logging
from sem02_task1_app.models import Drop
from sem02_task1_app.models import Author
from sem02_task1_app.models import Article
from sem02_task1_app.models import Post
from django.shortcuts import render


# Create your views here.


logger = logging.getLogger(__name__)

def game1(request):
    res_list = ['орел','решка']
    res = random.choice(res_list)
    drop_step = Drop(drop_result=res)
    drop_step.save()
    logger.info(f'Сработала игра "орел-решка" - {drop_step}')

    return HttpResponse(f"Hello, game1! Выпало значение {drop_step}")

def game2(request):
    # res_list = ['орел','решка']
    res = random.randint(1,6)
    logger.info(f'Сработала игра 2 "кости", выпало {res}')
    return HttpResponse(f"Hello, game2! Выпало значение {res}")

def game3(request, count_drop: int):
    game_list = ['ор', 'реш']
    res = []
    for i_ in range(count_drop):
        res.append(random.choice(game_list))
    exit_cont = {
        'result_drops': res
                }
    return render(request, 'sem01_games_app/start.html', context=exit_cont)

def select_all_n(request, n: int):
    # drops = Drop()
    drops_all = Drop.sum_drops(n)
    # return HttpResponse(f"Было {len(drops_all)} попыток")
    return HttpResponse(drops_all)

def view_start(request, n: str):
    name = n
    exit_cont = {
        'name': name,
        'prosto_text': 'ssss-----ss'
            }
    return render(request, 'sem01_games_app/start.html', context=exit_cont)

def view_author_art(request, author_id: int):

    author = Author.objects.get(pk=author_id)
    articls = Article.objects.filter(author_id=author_id)
    # print(author)
    exit_context = {
        'author': author.firstname,
        'articls': articls,
                }
    return render(request, 'sem01_games_app/author_articl.html', context=exit_context)

def articl_full(request, articl_id):
    articl = Article.objects.get(id=articl_id)
    comments = Post.objects.filter(articl_id=articl_id).order_by('-edit_at')
    articl.count_view += 1
    articl.save()
    context = {
        'articl':articl,
        'comments':comments,
    }

    return render(request, 'sem01_games_app/articl_full.html', context=context)