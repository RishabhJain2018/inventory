from django.contrib import admin
from .models import Category
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
	list_display = ("name",)

admin.site.register(Category, categoryAdmin)
