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
from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    """
    def has_permission(self,request,view):
        """
        """
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

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
    try:
        current_user=request.user 
        user_profile=Profile.objects.get(user_id=current_user.id)
    except:
        return redirect(create_profile)
    return render(request, 'view_profile.html',{'user_profile':user_profile})

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
        permission_classes=(IsAdminOrReadOnly)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)