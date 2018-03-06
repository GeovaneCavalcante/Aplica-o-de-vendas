from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .form import UserCreationForm, UserChangeForm


from .models import User


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'phone', 'date_joined')
    list_filter = ('email', 'name')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password', 'phone', 'photo')}),
        ('Informações de usuário', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2')}
        ),
    )

    search_fields = ('email', 'name')
    ordering = ('email', 'name')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
