from django.contrib import admin
from .models import History

# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['User', 'temperature', 'from_unit', 'converted', 'to_unit', 'created_at']
    odering = ['User']

admin.site.register(History, HistoryAdmin)