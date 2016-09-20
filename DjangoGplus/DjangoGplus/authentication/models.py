from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser

from django.db import models

# Create your models here.

#AbstractBaseUser is DjangoDefined class to get all the related fields
# for a base user.
class Account(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)

	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)


    is_admin= models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # For getting a model instance in Django we need to Give it in the
    # format <className>Manager(). to instantiate an object. 
    # similar to Java obj a = new obj()
    objects = AccountManager()

    # Treat the email field to be the username (This is a unique field)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
    	return self.email

    def get_full_name(self):
    	return ' '.join([self.first_name,self.last_name])

    def get_short_name(self):
    	return self.first_name
