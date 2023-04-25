from django.urls import path
from multimedia.views import AudioListView, ImageListView, VideoListView, HomeView, AddImageView, AddAudioView, AddVideoView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('audios', AudioListView.as_view(), name='audio_list'),
  path('images', ImageListView.as_view(), name='image_list'),
  path('videos', VideoListView.as_view(), name='video_list'),
  path('images/add-image', AddImageView.as_view(), name='add_image'),
  path('images/add-video', AddVideoView.as_view(), name='add_video'),
  path('images/add-audio', AddAudioView.as_view(), name='add_audio'),
]