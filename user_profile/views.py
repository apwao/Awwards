from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from projects.models import Project

# Create your views here.
@login_required(login_url='/accounts/login/')
def create_profile(request):
    """
    """
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            created_profile = form.save(commit=False)
            created_profile.user_id = current_user.id
            created_profile.save()
                
        return redirect(view_profile)
    
    else:
        form=ProfileForm()
    return render(request, 'create_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def view_profile(request):
    print(request)
    """
    """
    current_user=request.user
    print('-' * 30)
    print(current_user.id)
    profile_photos=Profile.objects.filter(user_id=current_user.id)
    print(profile_photos)
    # all_user_photos=Image.objects.filter(editor=current_user.id)
    return render(request, 'profile.html',{'profile_photos':profile_photos})

