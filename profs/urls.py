from django.urls import path
from . import views


urlpatterns = [
    path('profs/', views.prof_list, name='profs'),
    path('profs/<str:pk>', views.prof_detail),
]

