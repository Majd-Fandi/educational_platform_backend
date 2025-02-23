from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')  # Videos will be stored in 'media/videos/'
    uploaded_at = models.DateTimeField(auto_now_add=True)