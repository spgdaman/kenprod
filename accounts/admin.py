from typing import Set

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
# , GroupPermissions
# , Group

class UserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'last_login',)
    search_fields = ('email','first_name', 'last_name',)
    ordering = ('first_name', 'last_name', 'email',)
    # filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        ('User Info', {'fields': ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'last_login',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
        ('Groups', {'fields': ('groups',)}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        is_admin = request.user.is_admin
        disabled_fields = set()

        # Prevent changing permissions without using groups
        if not is_superuser or not is_admin:
            disabled_fields |= {
                "is_superuser",
                "user_permissions",
            }
        
        # Prevent users changing own permissions
        if not is_superuser or not is_admin and obj is not None and obj == request.user:
            disabled_fields |= {
                "email_address",
                "first_name",
                "last_name",
                "last_login",
                "is_active",
                "is_admin",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
admin.site.register(User, UserAdmin)

# admin.site.register(User)
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     ordering = ('first_name', 'last_name', 'email')
#     fieldsets = (
#         # ('Permissions', {'fields': ('groups',)}),
#         ('Permissions', {
#             'classes': ['wide'],
#             'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'permissions')
#         })
#     )
#     filter_horizontal = ('groups', 'user_permissions',)
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('name', 'email', 'password1', 'password2', 'phone', 
#                 'civilId', 'address', 'groups',)}
#         ),
#         ('Permissions', {'fields': ('groups',)}),
#     )
    # list_display = ['email', 'first_name', 'last_name']
#     list_display = (
#         'first_name',
#         'last_name',
#         'email',
#         'is_staff',
#         'is_active',
#         'in_groups',
#     )
#     list_display_links = list_display
    # list_filter = (
    #     'groups',
    #     'is_staff',
    #     'is_active',
    # )
    # search_fields = ('email', 'first_name', 'last_name')

#     def in_groups(self, obj):
#         """
#         get group, separate by comma, and display empty string if user has no group
#         """
#         return ', '.join([x.name for x in obj.groups.all()]) if obj.groups.count() else ''
    
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()  # type: Set[str]

#         if not is_superuser:
#             disabled_fields |= {
#                 'username',
#                 'is_superuser',
#                 'user_permissions',
#             }

#         for f in disabled_fields:
#             if f in form.base_fields:
#                 form.base_fields[f].disabled = True

#         return form

# admin.site.register(User, CustomUserAdmin)
# admin.site.unregister(Group)

# admin.site.register(GroupPermissions)


# @admin.register(Group)
# class GroupAdmin(BaseGroupAdmin):
#     model = Group
#     fields = ('name', 'permissions',)
#     list_display = ('name', 'description')
#     list_display_links = list_display
#     order = ('name',)








# from django.contrib.auth import get_user_model

# User = get_user_model()

# class CustomUserAdmin(UserAdmin):
#     list_filter = ['is_active']
#     ordering = ('first_name', 'last_name', 'email')
#     readonly_fields = ["date_joined"]
    
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()

#         # Prevent changing permissions without using groups
#         if not is_superuser:
#             disabled_fields |= {
#                 "is_superuser",
#                 "user_permissions",
#             }

#         # Prevent users changing own permissions
#         if not is_superuser and obj is not None and obj == request.user:
#             disabled_fields = {
#                 "is_staff",
#                 "is_superuser",
#                 "groups",
#                 "user_permissions",
#             }

#         for f in disabled_fields:
#             if f in form.base_fields:
#                 form.base_fields[f].disabled = True

#         return form

# admin.site.register(User, CustomUserAdmin)