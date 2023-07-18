from django.urls import path
from . import views

urlpatterns = [
    path('classrooms/', views.classroom_list, name='classrooms'),
    path('classrooms/<str:pk>', views.classroom_detail),
]

