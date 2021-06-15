from django.contrib import admin

from user.models import CustomUser


class CustomAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']


admin.site.register(CustomUser, CustomAdmin)
