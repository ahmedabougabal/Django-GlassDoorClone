# every app should have its own urls
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.job_list), # returns all jobs (job_list) it will be triggered when the user types localhost:8000/jobs
    path('<int:job_id>', views.job_detail), # returns a single job
]
