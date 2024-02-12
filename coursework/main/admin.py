from django.contrib import admin
from .models import *


# Register your models here.
class EquationAdmin(admin.ModelAdmin):
    search_fields = ("n",)


admin.site.register(Equation, EquationAdmin)
