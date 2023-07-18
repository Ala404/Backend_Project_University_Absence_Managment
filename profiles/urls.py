from django.urls import path
from . import views



urlpatterns = [
     path('profiles/', views.profiles_list, name='profile'),
    path('profiles/<str:pk>', views.profiles_detail),
]
