from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='index'),
  path('inventoryBrowser/', views.inventoryBrowser, name='inventoryBrowser'),
  path('housePlanBrowser/', views.housePlanBrowser, name='housePlanBrowser'),
  path('housePlanBrowser/<int:id>/', views.housePlan, name='housePlan'),
  path('contact/', views.contact, name='contact'),
  path('register/', views.register, name='register'),
  #path('housePlanBrowser/<int:id>/media/<int:id>', views.housePlan, name='housePlan'),
]

