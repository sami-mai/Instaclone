from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    # url(r'^login/', views.login, name="login"),
    url(r'^accounts/profile/(\d+)', views.user_profile, name="user_profile"),
    url(r'^accounts/edit-profile/(\d+)', views.edit_profile, name='edit_profile'),
    url(r'^accounts/upload-photo/', views.upload_photo, name='upload_photo'),
    url(r'^post-comment/(/d+)', views.post_comment, name='post_comment'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^follow/(\d+)', views.follow, name="follow"),
    url(r'^likes/(\d+)', views.like_image, name='like_image'),
]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
