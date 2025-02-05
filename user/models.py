from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars", default="avatars/default_user.png")

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})
