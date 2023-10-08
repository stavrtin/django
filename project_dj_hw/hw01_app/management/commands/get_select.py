from django.core.management.base import BaseCommand
from hw01_app.models import Order, User, Product

class Command(BaseCommand):
    help = "Вывод ВСЕХ юзеров, заказывавших введенный продукт"

    def add_arguments(self, parser):
        parser.add_argument('prod_name', type=str, help='count_user')

    def handle(self, *args, **kwargs):
        prod_find = kwargs.get('prod_name')
        prods = Product.objects.filter(prodname__in=[prod_find])
        for prod_ in prods:
            orders = Order.objects.filter(products__in=[prod_])
            for i in orders:
                self.stdout.write(f'{i.customer}')


