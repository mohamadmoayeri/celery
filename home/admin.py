from django.contrib import admin

# Register your models here.

from .models import factorial_model

admin.site.register(factorial_model)
