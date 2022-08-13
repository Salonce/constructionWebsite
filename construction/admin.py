from django.contrib import admin
from .models import Inventory
from .models import HousePlan


# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'price']
    pass
admin.site.register(Inventory, InventoryAdmin)


class HousePlanAdmin(admin.ModelAdmin):
    pass
admin.site.register(HousePlan, HousePlanAdmin)