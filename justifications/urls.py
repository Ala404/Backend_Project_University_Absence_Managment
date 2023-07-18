
from django.urls import path
from . import views

urlpatterns = [
    path('justifications/', views.justification_list),
    path('justifications/<str:id>', views.justification_detail),
]