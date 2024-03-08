from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from EduAid.validatino import isalphavalidator,isimagevalidator

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name,contact,role, password=None, password2=None):
        """
        Creates and saves a User with the given email, name,tc and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            contact = contact,
            role = role, # defingig the role of a user
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name,contact, password=None):
        """
        Creates and saves a superuser with the given email, name,tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            contact=contact,
            role=User.Roles.ADMIN,
       
        )
        user.is_admin = True
        # user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    class Roles(models.TextChoices):
        STUDENT='STUDENT'
        ADMIN='ADMIN'

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
       
    )
    name = models.CharField(max_length=64, validators=[isalphavalidator])
    contact = models.BigIntegerField(blank=True,null=True)
    role = models.CharField(choices=Roles.choices,max_length=10,default=Roles.STUDENT)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default = False)
    # is_student = models.BooleanField(default = False)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = "email"
    # USERNAME_FIELD = "name"

    REQUIRED_FIELDS = ["name",'contact']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin





