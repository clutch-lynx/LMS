from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from .models import Subject, Grade

User = get_user_model()

def first_page(request):
    return render(request, 'first_page.html')
# Міксін для ролей
class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in self.allowed_roles:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@login_required
def diary(request):
    students = User.objects.filter(role='student')
    subjects = Subject.objects.all()
    grades = Grade.objects.all()

    return render(request, 'diary.html', {
        'students': students,
        'subjects': subjects,
        'grades': grades
    })




# Admin dashboard — додає уроки, користувачів
class AdminDashboardView(RoleRequiredMixin, TemplateView):
    template_name = 'admin_dashboard.html'
    allowed_roles = ['admin']


from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import CustomUser, Subject, Grade

class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in self.allowed_roles:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class TeacherDashboardView(RoleRequiredMixin, TemplateView):
    template_name = 'teacher_dashboard.html'
    allowed_roles = ['teacher', 'admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = CustomUser.objects.filter(role='student')
        context['subjects'] = Subject.objects.all()
        context['grades'] = Grade.objects.all()
        return context