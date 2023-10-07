from django.core.management.base import BaseCommand
from lection_02_app.models import User

class Command(BaseCommand):
    help = "Created USER"

    def handle(self, *args, **kwargs):
        user = User(
            name = 'Qasda',
            email = 'Qasda@sdfds',
            password = '333',
            age = 45,
            )
        user.save()
        self.stdout.write(f'User: {user}')

