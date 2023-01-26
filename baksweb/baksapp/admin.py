from django.contrib import admin
from .models import HezbeOne, TaxiOne, Automobile, DerekOne, Moter

datas = HezbeOne, TaxiOne, Automobile, DerekOne, Moter

class Datas(admin.ModelAdmin):
    list_display = ('name', 'result')

admin.site.register(datas, Datas)