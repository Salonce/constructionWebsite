from django.db import models

class Inventory(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField(max_length=255)
  amount = models.IntegerField(default=0)

  #def __str__(self):
  #  return "%s (price: %s, amount: %s)" % (self.name, self.price, self.amount)

class HousePlan(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField(max_length=255)
  total_area = models.FloatField(default=100.0)
  rooms = models.IntegerField()
  floors = models.IntegerField()
  additions = models.CharField(max_length=255) #balcony / garden / terrace
  parking_place = models.CharField(max_length=255) #balcony / garden / terrace
  description = models.CharField(max_length=1000)
  picture = models.ImageField(null=True, blank=True, upload_to='', default='default.jpg')
  #def __str__(self):
  #  return "%s" % (self.name)

#localization = models.CharField(max_length=255)
#typeOfTransaction = models.CharField(max_length=255) #renting or purchase
#state = models.CharField(max_length=255) #(finished? to finish)
#heating = models.CharField(max_length=255) #gas / wood / coal