from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from projects.models import Project
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from rest_framework import status

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
    user_profile=Profile.objects.get(user_id=current_user.id)
    # all_user_photos=Image.objects.filter(editor=current_user.id)
    return render(request, 'view_profile.html',{'user_profile':user_profile,'current_user':current_user})

class ProfileList(APIView):
    """
    """
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
    
    def post(self, request, formal=None):
        """
        method post used to perform POST operations
        """
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)