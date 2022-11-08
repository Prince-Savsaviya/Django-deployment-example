from django.urls import path,include
from app1 import views

app_name = 'app1'
urlpatterns = [
    path('',views.index,name='index'),
    path('browse.html/',views.browse,name='browse'),
    path('details.html/',views.details,name='details'),
    path('streams.html/',views.streams,name='streams'),
    path('profile.html/',views.profile,name='profile'),
    path('registration.html/',views.registration,name='registration'),
]
