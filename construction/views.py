from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Inventory

def index(request):
  myitems = Inventory.objects.all().values()

  #
  total_value = 0
  for x in myitems:
    total_value = total_value + x['amount']*x['price']
  #

  template = loader.get_template('index.html')
  context = {
    'myitems': myitems,
    'total_value': total_value
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  name = request.POST['name']
  price = request.POST['price']
  amount = request.POST['amount']
  item = Inventory(name=name, price=price, amount=amount)
  item.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  item = Inventory.objects.get(id=id)
  item.delete()
  return HttpResponseRedirect(reverse('index'))