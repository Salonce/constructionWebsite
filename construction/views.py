from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Inventory, HousePlan

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render({}, request))

def inventoryBrowser(request):
  myitems = Inventory.objects.all().values()

  #
  total_value = 0
  full_list = []

  for x in myitems:
    #full_list.append([x, x['amount']*x['price']])
    total_value = total_value + x['amount']*x['price']
  #

  template = loader.get_template('inventoryBrowser.html')
  context = {
     'myitems': myitems,
     'total_value': total_value,
     'full_list': full_list
  }
  return HttpResponse(template.render(context, request))


def houseBrowser(request):
  housePlans = HousePlan.objects.all().values()
  context = {
    'housePlans': housePlans
  }

  template = loader.get_template('housePlanBrowser.html')
  return HttpResponse(template.render(context, request))




