from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  path('constructionBrowser/', views.constructionBrowser, name='constructionBrowser'),
  path('adminPage/constructionAdminPage/', views.constructionAdminPage, name='constructionAdminPage'),
  path('adminPage/constructionAdminPage/addConstructionItemPage/', views.adddefaultvaluepage, name='adddefaultvaluepage'),
  path('adminPage/constructionAdminPage/adddefaultvaluepage/adddefaultvalue/', views.adddefaultvalue, name='adddefaultvalue'),
  path('adminPage/constructionAdminPage/updatedefaultvalue/<int:id>', views.updatedefaultvalue, name='updatedefaultvalue'),
  path('adminPage/', views.adminPage, name='adminPage'),
  path('houseBrowser/', views.houseBrowser, name='houseBrowser'),
  path('houseAdminPage/', views.houseAdminPage, name='houseAdminPage'),
  path('houseAdminAddHouse/', views.houseAdminAddHouse, name='houseAdminAddHouse'),
]