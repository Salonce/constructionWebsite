from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('inventoryBrowser/', views.inventoryBrowser, name='inventoryBrowser'),
  path('userInventory/', views.userInventory, name='userInventory'),
  path('housePlanBrowser/', views.housePlanBrowser, name='housePlanBrowser'),
  path('housePlanBrowser/<int:id>/', views.housePlan, name='housePlan'),
  path('contact/', views.contact, name='contact'),
  path('register/', views.register, name='register'),
  path('login/', views.loginPage, name='loginPage'),
  path('logout/', views.logoutPage, name='logoutPage')
  #path('housePlanBrowser/<int:id>/media/<int:id>', views.housePlan, name='housePlan'),
]

