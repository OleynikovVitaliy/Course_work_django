import typing

from django.core.management.base import BaseCommand

from mailing.scheduler import start_scheduler


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args: typing.Any, **options: typing.Any) -> typing.Any:
        start_scheduler()
