from django.db import models

class Inventory(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField(max_length=255)
  amount = models.IntegerField(default=0)

class DefaultPrices(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField(max_length=255)
  hundred = models.FloatField(max_length=255, default=0)
  hundredfifty = models.FloatField(max_length=255, default=0)
  twohundred = models.FloatField(max_length=255, default=0)