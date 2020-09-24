from django.urls import path
from . import views

#child urls of the main registered url
urlpatterns = [
    path('', views.authlogin, name='login'),
    path('registeration/', views.authregisteration, name='registeration'),
    path('forgot-password/', views.forgotpassword, name='forgotpassword'),
    path('logout/', views.authlogout, name='logout'),
]
