from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='index'),
  path('inventoryBrowser/', views.inventoryBrowser, name='inventoryBrowser'),
  path('houseBrowser/', views.houseBrowser, name='houseBrowser'),
]