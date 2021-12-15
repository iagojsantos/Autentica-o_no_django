from django.contrib import admin

# Register your models here.

from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone')
    search_fields = ('user__email',)
