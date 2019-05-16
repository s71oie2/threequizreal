from django.contrib import admin
from .models import Seed, State, Diary

@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state')
    list_display_links = ('id', 'state')

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'seed', 'harvest_at')
    list_display_links = ('id', 'user')

    def harvest_at(self, obj):
        if obj.harvest == None:
            pass
        else:
            return obj.harvest.strftime("%Y-%m-%d")

    harvest_at.short_description = '수확날짜'
