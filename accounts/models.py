from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser, PermissionsMixin
)
# from django.contrib.auth.models import Group as DjangoGroup

# class GroupPermissions(models.Model):
#     """Instead of trying to get new user under existing `Aunthentication and Authorization`
#     banner, create a proxy group model under our Accounts app label.
#     Refer to: https://github.com/tmm/django-username-email/blob/master/cuser/admin.py
#     """
#     description = models.CharField(max_length=150, null=True, blank=True, verbose_name="Human readable name")

#     class Meta:
#         verbose_name = 'group perms'
#         verbose_name_plural = 'group perms'

#     def __str__(self):
#         return self.description

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email_address',
        max_length=255,
        unique=True,
    )
    username= models.CharField(max_length=30, null=True,blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # groups = models.ManyToManyField(GroupPermissions, null=True, verbose_name=('Group Permissions'), blank=True, help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default

    def get_full_name(self):
        # The user is identified by their email address
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        # The user is identifed by their email address
        return self.email
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    
    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app 'app_label'?"
    #     # Simplest possible answer: Yes, always
    #     return True
    
    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     return self.staff
    
    # @property
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.admin
    
    objects = UserManager()

    # class Meta:
    #     db_table = 'auth_user'

    # @property
    # def cached_groups(self):
    #     """Warning 'groups' is a field name (M2M) so can't called this property 'groups'"""
    #     if not hasattr(self, '_cached_groups'):
    #         self._cached_groups = DjangoGroup.objects.filter(user=self).values_list(
    #             'name', flat=True
    #         )
    #     return self._cached_groups

    # def in_groups(self, *names):
    #     for name in names:
    #         if name in self.cached_groups:
    #             return True
    #     return False

