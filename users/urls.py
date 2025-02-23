from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, LogoutView,CurrentUserView,users_get,user_get_put_delete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # api/users/... 
    path('', users_get, name='users'),
    path('<int:pk>/', user_get_put_delete, name='user_detail'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
