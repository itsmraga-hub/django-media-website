from django.urls import path
from multimedia.views import AudioListView

urlpatterns = [
  path('audio/', AudioListView.as_view(), name='audio_list')
]