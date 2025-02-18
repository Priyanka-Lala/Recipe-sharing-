from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('home.urls')),
    path('recipes/', include('recipes.urls')),  
    path('profiles/',include('profiles.urls')),
     path('meal_planner/', include('meal_planner.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
