from django.conf import settings
from django.db import models
from products.models import Product

# Create your models here.
class Favourite(models.Model):
    """ Favourites model """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"