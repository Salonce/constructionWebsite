from django.contrib import admin
from .models import Inventory
from .models import HousePlan


# Register your models here.
@admin.register(Inventory)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(HousePlan)
class PersonAdmin(admin.ModelAdmin):
    pass
