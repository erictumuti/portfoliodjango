from django.urls import path
from . import views

#child urls of the main registered url
urlpatterns = [
    path('', views.contactus, name='contact'),
]
