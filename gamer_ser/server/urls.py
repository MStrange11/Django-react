from django.urls import path, include
from .views import RegisterView,LoginView, UpdateUserProfileView,MyfriendsView

urlpatterns = [
    path('myfriends/', MyfriendsView.as_view()),
    path('profile/', UpdateUserProfileView.as_view(), name='update_profile'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]