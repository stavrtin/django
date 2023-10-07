from django.core.management.base import BaseCommand
from lection_02_app.models import User


class Command(BaseCommand):
    help = "Update USER"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User age')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}')
