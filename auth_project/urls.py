from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views # Needed for the debug view

urlpatterns = [
    path('admin/', admin.site.urls),
    # Point everything to accounts. We will handle the 'api/' prefix inside accounts.urls
    path('', include('accounts.urls')), 
    path('debug-media/', views.debug_media),
]

# Serves media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)