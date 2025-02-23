"""
URL configuration for educational_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/users/reset-password/', include('django_rest_passwordreset.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# endpoints :

# http://127.0.0.1:8000/api/users/
# http://127.0.0.1:8000/api/users/<id>
# http://127.0.0.1:8000/api/users/login
# http://127.0.0.1:8000/api/users/register
# http://127.0.0.1:8000/api/users/logout
# http://127.0.0.1:8000/api/users/token/refresh/
# http://127.0.0.1:8000/api/users/reset-password/
