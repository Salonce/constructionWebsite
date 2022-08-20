from django.contrib import admin
from .models import HousePlan, Snippet, UserItem, UserFavourite

# Register your models here.
class HousePlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_area', 'rooms']
    pass
admin.site.register(HousePlan, HousePlanAdmin)


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['name', 'body']
    pass
admin.site.register(Snippet, SnippetAdmin)


class UserItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    pass
admin.site.register(UserItem, UserItemAdmin)


class UserFavouriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'house_plan']
    pass
admin.site.register(UserFavourite, UserFavouriteAdmin)