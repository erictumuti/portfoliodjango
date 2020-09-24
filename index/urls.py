
from django.urls import path
from . import views

#child urls of the main registered url
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.aboutus, name='about'),
]
