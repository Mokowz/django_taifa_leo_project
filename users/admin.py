from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "age", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
