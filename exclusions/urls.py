from django.urls import path
from . import views

urlpatterns = [
    path('exclusions/', views.exclusion_list),
    path('exclusions/<str:id>', views.exclusion_detail),
]