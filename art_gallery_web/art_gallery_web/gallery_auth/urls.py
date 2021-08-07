from django.urls import path

from art_gallery_web.gallery_auth.views import RegisterView, LogInView, LogOutView, UserProfileView

urlpatterns = [
    path('login/', LogInView.as_view(), name="login user"),
    path('logout/', LogOutView.as_view(), name="logout user"),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile/', UserProfileView.as_view(), name='my_profile'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
]
