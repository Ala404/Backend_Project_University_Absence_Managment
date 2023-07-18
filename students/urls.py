from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<str:id>', views.student_detail),
]
