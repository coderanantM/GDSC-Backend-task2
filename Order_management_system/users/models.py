from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, default = None)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.customer.username}-Profile'