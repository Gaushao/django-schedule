from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start', 'end', 'allDay')

# Register your models here.

admin.site.register(Schedule, ScheduleAdmin)