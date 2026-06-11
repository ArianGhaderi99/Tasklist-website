from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/login.html'   # همان صفحه تب‌دار
    success_url = reverse_lazy('task:task_list')   # بعد از ثبت‌نام به صفحه تسک‌ها برود

    def form_valid(self, form):
        response = super().form_valid(form)
        # پس از ثبت‌نام، کاربر را وارد می‌کنیم
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
        login(self.request, user)
        messages.success(self.request, 'Registration successful. Welcome!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('task:task_list')

    def get_success_url(self):
        return self.success_url

    def form_valid(self, form):
        messages.success(self.request, 'Login successful.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('task:task_list')