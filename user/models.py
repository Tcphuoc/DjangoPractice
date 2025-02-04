from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(AbstractBaseUser):
    class Levels(models.TextChoices):
        JUNIOR = 'JR', 'Junior'
        MIDDLE = 'ME', 'Middle'
        SENIOR = 'SR', 'Senior'

    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars", default="avatars/default_user.jpg")
    level = models.CharField(max_length=50, choices=Levels.choices, default=Levels.JUNIOR)
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.USER)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})
