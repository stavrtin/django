import random

from django.core.management.base import BaseCommand
from hw01_app.models import Order, User, Product

class Command(BaseCommand):
    help = "n заказов для всех юзеров со случай набором товаров"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        prods = Product.objects.all()
        for user_ in users:
            # order = Order(customer=user_, total=0)
            order = Order(customer=user_)
            total_ = 0
            for prod_ in prods:
                if random.randint(0, 1) == 1:  # выбираем рандомные товары
                    total_ += float(prod_.price) * float(prod_.amount)
                    order.total = total_
                    order.save()
                    order.products.add(prod_)

        self.stdout.write(f'Записан {order} ')       # self.stdout.write(f'User: {author}')


