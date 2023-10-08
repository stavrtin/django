from django.core.management.base import BaseCommand
from hw01_app.models import User

class Command(BaseCommand):
    help = "Created USER"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Users count ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(
                name=f'User_{i}',
                email=f'User_{i}@mail.ru',
                phone=f'{i}{i}{i}-{i}{i}-{i}{i}',
                adres=f'Улица .. дом {i}',
            )
            user.save()
        self.stdout.write(f'Записано {count} юзеров')       # self.stdout.write(f'User: {author}')

