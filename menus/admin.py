from django.contrib import admin
from menus.models import MenuItem
from menus.serializers import MenuItemFormSerializer


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    form = MenuItemFormSerializer


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    form = MenuItemFormSerializer

admin.site.register(MenuItem, MenuItemAdmin)
