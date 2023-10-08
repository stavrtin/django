from django.core.management.base import BaseCommand
from hw01_app.models import Order, User, Product

class Command(BaseCommand):
    help = "Вывод всех юзеров"

    def handle(self, *args, **kwargs):
        prods = Product.objects.all()
        for i in prods:
            self.stdout.write(f'prods: {i}')


