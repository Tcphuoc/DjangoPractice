from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

@login_required
def index(request):
    return HttpResponse('Hello')

@login_required
def profile(request):
    return render(request, 'user/profile.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} to Learning')
            return redirect('course:course_index')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', { 'form': form })
