from django.core.management.base import BaseCommand
from lection_02_app.models import User

class Command(BaseCommand):
    help = "Read all USER by age"

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **kwargs):
        # age = kwargs['age']
        age = kwargs.get('age')
        users = User.objects.filter(age__gt=age)
        self.stdout.write(f'{users}')
