from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView
from multimedia.models import AudioMedia, VideoMedia, ImageMedia
from .forms import AddImageForm, AddAudioForm, AddVideoForm


# Create your views here.
class HomeView(TemplateView):
  template_name = 'home.html'

class AudioListView(ListView):
    model = AudioMedia
    template_name = 'audio_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        audios = AudioMedia.objects.all()
        context['audios'] = audios
        return context


class VideoListView(ListView):
    model = VideoMedia
    template_name = 'video_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = VideoMedia.objects.all()
        context['videos'] = videos
        return context


class ImageListView(ListView):
    model = ImageMedia
    template_name = 'image_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = ImageMedia.objects.all()
        context['images'] = images
        return context


class AddImageView(FormView):
    template_name = 'add_image.html'
    form_class = AddImageForm
    success_url = "/media/images"

    def form_valid(self, form):
        image = ImageMedia.objects.create(
          image = form.cleaned_data['image'],
          name = form.cleaned_data['name']
        )
        image.save()
        return super().form_valid(form)


class AddVideoView(FormView):
    template_name = 'add_video.html'
    form_class = AddVideoForm
    success_url = "/media/videos"

    def form_valid(self, form):
        video = VideoMedia.objects.create(
          file = form.cleaned_data['file'],
          title = form.cleaned_data['title']
        )
        video.save()
        return super().form_valid(form)


class AddAudioView(FormView):
    template_name = 'add_audio.html'
    form_class = AddAudioForm
    success_url = "/media/audios"

    def form_valid(self, form):
        audio = AudioMedia.objects.create(
          file = form.cleaned_data['file'],
          title = form.cleaned_data['title']
        )
        audio.save()
        return super().form_valid(form)