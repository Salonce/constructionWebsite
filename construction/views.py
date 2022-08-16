from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Inventory, HousePlan
from .forms import ContactForm, SnippetForm, UserCreatorForm



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


def housePlanBrowser(request):
  housePlans = HousePlan.objects.all().values()
  context = {
    'housePlans': housePlans
  }

  template = loader.get_template('housePlanBrowser.html')
  return HttpResponse(template.render(context, request))

def housePlan(request, id):
  housePlan = HousePlan.objects.get(id=id)
  context = {
    'housePlan': housePlan
  }
  template = loader.get_template('housePlan.html')
  return HttpResponse(template.render(context, request))

def contact(request):
  if request.method == 'POST':
    form = SnippetForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']

      print(name)
      form.save()

  form = SnippetForm()
  template = loader.get_template('form.html')
  context = {
    'form': form
  }
  return HttpResponse(template.render(context, request))


def register(request):
  form = UserCreatorForm()

  if request.method == 'POST':
    form = UserCreatorForm(request.POST)
    if form.is_valid():
      #name = form.cleaned_data['name']
      form.save()
    else:
      return render(request, 'register.html', context={'form': form})


  template = loader.get_template('register.html')
  context = {
    'form': form
  }
  return HttpResponse(template.render(context, request))
