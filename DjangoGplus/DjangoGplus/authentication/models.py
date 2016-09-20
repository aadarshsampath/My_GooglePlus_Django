from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import BaseUserManager

from django.db import models

# Create your models here.

class AccountManager(BaseUserManager):
	def create_user(self,email,password=None, **kwargs):
		if not email:
			raise ValueError('Users must have a valid email address')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username')

		account = self.model(
			email=self.normalize_email(email), username=kwargs.get('username'))

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self,email,password, **kwargs):
		account=self.create_user(email,password, **kwargs)

		account.is_admin = True
		account.save()

		return account


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
