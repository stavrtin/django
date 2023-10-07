from django.http import HttpResponse
from django.shortcuts import render
import random
import logging
# Create your views here.


logger = logging.getLogger(__name__)

def main_index(request):
    res_list = ['орел','решка']
    # res = random.choice(res_list)
    res = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Что-то про меня</title>
</head>
<body>
<p>Тут я</p>
<p>И Что-то про меня</p>
</body>
</html>'''
    logger.info(f'Сработал переход на главную')
    return HttpResponse({res})

def about(request):
    res_list = ['орел','решка']
    # res = random.choice(res_list)
    res = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Что-то снова про меня</title>
</head>
<body>
<p>А тут что-то другое</p>
<p>И тоже что-то про меня</p>
</body>
</html>'''
    logger.info(f'Сработал переход на "обо мне" ')
    return HttpResponse({res})

