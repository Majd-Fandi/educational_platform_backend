from rest_framework import serializers
from .models import Course, Module, Video, PDFFile, Rating, Download

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_file', 'duration', 'uploaded_at']

class PDFFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFFile
        fields = ['id', 'title', 'file', 'uploaded_at']

class ModuleSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    pdf_files = PDFFileSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'order', 'videos', 'pdf_files']

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    uploader = serializers.StringRelatedField()  # Show the uploader's username

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'slug', 'poster', 'uploader', 'created_at', 'updated_at', 'num_of_lessons', 'size', 'course_duration', 'modules']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'course', 'user', 'rating', 'created_at']

class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = ['id', 'course', 'user', 'downloaded_at']


# from rest_framework import serializers
# from .models import Video

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ['id', 'title', 'video_file', 'uploaded_at']