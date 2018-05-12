from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from .forms import UpdateProfile, CreateComment, NewImagePost


# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'index.html', {"images": images})


'''
 limit only an authenticated User to view and update full profile
 '''


@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    # photos = Profile.objects.filter(photos=current_user)
    return render(request, "dashboard/profile.html", {"profile": profile})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = UpdateProfile()
    # profile = Profile.objects.get(user=current_user)
    return render(request, 'dashboard/profile.html', {"form": form})


def single(request, image_id):

    # images_id = Image.objects.get(id=image_id)
    if request.method == 'POST':
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = images_id
            comment.profile = request.user
            comment.save()
            HttpResponseRedirect('single')
    else:
        form = CreateComment()

    # image = Image.objects.get(id=image_id)
    comments = Comment.objects.filter(image=image_id)
    return render(request, 'dashboard/single.html', {"comments": comments, "form": form})


@login_required(login_url='/accounts/login/')
def create(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImagePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
            HttpResponseRedirect('/accounts/profile')
    else:

        form = NewImagePost()
    return render(request, 'dashboard/create_post.html', {"form": form})
