# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Afas(models.Model):

    #__Afas_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)

    #__Afas_FIELDS__END

    class Meta:
        verbose_name        = _("Afas")
        verbose_name_plural = _("Afas")


class Accounts(models.Model):

    #__Accounts_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    code = models.TextField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField()

    #__Accounts_FIELDS__END

    class Meta:
        verbose_name        = _("Accounts")
        verbose_name_plural = _("Accounts")



#__MODELS__END
