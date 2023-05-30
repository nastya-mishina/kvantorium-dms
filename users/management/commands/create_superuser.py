import string
import random

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.filter(username='admin')[0]:
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' already created"))
        else:
            User.objects.create_superuser(username='admin', password='admin')
