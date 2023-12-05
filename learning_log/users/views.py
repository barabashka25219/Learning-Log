from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Userinfo
from .forms import UserInfoForm

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        profile = Userinfo()

        if form.is_valid():
            new_user = form.save() 
            profile.user = new_user
            profile.save()
            login(request, new_user)
            return redirect('users:profile', user_id=new_user.id)
    
    return render(request, 'users/register.html', context={'form': form})

@login_required
def profile(request, user_id):
    profile = Userinfo.objects.get(user=user_id)
    avatar_img  = profile.avatar
    
    if avatar_img:
        avatar_url = avatar_img.url
    else:
        avatar_url = None

    if request.method == 'GET':
        profile_form = UserInfoForm(instance=profile)
    else:
        profile_form = UserInfoForm(instance=profile, data=request.POST, files=request.FILES)

        if profile_form.is_valid():
            profile_form.save()
    
    return render(request, 'users/profile.html', context={'profile_form': profile_form, 'user_id': user_id, 'avatar_url': avatar_url})