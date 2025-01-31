from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=200)
    course_image = models.ImageField(default="images/default_course.jpg",upload_to='images', blank=True)
