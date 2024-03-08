from collections.abc import Iterable
from django.db import models
from Accounts.models import User



class BaseClass(models.Model):
    name = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
        ordering = ['name','date_created','date_updated']
        abstract = True


