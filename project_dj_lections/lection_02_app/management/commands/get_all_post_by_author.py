from django.core.management.base import BaseCommand
from lection_02_app.models import User, Post, Author

class Command(BaseCommand):
    help = "Read post by # autor"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID authorth')

    def handle(self, *args, **kwargs):
        # author_id = kwargs.get('pk')
        # author = Author.objects.filter(pk=author_id).first()
        # if author is not None:
        #     posts = Post.objects.filter(author=author)
        #     intro = f'All posts of {author.name}\n'
        #     text = '\n'.join(post.content for post in posts)
        #     self.stdout.write(f'{intro}{text}')
        author_id = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=author_id)
        intro = f'All posts of {author_id}\n'
        text = '\n'.join(post.get_first_text() for post in posts)
        self.stdout.write(f'{intro}{text}')