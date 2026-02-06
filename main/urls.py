from django.urls import path
from . import views
from .views import LessonCreateView,LessonListView
app_name = 'main'

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('diary/', views.diary, name='diary'),
    path('teacher/', views.TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('admin-panel/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),

]