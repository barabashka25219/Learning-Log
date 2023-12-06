from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Userinfo
from .forms import UserInfoForm
from PIL import Image

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save() 
            login(request, new_user)
            return redirect('users:profile', user_id=new_user.id)
        
    context = {
        'form': form,
    }
    
    return render(request, 'users/register.html', context)


@login_required
def profile(request, user_id):
    profile = Userinfo.objects.get(user=user_id)

    if request.method == 'GET':
        profile_form = UserInfoForm(instance=profile)
    else:
        profile_form = UserInfoForm(instance=profile, data=request.POST, files=request.FILES)

        if profile_form.is_valid():
            profile_form.save()
        
        resized_image = Image.open(f'{profile.avatar.url[1:]}')
        new_image = resized_image.resize((60, 60))
        new_image.save(f'{profile.avatar.url[1:]}')

    context = {
        'profile_form': profile_form,
        'user_info': profile,
    }
    
    return render(request, 'users/profile.html', context)