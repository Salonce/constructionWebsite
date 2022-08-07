from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('construction/', include('construction.urls')),
    path('admin/', admin.site.urls),
]