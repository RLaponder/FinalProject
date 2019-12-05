from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('straat', 'huisnummer', 'postcode', 'woonplaats')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
