
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path ('', include('adminApps.urls')),
    ######Prof#########
    path('', include('profs.urls')),
    ######Module#######
    path('', include('modules.urls')),
    ######Section#######
    path('', include('sections.urls')),
    ######Schedule#######
    path('', include('schedules.urls')),
    path('', include('sessionApps.urls')),
    path('', include('classrooms.urls')),
    path('', include('students.urls')),
    path('', include('absences.urls')),
    path('', include('justifications.urls')),
    path('', include('exclusions.urls')),
    path('', include('profiles.urls')),




]
