from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, RegisterForm

# LoginView без змін
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('main:first_page')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)

# RegisterView з правильною обробкою ролі та пароля
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm  # наша форма з роллю
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # хешуємо пароль
        user.save()
        return super().form_valid(form)

# HomeView (Diary) без змін
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'main/diary.html'