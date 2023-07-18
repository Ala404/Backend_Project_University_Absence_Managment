from django.urls import path
from .models import Section, Group
from . import views


urlpatterns = [
    path('sections/', views.section_list),
    path('sections/<str:pk>',views.section_detail),
    path('groups/',views.group_list),
    path('groups/<str:pk>',views.group_detail),
    
    
]



