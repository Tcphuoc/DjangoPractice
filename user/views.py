from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .forms import RegisterForm, EditUserForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} to Chatbot')
            return redirect('login')
    else:
        form = EditUserForm()
    return render(request, 'user/register.html', { 'form': form })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} to Chatbot')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', { 'form': form })

class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)
