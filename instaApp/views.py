from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, User, Image


# Create your views here.
def home(request):
    return render(request, 'index.html')


'''
 limit only an authenticated User to view a full profile
 '''


@login_required(login_url='/login/')
def profile(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "dashboard/profile.html", {"profile": profile})


# def search_results(request):
#     if 'category' in request.GET and request.GET["category"]:
#         search_term = request.GET.get('category')
#         searched_images = Image.search_by_category(search_term)
#         message = f"{search_term}"
#
#         return render(request, 'albums/search.html', {"message": message, "categories": searched_images})
#
#     else:
#         message = "...You haven't searched for any term"
#         return render(request, 'albums/search.html', {"message": message})
