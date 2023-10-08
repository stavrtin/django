from django.core.management.base import BaseCommand
from hw01_app.models import Order, User, Product

class Command(BaseCommand):
    help = "Вывод всех юзеров"


    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for i in orders:
            self.stdout.write(f'orders: {i} {i.total}')


