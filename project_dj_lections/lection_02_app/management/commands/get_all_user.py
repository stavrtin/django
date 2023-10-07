from django.core.management.base import BaseCommand
from lection_02_app.models import User

class Command(BaseCommand):
    help = "Read all USER"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for i in users:
            self.stdout.write(f'User: {i}')

