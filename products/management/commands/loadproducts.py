import random
from random import randint
from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from products.models import Category, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        # Initialize Faker
        fake = Faker()

        # Predefined categories
        categories = ['Electronics', 'Clothing', 'Books', 'Toys', 'Food', 'Tools', 'Sport', 'Other']

        # Create categories
        for category in categories:
            Category.objects.get_or_create(name=category)

        # Create product names using Faker
        products = []
        for _ in range(10000):
            product_name = f"{fake.word()} {fake.word()}".title()  # Generate a two-word product name
            category = Category.objects.order_by("?").first()  # Randomly select a category
            price = randint(10, 100)

            products.append(category.products.create(name=product_name, price=price))

        # Predefined tags
        tags_names = ['New', 'Sale', 'Top', 'Best', 'Cheap', 'Expensive', 'Exclusive', 'Limited']

        # Create tags if they don't exist
        tags = [
            Tag.objects.get_or_create(name=tag_name)[0]
            for tag_name in tags_names
        ]

        # Assign random tags to products
        for product in products:
            random_tags = random.sample(tags, randint(1, 3))  # Assign 1 to 3 random tags to each product
            product.tags.add(*random_tags)
            product.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully created 1000 products with random tags."))
