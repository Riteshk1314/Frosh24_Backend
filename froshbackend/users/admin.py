from django.contrib import admin
from .models import User
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('registration_id', 'email', 'name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('registration_id', 'email', 'password')}),
        ('Personal info', {'fields': ('name', 'image', 'secure_id', 'events', 'hood_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('registration_id', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'registration_id', 'name')
    ordering = ('registration_id',)

admin.site.register(User, CustomUserAdmin)