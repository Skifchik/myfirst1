from django.db import models


# Create your models here.
class Order(models.Model):
    user_id = models.IntegerField()
    order_info = models.CharField(max_length=200)
