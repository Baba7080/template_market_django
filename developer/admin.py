from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(template_post)
class template_postAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','category','is_pro']