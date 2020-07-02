from django.db import models
import json


class Product(models.Model):

    id = models.CharField(primary_key=True, max_length=250)
    name = models.CharField(max_length=250, null=False)
    value = models.FloatField(null=False)
    discount_value = models.FloatField(null=True)
    stock = models.IntegerField(null=False)

    def __str__(self):
        return json.dumps({'id': self.id,
                'name': self.name,
                'value': self.value,
                'discount_value': self.discount_value,
                'stock': self.stock})