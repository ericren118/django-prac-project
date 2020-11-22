from django.urls import path, include
from jobs import views

app_name='jobs'

urlpatterns = [
    path('', views.joblist, name='joblist'),
    path('job/<int:pk>/', views.jobdetail, name='jobdetail'),

    path('newjoblist/',views.JobListView.as_view(), name='newjoblist'),
    path('new_job_detail/<int:pk>/', views.JobDetailView.as_view(), name='new_job_detail'),

    ]
