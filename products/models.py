from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('rods', 'Rods'),
        ('reels', 'Reels'),
        ('lines', 'Lines'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self):
        return self.name