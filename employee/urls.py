
from django.urls import path
from . import views

#child urls of the main registered url
urlpatterns = [
    path('', views.employee),
    path('profile/', views.profile, name='profile'),
]
