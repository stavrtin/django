from django.core.management.base import BaseCommand
from hw01_app.models import Order, User, Product

class Command(BaseCommand):
    help = "Вывод всех юзеров"


    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for i in users:
            self.stdout.write(f'User: {i}')


