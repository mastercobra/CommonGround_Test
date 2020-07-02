from django.db import models


class Product(models.Model):

    id = models.CharField(primary_key=True, max_length=250)
    name = models.CharField(max_length=250, null=False)
    value = models.FloatField(null=False)
    discount_value = models.FloatField(null=True)
    stock = models.IntegerField(null=False)
