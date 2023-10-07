import random

from django.core.management.base import BaseCommand
from lection_02_app.models import User, Author, Post

class Command(BaseCommand):
    help = "Created USER"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Users count ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author  = Author(
                name = f'Имя_{i}',
                email = f'Имя_{i}@mail.ru'  )
            author.save()
            post_count = random.randint(1,5)
            for j in range(1, post_count + 1):
                post = Post(
                    title = f'title_{j}',
                    content = f'text from {author.name} # {j} sdf ert ert ert',
                    author = author)
                post.save()
        # self.stdout.write(f'User: {author}')

