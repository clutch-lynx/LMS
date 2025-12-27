from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('diary/', views.diary, name='diary'),
    path('teacher/', views.TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('admin-panel/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
]