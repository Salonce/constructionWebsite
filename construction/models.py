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

class House(models.Model):
  name = models.CharField(max_length=255)
  localization = models.CharField(max_length=255)
  total_area = models.CharField(max_length=255)
  price = models.FloatField(max_length=255)
  rooms = models.IntegerField(max_length=255)
  floors = models.IntegerField(max_length=255)
  typeOfTransaction = models.CharField(max_length=255) #renting or purchase
  state = models.CharField(max_length=255) #(finished? to finish)
  additions = models.CharField(max_length=255) #balcony / garden / terrace
  parking_place = models.CharField(max_length=255) #balcony / garden / terrace
  heating = models.CharField(max_length=255) #gas / wood / coal
  description = models.CharField(max_length=1000)
