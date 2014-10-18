from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	"""
	Subclass UserCreationForm so we can override the model field
	with get_user_model.  This allows users to specify their own
	custom AUTH_USER_MODEL.
	"""
	class Meta:
		model = get_user_model()
		fields = ("username",)