from django.urls import path
from . import views




urlpatterns = [
    path('admins/', views.admin_list),
    path('admins/<str:pk>/', views.admin_detail),
]