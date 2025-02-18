# urls.py
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='home'),  # Ensure to use .as_view()
]
