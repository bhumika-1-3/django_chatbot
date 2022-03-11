import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True , **other):
        if not email:
            raise ValueError("Invalid email address")

        if not password:
            raise ValueError("Enter the password")

        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        # user_obj.username = username
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_staff=True,

        )
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=255)
    phone = models.CharField(null=True , max_length=12)
    # can login
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

# email and password required
    REQUIRED_FIELD = []

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, app_label):
        return True


    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
