from django.http import HttpResponse
from django.shortcuts import render
import random
import logging
from sem02_task1_app.models import Drop


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

def game3(request):
    res = random.randint(1,100)
    logger.info(f'Сработала игра 2 "1213123", выпало {res}')
    return HttpResponse(f"game3! Выпало значение {res}")

def select_all_n(request, n: int):
    # drops = Drop()
    drops_all = Drop.sum_drops(n)
    # return HttpResponse(f"Было {len(drops_all)} попыток")
    return HttpResponse(drops_all)