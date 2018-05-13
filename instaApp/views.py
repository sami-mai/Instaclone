from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment, WelcomeEmailRecipients
from .forms import EditProfile, CreateComment, NewImagePost, EditUserForm, WelcomeEmailForm
from django.db import transaction
from .email import send_welcome_email


# Create your views here.
def home(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = WelcomeEmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = WelcomeEmailRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('/accounts/login/')
    else:
        form = WelcomeEmailForm()
    context = {"images": images, "current_user": current_user, "form":form, "profiles":profiles}
    return render(request, 'index.html', context)


'''
 Limited to an authenticated User
 '''


@login_required(login_url='/accounts/login/')
def user_profile(request, id):
    current_user = request.user

    try:
        profile = Profile.objects.get(user=current_user.id)
        photos = Image.objects.filter(user=current_user.id)

    except DoesNotExist:
        raise Http404()

    context = {"current_user": current_user, "photos": photos, "profile": profile,}
    return render(request, 'dashboard/profile.html', context)


@login_required(login_url='/accounts/login/')
@transaction.atomic
def edit_profile(request, id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, request.FILES, instance=current_user.profile)
        user_form = EditUserForm(request.POST, instance=current_user)
        if profile_form.is_valid() and user_form.is_valid():
            profile = profile_form.save(commit=False)
            user = user_form.save(commit=False)
            profile.user = current_user
            profile.save()
            user.save()
            return redirect('user_profile', current_user.id)
    else:
        profile_form = EditProfile()
        user_form = EditUserForm()
    context = {"current_user": current_user, "profile_form": profile_form, "user_form": user_form, "profile": profile}
    return render(request, 'dashboard/edit-profile.html', context)


@login_required(login_url='/accounts/login/')
def upload_photo(request):
    current_user = request.user
    current_profile = current_user.profile
    if request.method == 'POST':
        uploads_form = NewImagePost(request.POST, request.FILES)
        if uploads_form.is_valid():
            post = uploads_form.save(commit=False)
            post.user = current_user
            post.profile = current_profile
            post.save()
            return redirect(user_profile, current_user.id)
    else:
        uploads_form = NewImagePost()
    return render(request, 'dashboard/create_post.html', {"uploads_form": uploads_form, "current_user": current_user})


@login_required(login_url='/accounts/login/')
def post_comment(request, image_id):
    current_user = request.user
    images_id = Image.objects.get(id=image_id)
    if request.method == 'POST':
        comment_form = CreateComment(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.image = images_id
            comment.user = request.user
            comment.save()
            return redirect('post_comment')
    else:
        comment_form = CreateComment()
    photo = Image.objects.get(id=image_id)
    comments = Comment.get_comments(photo=image_id)
    context = {"title": title, "photo": photo, "comments": comments, "comment_form": comment_form}
    return render(request, 'dashboard/post-comment.html', context)


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'profile' in request.GET and request.GET['profile']:
            search_term = request.GET.get('profile')
            searched_photos = Profile.search_profile(search_term)
            message = f"{search_term}"
            context = {"message": message, "searched_photos": searched_photos}
            return render(request, 'all-instagram/search.html', context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'dashboard/search.html', {"message": message})
