from django.db import models

# Create your models here.
class Order(models.Model):
    order_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.order_name
