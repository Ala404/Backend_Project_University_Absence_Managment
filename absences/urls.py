from django.urls import path
from . import views

urlpatterns = [
    path('absences/', views.absence_list),
    path('absences/<str:id>', views.absence_detail),
]