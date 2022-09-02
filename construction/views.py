import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import HousePlan, UserFavourite, UserSettings
from .forms import SnippetForm, UserCreatorForm, UserSettingsForm
from .decorators import authGoHome, onlyAuthPermitted, allowOnlySpecificRoles




def home(request):
  return render(request, 'home.html', context={})


@onlyAuthPermitted
@allowOnlySpecificRoles(allowed_roles=['customer'])
def userSettings(request):
  #print(request.path)
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
    print(request.body)
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

  ### (POST)
  if request.method == 'POST':
    form = UserCreatorForm(request.POST)
    if form.is_valid():
      user = form.save()
      group = Group.objects.get(name='customer')
      user.groups.add(group)
      return redirect('loginPage')
    else:
      return render(request, 'register.html', context={'form': form})

  ### (GET)
  return render(request, 'register.html', context={'form': form})


@authGoHome
def loginPage(request):
    ### (POST)
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('home')

    ### (GET)
    return render(request, 'login.html', context={})


def logoutPage(request):
  logout(request)
  return redirect('loginPage')


def housePlanBrowser(request):
  #### (AJAX) add/delete a favourite by clicking on fav button
  if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    received_json = json.loads(request.body)
    house_plan_id = received_json['housePlanID']
    picked_house_plan = HousePlan.objects.all().get(id=house_plan_id)
    result_record = UserFavourite.objects.all().filter(user=request.user, house_plan=picked_house_plan)
    state = None
    if result_record:
      result_record.delete()
      state = "deleted"
    else:
      new_record = UserFavourite(user=request.user, house_plan=picked_house_plan)
      new_record.save()
      state = "added"
    context={'state': state}
    return JsonResponse(context)

  #### (GET) save IDs of user's favourites in a list
  if request.method == 'GET':
    userFavs = UserFavourite.objects.all().filter(user=request.user)
    favourites = []
    favourites_ids = userFavs.values('house_plan')
    for i in favourites_ids:
      favourites.append(i['house_plan'])

    #### SET SORTING
    sort = "name"
    if "sort" in request.GET:
      sorty = request.GET['sort']
      if (sorty == 'name' or sorty == 'total_area' or sorty == 'price' or sorty == 'rooms'):
        sort = request.GET['sort']
    house_plans = HousePlan.objects.all().order_by(sort)
    return render(request, 'housePlanBrowser.html', context={'house_plans': house_plans, 'favourites': favourites, 'sort': sort})


@onlyAuthPermitted
@allowOnlySpecificRoles(allowed_roles=['customer'])
def userFavourites(request):

  #### (AJAX) add/delete a favourite by clicking on fav button
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':
    state = None
    received_json = json.loads(request.body)
    house_plan_id = received_json['housePlanID']
    picked_house_plan = HousePlan.objects.all().get(id=house_plan_id)
    result_record = UserFavourite.objects.all().filter(user=request.user, house_plan=picked_house_plan)
    if result_record:
      result_record.delete()
      state = "deleted"
    else:
      new_record = UserFavourite(user=request.user, house_plan=picked_house_plan)
      new_record.save()
      state = "added"
    context={'state': state}
    return JsonResponse(context)

  #### (GET) SET SORTING
  sort = "name"
  if "sort" in request.GET:
    sorty = request.GET['sort']
    if (sorty == 'name' or sorty == 'total_area' or sorty == 'price' or sorty == 'rooms'):
      sort = request.GET['sort']
  user_favourites = UserFavourite.objects.filter(user=request.user).order_by("house_plan__" + sort)
  return render(request, 'userFavourites.html', context={'user_favourites': user_favourites, 'sort': sort})






