# vas/management/commands/generate_contacts.py

from django.core.management.base import BaseCommand
from vas.models import Contact
from faker import Faker

class Command(BaseCommand):
    help = 'Generate dummy contacts for testing'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of contacts to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        for _ in range(total):
            Contact.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address1=fake.street_address(),
                address2=fake.secondary_address(),
                city=fake.city(),
                county=fake.state(),
                postcode=fake.postcode(),
                country=fake.country()
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} contacts'))