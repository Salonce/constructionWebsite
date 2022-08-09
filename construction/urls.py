from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  path('defaultvalues/', views.defaultvalues, name='defaultvalues'),
  path('defaultvalues/adddefaultvaluepage/', views.adddefaultvaluepage, name='adddefaultvaluepage'),
  path('defaultvalues/adddefaultvaluepage/adddefaultvalue/', views.adddefaultvalue, name='adddefaultvalue'),
  path('defaultvalues/updatedefaultvalue/<int:id>', views.updatedefaultvalue, name='updatedefaultvalue'),
]