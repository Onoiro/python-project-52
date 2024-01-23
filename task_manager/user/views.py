from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

from .forms import UserRegisterForm
from django.contrib.auth.models import User


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users_list'
    

class UserCreateView(CreateView, SuccessMessageMixin):
    form_class = UserRegisterForm
    template_name = 'user/user_create_form.html'
    success_url = reverse_lazy('login')
    success_message = 'User created successfully'
    
    # def form_valid(self, form):
    #     messages.success(self.request, 'User created successfully')
    #     return super().form_valid(form)
    
    # def get_success_url(self):
    #     return reverse_lazy('login')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'user/user_create_form.html'
    success_url = reverse_lazy('user-update')

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.request.user.pk)

    def form_valid(self, form):
        messages.success(self.request, 'User updated successfully')
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return ('user-list')
    

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/user_delete.html'

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.request.user.pk)
    
    def get_success_url(self):
        messages.success(self.request, 'User deleted successfully')
        return reverse_lazy('user-list')


class UserLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form: AuthenticationForm):
        messages.success(self.request, "You successfully logged in")
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, "You are logged out")
        return response
