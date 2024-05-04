from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_user(request):

    if request.method == 'POST':
        logout(request)
        return redirect('blog-home')
    
    return render(request, 'users/logout.html')


@login_required # decorator: adds functionality to a existing function
def profile(request):
    return render(request, 'users/profile.html')
