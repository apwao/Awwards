def view_profile(request):
    try:
        current_user=request.user 
        user_profile=Profile.objects.get(user_id=current_user.id)
    except:
        return redirect(create_profile)
    return render(request, 'view_profile.html',{'user_profile':user_profile})
