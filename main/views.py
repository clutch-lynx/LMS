from django.shortcuts import render
from .models import CustomUser
# Create your views here.
def first_page(request):
    return render(request, 'first_page.html')


from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Subject, Grade,CustomUser

#User = get_user_model()

def diary(request):
    students = CustomUser.objects.all()
    subjects = Subject.objects.all()
    grades = Grade.objects.all()
    return render(request, 'diary.html', {
        'students': students,
        'subjects': subjects,
        'grades': grades
    })