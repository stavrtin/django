import random

from django.core.management.base import BaseCommand
from sem02_task1_app.models import Author, Article

class Command(BaseCommand):
    help = "Созданееи тестовых пользователей"
    def add_arguments(self, parser):
      parser.add_argument('count', type=int, help='count Author ID')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(
                firstname = f'Имя_{i}',
                lastname = f'Петров_{i}',
                email = f'Имя__{i}@mail.ru',
                biography = 'AWQEzzx zvxcv sd ',
                birthday = '2020-03-02',
                            )
            author.save()
            count_articl = random.randint(1,5)
            for j in range(1, count_articl):
                article = Article(
                    title = f'title_{j}',
                    description =f'{j}{j} sdfsd {j}{j} sdasd',
                    # create_at = '2023-03-02',
                    author_id = author,
                    category = 'adada asd as',
                    count_view = random.randint(1,1000),
                    publicated = random.choice([False, True])
                    )
                article.save()
        self.stdout.write(f'{author}')