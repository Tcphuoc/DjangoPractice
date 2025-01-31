from django.db import models

# Create your models here.
class User(models.Model):
    class Levels(models.TextChoices):
        JUNIOR = 'JR', 'Junior'
        MIDDLE = 'ME', 'Middle'
        SENIOR = 'SR', 'Senior'

    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars")
    level = models.CharField(max_length=50, choices=Levels.choices, default=Levels.JUNIOR)
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.USER)
