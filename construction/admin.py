from django.contrib import admin
from .models import Inventory, HousePlan, Snippet

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'price']
    pass
admin.site.register(Inventory, InventoryAdmin)


class HousePlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_area', 'rooms']
    pass
admin.site.register(HousePlan, HousePlanAdmin)


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['name', 'body']
    pass
admin.site.register(Snippet, SnippetAdmin)


