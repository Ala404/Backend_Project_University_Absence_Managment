from django.urls import path
from . import views


urlpatterns = [
    path('sessions/', views.session_list, name='session'),
    path('sessions/<str:pk>', views.session_detail),

#     path('sessionDate/', views.datasession_list, name='sessionDate'),
#     path('sessionDate/<str:pk>', views.datasession_detail),
]

