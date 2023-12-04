from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from .forms import UserInfoForm

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
        info_form = UserInfoForm()
    else:
        print(dir(request.user))
        form = UserCreationForm(data=request.POST)
        info_form = UserInfoForm(data=request.POST)

        if form.is_valid() and info_form.is_valid():
            new_user = form.save()
            info_form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    
    return render(request, 'users/register.html', context={'form': form, 'info_form': info_form})
