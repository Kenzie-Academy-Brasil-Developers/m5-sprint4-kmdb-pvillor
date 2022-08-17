from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    readonly_fields = ('date_joined', 'last_login', 'updated_at')

    fieldsets = (
        ('Credentials', {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('bio', 'birthdate')}),
        ('Permission', {'fields': ('is_superuser', 'is_active', 'is_staff', 'is_critic')}),
        ('Important Dates', {'fields': ('date_joined', 'last_login', 'updated_at')})
    )

    list_display = ('username', 'is_critic')

admin.site.register(User, CustomUserAdmin)