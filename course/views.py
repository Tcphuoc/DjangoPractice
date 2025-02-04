from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
from .forms import CourseForm

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

def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success("Create course success!")
            return redirect("course:index")
    else:
        form = CourseForm()
    return render(request, 'course/course_form.html', { 'form': form })
