from django.urls import path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients', views.PlayerViewsets, basename='clients')

urlpatterns = [
]

urlpatterns += router.urls