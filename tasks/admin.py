from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'completed')
    list_filter = ('priority', 'completed')
    search_fields = ('title',)
