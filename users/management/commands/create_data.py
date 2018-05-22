from __future__ import absolute_import
from __future__ import print_function
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from todos.models import Todo
from users.models import User
from faker import Faker


class Command(BaseCommand):
    """
    Check Invite Expiration Command
    """

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def handle(self, **options):
        """
        Execute the command.

        """
        print(options)
        fake = Faker()
        for _ in range(70):
            email = fake.email()
            user = User(
                username=email,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                password=make_password('P@ssw0rd')
            )
            user.save()
            for _ in range(35):
                todo = Todo(name=fake.sentence(), user=user)
                todo.save()

