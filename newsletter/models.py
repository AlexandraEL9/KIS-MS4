from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    date_subscribed = models.DateTimeField('Date created', default=timezone.now)
    
    def __str__(self):
        return self.email