from django.core.management.base import BaseCommand
from hw01_app.models import Order, User, Product

class Command(BaseCommand):
    help = "Вывод одного юзеров"

    def add_arguments(self, parser):
        parser.add_argument('pk_user', type=int, help='count_user')

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('pk_user')
        user = User.objects.filter(pk=user_id).first()
        self.stdout.write(f'{user.name} {user.pk}')
