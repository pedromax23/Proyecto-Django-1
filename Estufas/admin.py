from django.contrib import admin
from .models import Estufa

# Register your models here.
class Estufas(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=("titulo",)

admin.site.register(Estufa, Estufas)