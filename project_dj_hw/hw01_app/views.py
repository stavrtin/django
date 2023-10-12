from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render
import random
import logging
from hw01_app.models import User
from hw01_app.models import Product
from hw01_app.models import Order

# Create your views here.


logger = logging.getLogger(__name__)


def main_index(request):
    res_list = ['орел', 'решка']
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
    res_list = ['орел', 'решка']
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


def users_orders(request, user_id):
    prods = {}
    user = User.objects.get(id=user_id)
    orders = Order.objects.filter(customer=user_id)
    for order_ in orders:

        prods[order_.id] = str(order_.products.all()).replace('<QuerySet [<', '').replace('>]>', '').split('>, <')
    context = {
        'user':user,
        'orders':orders,
        'prods':prods,
            }

    return render(request, 'hw01_app/user_ords.html', context=context)


def users_prods(request, user_id, period: int):
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=period)
    user = User.objects.get(pk=user_id)
    orders = Order.objects.filter(customer=user, create_order_at__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    context = {
        'user':user,
        'product_set':product_set,
        'period':period,
            }


    return render(request, 'hw01_app/user_prods.html', context=context)