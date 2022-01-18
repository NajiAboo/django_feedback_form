from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from feedback.settings import MEDIA_ROOT

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfileView.as_view()),
    
] 
