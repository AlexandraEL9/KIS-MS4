from django.db import models

# Create your models here.

# category model


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

# product size model


class ProductSize(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    product = models.ForeignKey('Product', related_name='sizes', on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.get_size_display()} - ${self.price}"
# product model

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

# get_-price_range method to return range of prices available for product

    def get_price_range(self):
        sizes = self.sizes.all()
        if sizes.exists():
            prices = [size.price for size in sizes]
            return f"${min(prices):.2f} - ${max(prices):.2f}"
        return "Price unavailable"
