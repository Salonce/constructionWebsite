import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from .models import HousePlan, UserFavourite, UserSettings
from .forms import ContactForm, SnippetForm, UserCreatorForm, UserSettingsForm
from .decorators import authGoHome, onlyAuthPermitted, allowOnlySpecificRoles
from django.core import serializers
from django.contrib.auth.models import User


@onlyAuthPermitted
@allowOnlySpecificRoles(allowed_roles=['customer'])
def userSettings(request):

  if UserSettings.objects.filter(user_id=request.user.id).exists():
    user_settings_instance = UserSettings.objects.get(user_id=request.user.id)
    initial_values = {
      'address_one': user_settings_instance.address_one,
      'address_two': user_settings_instance.address_two,
      'contact_person_name': user_settings_instance.contact_person_name,
      'telephone_number': user_settings_instance.telephone_number
    }
    form = UserSettingsForm(initial=initial_values)
  else:
    form = UserSettingsForm()

  if request.method == "POST":
    form = UserSettingsForm(request.POST)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.user = request.user
      if UserSettings.objects.filter(user_id=request.user.id).exists():
        old_id = UserSettings.objects.get(user_id=request.user.id).id
        obj.id = old_id
      form.save()
      return redirect('home')
    else:
      return HttpResponse('didnt update')

  return render(request, 'userSettings.html', context={'form': form})


def home(request):
  if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    some_text = request.GET.get('someText')
    #print()
    #print(some_text)
    #print()
  return render(request, 'home.html', context={})

def loadInfo(request):
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    print("      ")
    print("dsadsa")
    print("      ")
    data = {'tree': 'tree', 'grass': 'grass', 'house': 'house'}
    return JsonResponse(data)
  else:
    return render(request, 'home.html', context={})


def housePlanBrowser(request):

  if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':
    print("i am inside ajax post request, success")
    print(request.body)
    state = None
    received_json = json.loads(request.body)
    house_plan_id = received_json['housePlanID']
    print("house_plan_id:", house_plan_id)
    picked_house_plan = HousePlan.objects.all().get(id=house_plan_id)
    result_record = UserFavourite.objects.all().filter(user=request.user, house_plan=picked_house_plan)
    if result_record:
      result_record.delete()
      state = "deleted"
      print("deleted object")
    else:
      new_record = UserFavourite(user=request.user, house_plan=picked_house_plan)
      new_record.save()
      state = "added"
      print("added object")
    print("result_record:", result_record)
    context={'state': state}
    return JsonResponse(context)


  #fetch table with userFavs for this user
  #get all house_IDs into a list
  #??for each ID, if it is in the list, add DJANGO IF in HTML template: if the ID of the given HOUSE
  #is in the list, add 'fav-selected' class

  if request.method == 'GET':
    userFavs = UserFavourite.objects.all().filter(user=request.user)
    fav_plans_ids = userFavs.values('house_plan')
    vals = []
    for i in fav_plans_ids:
      vals.append(i['house_plan'])
    #print(userFavs)
    print('fav_plans_ids: ', vals)

    order = None
    if "order" in request.GET:
      order = request.GET['order']
      if order == 'total-area':
        order = "total_area"
      house_plans = HousePlan.objects.all().order_by(order)
    else:
      house_plans = HousePlan.objects.all().order_by("name")
    return render(request, 'housePlanBrowser.html', context={'fav_plans_ids': vals, 'house_plans': house_plans, 'order': order})


def housePlan(request, id):
  housePlan = HousePlan.objects.get(id=id)
  return render(request, 'housePlan.html', context={'housePlan': housePlan})


def contact(request):
  if request.method == 'POST':
    form = SnippetForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      print(name)
      form.save()

  form = SnippetForm()
  return render(request, 'form.html', context={'form': form})


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

  order = None
  #rint(request.type)
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':

    print("i am inside ajax post request, success")
    print(request.body)

    state = None

    received_json = json.loads(request.body)
    house_plan_id = received_json['housePlanID']
    print("house_plan_id:", house_plan_id)
    picked_house_plan = HousePlan.objects.all().get(id=house_plan_id)

    result_record = UserFavourite.objects.all().filter(user=request.user, house_plan=picked_house_plan)
    if result_record:
      result_record.delete()
      state = "deleted"
      print("deleted object")
    else:
      new_record = UserFavourite(user=request.user, house_plan=picked_house_plan)
      new_record.save()
      state = "added"
      print("added object")

    print("result_record:", result_record)

    context={'state': state}
    return JsonResponse(context)

    # user_id = UserSettings.objects.get(user=request.user, house_plan= ).id
    #if in favourite user objects record houseplanid request.user.id exists then
      #remove the houseplan id
    #else:
      #add the houseplan id user id record
    #print(data)

    #houseID = request.POST
    #dataaa = serializers.deserialize(request.data)
    #print(request)
    #get house ID variable here


  """
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    print("dsadsa")
    if order == 'total-area':
      order = "total_area"
      user_favourites = UserFavourite.objects.filter(user=request.user).order_by("house_plan__" + order)
    else:
      user_favourites = UserFavourite.objects.filter(user=request.user).order_by("house_plan__name")

    data = serializers.serialize("json", user_favourites)
    print(data)
    return HttpResponse(data, content_type="application/json")
  """

  if "order" in request.GET:
    order = request.GET['order']
    if order == 'total-area':
      order = "total_area"
    user_favourites = UserFavourite.objects.filter(user=request.user).order_by("house_plan__" + order)
    #x = UserFavourite.objects.filter(user=request.user).prefetch_related('house_plan')
  else:
    user_favourites = UserFavourite.objects.filter(user=request.user).order_by("house_plan__name")

  template = loader.get_template('userFavourites.html')
  context = {
    'user_favourites': user_favourites,
    'order': order,
  }

  return HttpResponse(template.render(context, request))






