from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from .models import HousePlan, UserItem, UserFavourite
from .forms import ContactForm, SnippetForm, UserCreatorForm
from .decorators import authGoHome, onlyAuthPermitted, allowOnlySpecificRoles
from django.contrib.auth.models import User


def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render({}, request))



def housePlanBrowser(request):
  house_plans = HousePlan.objects.all().values()

  order = None
  if "order" in request.GET:
    order = request.GET['order']
    if order == 'total-area':
      order = "total_area"
    house_plans = HousePlan.objects.all().order_by(order)
  else:
    house_plans = HousePlan.objects.all().order_by("name")

  context = {
    'house_plans': house_plans,
    'order': order,
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


@authGoHome
def register(request):
  form = UserCreatorForm()

  if request.method == 'POST':
    form = UserCreatorForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      group = Group.objects.get(name='customer')
      user.groups.add(group)

      return redirect('loginPage')

    else:
      return render(request, 'register.html', context={'form': form})


  template = loader.get_template('register.html')
  context = {
    'form': form
  }
  return HttpResponse(template.render(context, request))


@authGoHome
def loginPage(request):
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('home')

    template = loader.get_template('login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def logoutPage(request):
  logout(request)
  return redirect('loginPage')


@onlyAuthPermitted
@allowOnlySpecificRoles(allowed_roles=['customer'])
def userFavourites(request):

  order =  None
  if "order" in request.GET:
    order = request.GET['order']
    if order == 'total-area':
      order = "total_area"
    user_favourites = UserFavourite.objects.filter(user=request.user).all().order_by("house_plan__" + order)
  else:
    user_favourites = UserFavourite.objects.filter(user=request.user).order_by("house_plan__name")

  template = loader.get_template('userFavourites.html')
  context = {
    'user_favourites': user_favourites,
    'order': order,
  }

  return HttpResponse(template.render(context, request))

