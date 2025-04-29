# from django.urls import path
# from .views import VideoUploadView,VideoListView

# urlpatterns = [
#     # api/courses/... 
#     path('upload/', VideoUploadView.as_view(), name='video-upload'),
#     path('videos/', VideoListView.as_view(), name='video-list'),

# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ModuleViewSet, VideoViewSet, PDFFileViewSet, RatingViewSet, DownloadViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'pdfs', PDFFileViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'downloads', DownloadViewSet)

# Include the router's URLs
urlpatterns = [
    path('', include(router.urls)),
]




# Endpoint	                                 HTTP Method	                    Description
# /api/courses/       	                     GET, POST	                        List all courses or create a new course
# /api/courses/<id>/	                     GET, PUT, DELETE	                Retrieve, update, or delete a course
# /api/modules/       	                     GET, POST	                        List all modules or create a new module
# /api/modules/<id>/	                     GET, PUT, DELETE       	        Retrieve, update, or delete a module
# /api/videos/	                             GET, POST	                        List all videos or create a new video
# /api/videos/<id>/	                         GET, PUT, DELETE	                Retrieve, update, or delete a video
# /api/pdfs/	                             GET, POST	                        List all PDFs or upload a new PDF
# /api/pdfs/<id>/	                         GET, PUT, DELETE	                Retrieve, update, or delete a PDF
# /api/ratings/	                             GET, POST	                        List all ratings or create a new rating
# /api/ratings/<id>/  	                     GET, PUT, DELETE	                Retrieve, update, or delete a rating
# /api/downloads/	                         GET, POST	                        List all downloads or create a new download
# /api/downloads/<id>/	                     GET, PUT, DELETE	                Retrieve, update, or delete a download