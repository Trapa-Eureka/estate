from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates House Rules"

    """ 
    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
    """

    def handle(self, *args, **options):
        house_rules = [
            "No smoking",
            "No parties or events",
            "No pets/Pets allowed",
            "No unregistered guests",
            "No food or drink in bedrooms",
            "No loud noise after 9 PM",
            "Self check-in with lockbox",
            "Long-term stays (28 days or more) are allowed",
        ]
        for h in house_rules:
            HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} houserules created!"))