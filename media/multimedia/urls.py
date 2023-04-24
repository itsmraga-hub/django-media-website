from django.urls import path
from multimedia.views import AudioListView, ImageListView, VideoListView, HomeView, AddImageView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('audios', AudioListView.as_view(), name='audio_list'),
  path('images', ImageListView.as_view(), name='image_list'),
  path('videos', VideoListView.as_view(), name='video_list'),
  path('images/add-image', AddImageView.as_view(), name='add_image')
]