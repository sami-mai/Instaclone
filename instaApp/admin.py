from django.contrib import admin
from .models import Image, Profile, Tag, Comment


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('Tag',)


# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Tag)
