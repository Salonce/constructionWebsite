from django.db import models

class Inventory(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField(max_length=255)