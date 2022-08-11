from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Inventory, DefaultPrices

def index(request):
  myitems = DefaultPrices.objects.all().values()

  #
  total_value = 0
  full_list = []

  """
  for x in myitems:
    full_list.append([x, x['amount']*x['price']])
    total_value = total_value + x['amount']*x['price']
  """
  #

  template = loader.get_template('index.html')
  context = {
    'myitems': myitems,
  #  'total_value': total_value,
  #  'full_list': full_list
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

def update(request, id):
  item = DefaultPrices.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'item': item,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  price = request.POST['price']
  amount = request.POST['amount']
  item = Inventory.objects.get(id=id)
  item.price = price
  item.amount = amount
  item.save()
  return HttpResponseRedirect(reverse('index'))

def defaultvalues(request):
  items = DefaultPrices.objects.all().values()
  template = loader.get_template('defaultValues.html')
  context = {
    'items': items
  }
  return HttpResponse(template.render(context, request))

def adddefaultvaluepage(request):
  template = loader.get_template('addDefaultValue.html')
  return HttpResponse(template.render({}, request))

def adddefaultvalue(request):
  name = request.POST['name']
  price = request.POST['price']
  hundred = request.POST['hundred']
  hundredfifty = request.POST['hundredfifty']
  twohundred = request.POST['twohundred']
  item = DefaultPrices(name=name, price=price, hundred=hundred, hundredfifty=hundredfifty, twohundred=twohundred)
  item.save()
  return HttpResponseRedirect(reverse('defaultvalues'))

def updatedefaultvaluepage(request, id):
  template = loader.get_template('updateDefaultValue.html')
  return HttpResponse(template.render({}, request))

def updatedefaultvalue(request, id):
  name = request.POST['name']
  price = request.POST['price']
  hundred = request.POST['hundred']
  hundredfifty = request.POST['hundredfifty']
  twohundred = request.POST['twohundred']
  item = DefaultPrices(name=name, price=price, hundred=hundred, hundredfifty=hundredfifty, twohundred=twohundred)
  item.save()
  return HttpResponseRedirect(reverse('defaultvalues'))


def houseAdminPage(request):
  template = loader.get_template("houseAdminPage.html")
  return HttpResponse(template.render({}, request))

def houseAdminAddHouse(request):
  return HttpResponseRedirect(reverse('index'))





