from django.contrib import admin
from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('home/', views.home, name='home'),
    path('home/<int:selected>', views.detail, name='detail'),
    path('home/all_student', views.all_student, name="normal_view_all_student"),



    path('student/<int:pk>/', views.Student_profile.as_view(), name='student_profile'),



    path('dan/', views.danTest.as_view(), name='dan'),
    path('svengates/', views.SvenGates.as_view(), name='svengates'),
    path('yilin/', views.YilinView.as_view(), name='yilin'),
    path('tarun/', views.Tarun.as_view(), name='tarun'),
    path('index1/', views.index1.as_view(), name='index1'),
    path('enowell/', views.enowell.as_view(), name='enowell'),
]
