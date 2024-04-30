from django.core.management import BaseCommand

from mailing.models import Mailing


class Command(BaseCommand):
    """
    Команда для отправки рассылки
    """

    def handle(self, *args, **options):
        Mailing.objects.filter(status=2)
