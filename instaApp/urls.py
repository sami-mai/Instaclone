from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^accounts/single/', views.single, name='single'),
    url(r'^accounts/create/', views.create, name='create'),
    # url(r'^search/', views.search_results, name='search_results'),
]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
