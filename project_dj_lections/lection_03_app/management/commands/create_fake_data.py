import random

from django.core.management.base import BaseCommand
from lection_03_app.models import Author, Post


LOREM = ("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus ad asperiores at "
         "beatae consectetur deleniti dignissimos doloribus eos facere fugiat harum id labore maxime "
         "molestias mollitia nisi nostrum officiis optio perspiciatis, quas quasi quibusdam quisquam "
         "sapiente sequi veritatis. Amet animi dicta doloribus eveniet nobis optio, quas ratione soluta "
         "tempore? Aliquam aliquid consequatur, dolores laudantium magni modi neque obcaecati, odit, "
         "optio perferendis praesentium quidem quos repellat repudiandae tempore voluptatem voluptatum! "
         "Aliquam atque illum magnam maxime nisi odit possimus reiciendis. Beatae blanditiis consectetur "
         "luptas. Aliquid architecto eligendi optio?")

class Command(BaseCommand):
    help = "Created USER"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Users count ID')


    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}',
                            email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(random.choices(text, k=64)),
                    author=author
                            )
                post.save()

