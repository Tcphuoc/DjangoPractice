from django.db import models
from user.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    estimation_hours = models.FloatField(null=True)
    requirements = models.TextField()
    image = models.ImageField(default="images/default_course.jpg",upload_to='images', null=True)
    users = models.ManyToManyField(User, blank=True)

class Progress(models.Model):
    completed_lessons = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
