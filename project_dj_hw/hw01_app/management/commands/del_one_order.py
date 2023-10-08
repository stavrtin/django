from django.core.management.base import BaseCommand
from hw01_app.models import Order, User, Product

class Command(BaseCommand):
    help = "Удалить заказ"

    def add_arguments(self, parser):
        parser.add_argument('pk_order', type=int, help='count_user')

    def handle(self, *args, **kwargs):
        order_id = kwargs.get('pk_order')
        order = Order.objects.filter(pk=order_id).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'Заказ {order} удален')
