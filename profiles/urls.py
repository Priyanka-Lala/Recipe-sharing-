from django.urls import path
from .views import Profiles,Editprofile

urlpatterns = [
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit/<slug:pk>/",Editprofile.as_view(),name="edit_profile")
]
