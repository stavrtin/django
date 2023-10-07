from django.http import HttpResponse
from django.shortcuts import render
import random
import logging
# Create your views here.


logger = logging.getLogger(__name__)

def game1(request):
    res_list = ['орел','решка']
    res = random.choice(res_list)
    logger.info(f'Сработала игра 1 орел-решка, выпало {res}')
    return HttpResponse(f"Hello, game1! Выпало значение {res}")

def game2(request):
    # res_list = ['орел','решка']
    res = random.randint(1,6)
    logger.info(f'Сработала игра 2 "кости", выпало {res}')
    return HttpResponse(f"Hello, game2! Выпало значение {res}")

def game3(request):
    res = random.randint(1,100)
    logger.info(f'Сработала игра 2 "1213123", выпало {res}')
    return HttpResponse(f"game3! Выпало значение {res}")

