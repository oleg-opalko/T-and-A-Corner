from decimal import Decimal

from django.core.management.base import BaseCommand

from shop.models import Brand, Category, Perfume


class Command(BaseCommand):
    help = 'Load demo perfumes matching the design mockup'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(
            slug='signature',
            defaults={'name': 'Signature Collection'},
        )
        brand, _ = Brand.objects.get_or_create(
            slug='ta-corner',
            defaults={'name': 'T&A Corner'},
        )

        demo_products = [
            ('noir-eclat', 'Noir Éclat'),
            ('ambre-minuit', 'Ambre Minuit'),
            ('velour-oud', 'Velour Oud'),
            ('lunar-shadow', 'Lunar Shadow'),
        ]

        for slug, name in demo_products:
            Perfume.objects.update_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'brand': brand,
                    'category': category,
                    'product_type': 'Extrait de Parfum',
                    'price': Decimal('180.00'),
                    'volume_ml': 50,
                    'is_available': True,
                    'is_featured': True,
                    'description': 'A signature fragrance from the T&A Corner collection.',
                },
            )

        self.stdout.write(self.style.SUCCESS('Demo products loaded.'))
