from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUsersAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {"fields": ("username", "password", "name", "email", "is_host")},
        ),
    )
    list_display = ("username", "email", "is_host")
