from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
@login_required
def profile(request):
    if request.method == 'POST':
        name=ProfileForm(request.POST,instance=request.user)
        profile = request.user.profile
        if name.is_valid():
            name.save()
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
            profile.save()
        return redirect('profiles:profile')
    else:
        name=ProfileForm(instance=request.user) 
    return render(request, 'profiles/your_profile.html',{'name':name})
