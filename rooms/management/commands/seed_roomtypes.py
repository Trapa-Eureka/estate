from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates Room Types"

    """ 
    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
    """

    def handle(self, *args, **options):
        room_type = [
            "Hotel room",
            "Shared room",
            "Private room",
            "Entire room",
        ]
        for r in room_type:
            RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(room_type)} roomtypes created!"))