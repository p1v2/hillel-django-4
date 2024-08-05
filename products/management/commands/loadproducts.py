import random
from random import randint

from django.core.management import BaseCommand
from django.db import transaction

from products.models import Category, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        categories = ['Electronics', 'Clothing', 'Books', 'Toys', 'Food', 'Tools', 'Sport', 'Other']

        for category in categories:
            Category.objects.create(name=category)

        products_names = [
            "Coca-Cola 0.5L", "Fanta 0.5L", "Sprite 0.5L", "Pepsi 0.5L", "Mirinda 0.5L", "Hoegaarden 0.5L", "Leffe 0.5L",
            "Chimay 0.5L", "Duvel 0.5L", "Westmalle 0.5L", "Stella Artois 0.5L", "Jupiler 0.5L", "Heineken 0.5L",
            "Grolsch 0.5L", "Amstel 0.5L", "Bavaria 0.5L", "Budweiser 0.5L", "Corona 0.5L", "Guinness 0.5L",
        ]

        products = []
        for product_name in products_names:
            category = Category.objects.get(name='Food')
            price = randint(10, 100)

            products.append(category.products.create(name=product_name, price=price))

        tags_names = ['New', 'Sale', 'Top', 'Best', 'Cheap', 'Expensive', 'Exclusive', 'Limited']

        tags = [
            Tag(name=tag_name)
            for tag_name in tags_names
        ]

        Tag.objects.bulk_create(tags)

        for product in products:
            # Select random tags
            random_tag = random.choice(tags)

            product.tags.add(random_tag)
            product.save()
