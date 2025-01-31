from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course/index.html', context)

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course
    }
    return render(request, 'course/detail.html', context)
