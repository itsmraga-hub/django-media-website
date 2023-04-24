from django.contrib import admin
from .models import ImageMedia, VideoMedia, AudioMedia


# Register your models here.
admin.site.register(AudioMedia)
admin.site.register(ImageMedia)
admin.site.register(VideoMedia)