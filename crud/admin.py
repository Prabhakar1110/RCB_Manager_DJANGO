from django.contrib import admin
from .models import Food, Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "role"]

class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Player, PlayerAdmin)
admin.site.register(Food, FoodAdmin)