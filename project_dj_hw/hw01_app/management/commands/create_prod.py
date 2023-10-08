from django.core.management.base import BaseCommand
from hw01_app.models import Product

class Command(BaseCommand):
    help = "Created USER"

    def add_arguments(self, parser):
        parser.add_argument('prodname', type=str, help='Prod')
        parser.add_argument('description', type=str, help='Prod count ID')
        parser.add_argument('price', type=float, help='Prod count ID')
        parser.add_argument('amount', type=float, help='Prod count ID')

    def handle(self, *args, **kwargs):
        prodname = kwargs.get('prodname')
        description = kwargs.get('description')
        price = kwargs.get('price')
        amount = kwargs.get('amount')
        prod = Product(
            prodname=prodname,
            description=description,
            price=price,
            amount=amount
        )
        prod.save()
        self.stdout.write(f'Записан {prod} ')

