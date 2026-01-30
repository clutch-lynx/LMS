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
    


from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
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
        context['grades'] = Grade.objects.all().order_by('id')
        return context

    def post(self, request, *args, **kwargs):
        students = CustomUser.objects.filter(role='student')
        subjects = Subject.objects.all()

        for student in students:
            for subject in subjects:
                field_name = f'grade_{student.id}_{subject.id}'
                value = request.POST.get(field_name)

                if value:
                    Grade.objects.create(
                        student=student,
                        subject=subject,
                        value=value
                    )

        return redirect('main:diary')
    



# views.py
from .models import Lesson

class LessonCreateView(RoleRequiredMixin, TemplateView):
    template_name = 'lesson_create.html'
    allowed_roles = ['teacher', 'admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['teachers'] = CustomUser.objects.filter(role='teacher')
        context['lessons'] = Lesson.objects.order_by('date', 'start_time')
        return context

    def post(self, request, *args, **kwargs):
        Lesson.objects.create(
            subject_id=request.POST['subject'],
            teacher_id=request.POST['teacher'],
            date=request.POST['date'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time'],
        )
        return redirect('main:lesson_create')