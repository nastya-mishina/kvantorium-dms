import string
import random

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('password', type=str, help='Password')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        User.objects.create_superuser(username=username, password=password)
        self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
