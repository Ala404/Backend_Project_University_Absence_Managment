from django.urls import path
from . import views


urlpatterns = [
    path('modules/', views.module_list),
    path('modules/<int:pk>/', views.module_detail),
]
 