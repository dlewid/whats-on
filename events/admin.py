from django.contrib import admin

# put our models here to import from models
from .models import Event

admin.site.register(Event)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'sports_category', 'date')
    list_filter = ('sports_category', 'date')
    search_fields = ('title', 'sports_category')