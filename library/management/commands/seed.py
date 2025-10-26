from django.core.management.base import BaseCommand
from django.core.management import call_command



class Command(BaseCommand):
    help = "Initial data seed (fixtures) for the aplication Library."

    def handle(self, *args, **options):
        try:
            call_command("loaddata", "library/fixtures/initial_data.json")
            self.stdout.write(self.style.SUCCESS("Successfully data initial seed for aplication Library."))
        except Exception as e:
            self.stdout.write(self.style.WARNING("Failed data initial seed for aplication Library. -> {e}", e))