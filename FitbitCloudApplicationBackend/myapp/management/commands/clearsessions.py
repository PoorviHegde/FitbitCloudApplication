from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session

class Command(BaseCommand):
    help = 'Clear all sessions'

    def handle(self, *args, **options):
        Session.objects.all().delete()
        self.stdout.write('All sessions have been cleared.')