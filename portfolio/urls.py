
from django.contrib import admin
from django.urls import path, include
from . import views

#must import for media
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #registering urls of employee to the main url
    path('', include('index.urls')),
    path('employee/', include('employee.urls')),
    path('contact/', include('contact.urls')),
    path('authentication/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     #FOR MEDIA_URL
