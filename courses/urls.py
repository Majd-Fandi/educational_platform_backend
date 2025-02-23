from django.urls import path
from .views import VideoUploadView,VideoListView

urlpatterns = [
    # api/courses/... 
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('videos/', VideoListView.as_view(), name='video-list'),

]
