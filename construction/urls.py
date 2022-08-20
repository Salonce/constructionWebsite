from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('userFavourites/', views.userFavourites, name='userFavourites'),
  path('userFavourites/<int:id>/', views.userFavourites, name='userFavourites'),
  path('housePlanBrowser/', views.housePlanBrowser, name='housePlanBrowser'),
  path('housePlanBrowser/<int:id>/', views.housePlan, name='housePlan'),
  path('contact/', views.contact, name='contact'),
  path('register/', views.register, name='register'),
  path('login/', views.loginPage, name='loginPage'),
  path('logout/', views.logoutPage, name='logoutPage')
  #path('housePlanBrowser/<int:id>/media/<int:id>', views.housePlan, name='housePlan'),
]

