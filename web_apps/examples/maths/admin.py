from django.contrib import admin
from .models import Math
# Register your models here.


class AdminMath(admin.ModelAdmin):
    list_display = ['operacja','a','b', 'wynik', 'created']
    list_filter = ['operacja']
    search_fields = ['wynik']

admin.site.register(Math, AdminMath)
