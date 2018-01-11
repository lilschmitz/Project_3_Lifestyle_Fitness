from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from profiles.forms import ProfileRegistrationForm
from profiles.models import UserProfile


def profile(request):
    profile = UserProfile.objects.all()
    data = {}
    data['object_list'] = profile
    return render(request, profile, data)

@login_required(login_url='/accounts/login')
def profile(request):
    try:
       profile = UserProfile.objects.get(user=request.user)
    except:
       UserProfile.DoesNotExist
       return render(request, "no_profile.html")
    else:
        return render(request, "profile.html")



@login_required(login_url='/login')
def no_profile(request, id):

    if request.method == 'POST':
       form = ProfileRegistrationForm()
       if form.is_valid():
           profile = form.save(commit=False)
           profile.user_id= request.user.id
           profile.save()
           return redirect('profile')
    else:
        form = ProfileRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'no_profile.html', args)



def missing_profile(request):
    form = ProfileRegistrationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form = ProfileRegistrationForm(request.POST, request.FILES)
            missing_profile = form.save(commit=False)
            missing_profile.user = request.user
            missing_profile.save()

        return render(request, "profile.html")
    else:
        form = ProfileRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request,'no_profile.html', args)



