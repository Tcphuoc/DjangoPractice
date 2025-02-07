from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class BaseForm():
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

class RegisterForm(BaseForm, UserCreationForm):
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name', 'avatar', 'password1', 'password2']
		labels = {
			'avatar': 'Avatar (Optional):',
		}

class EditUserForm(BaseForm, forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name', 'avatar']
		labels = {
			'avatar': 'Avatar (Optional):',
		}
