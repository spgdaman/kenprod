from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group as DjangoGroup

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Group

admin.site.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    ordering = ('first_name', 'last_name', 'email')
    # list_display = ['email', 'first_name', 'last_name']
    list_display = (
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'in_groups',
    )
    list_display_links = list_display
    list_filter = (
        'groups',
        'is_staff',
        'is_active',
    )
    search_fields = ('email', 'first_name', 'last_name')

    def in_groups(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ', '.join([x.name for x in obj.groups.all()]) if obj.groups.count() else ''

    
# admin.site.register(User, CustomUserAdmin)
admin.site.unregister(DjangoGroup)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin):
    fields = ('name', 'permissions')
    list_display = ('name', )
    list_display_links = list_display
    order = ('name',)


