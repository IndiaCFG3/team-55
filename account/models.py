from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, first_name, last_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			first_name=first_name,
			last_name=last_name
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password, first_name, last_name):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			first_name=first_name,
			last_name=last_name
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	first_name              = models.CharField(max_length=100)
	last_name 				= models.CharField(max_length=100, blank=True)
	# designation				= models.CharField(max_length=50, choices=[("Null","Select Designation"), ("Professor", "Professor"), ("Associate Professor", "Associate Professor"),("Assistant Professor","Assistant Professor")], default="Select Designation")
	# date_of_joining			= models.DateField(default=datetime.date.today)
	# experience_months		= models.IntegerField(null=False, default=0)
	# experience_years		= models.IntegerField(null=False, default=0)
	# scale_of_pay			= models.IntegerField(null=False, default=0)
	user_type				= models.CharField(max_length=20, blank=True, choices=[("IT", "IT"), ("HOD", "HOD"), ("HR", "HR"), ("OPERATIONS","OPERATIONS"), ("ACCOUNT", "ACCOUNT"), ("AUDIT", "AUDIT"), ("ENC", "ENC"), ("IMPACT SUPPORT", "IMPACT SUPPORT")])

    

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True