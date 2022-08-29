from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField

class HousePlan(models.Model):
  ADDITIONSCHOICES = [("balcony", "balcony"), ("terrace", "terrace"), ("garden", "garden"), ("none", "none")]
  GARAGECHOICES = [("garage", "garage"), ("carport", "carport"), ("none", "none")]
  name = models.CharField(max_length=255)
  price = models.FloatField(max_length=255)
  total_area = models.FloatField(default=100.0)
  rooms = models.IntegerField()
  floors = models.IntegerField()
  additions = models.CharField(max_length=255, choices=ADDITIONSCHOICES, default="none")
  parking_place = models.CharField(max_length=255, choices=GARAGECHOICES, default="none")
  description = models.CharField(max_length=1000)
  picture = models.ImageField(null=True, blank=True, upload_to='', default='default.jpg')
  def __str__(self):
    return "%s" % (self.name)


class UserFavourite(models.Model):
  class Meta:
    unique_together = (('user', 'house_plan'),)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  house_plan = models.ForeignKey(HousePlan, on_delete=models.CASCADE, related_name='favourite')


class Snippet(models.Model):
  name = models.CharField(max_length=100)
  body = models.TextField()
  def __str__(self):
    return "%s" % (self.name)


class UserSettings(models.Model):
  address_one = models.CharField(max_length=255)
  address_two = models.CharField(max_length=255)
  contact_person_name = models.CharField(max_length=255)
  telephone_number = models.CharField(max_length=255)
  user = models.OneToOneField(User, on_delete=models.CASCADE)



#localization = models.CharField(max_length=255)
#typeOfTransaction = models.CharField(max_length=255) #renting or purchase
#state = models.CharField(max_length=255) #(finished? to finish)
#heating = models.CharField(max_length=255) #gas / wood / coal