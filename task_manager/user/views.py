from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User
from .forms import UserForm
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class UserListView(ListView):
    model = User
    form_class = UserForm()
    context_object_name = 'users_list'
    template_name = 'user_list.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_create_form.html'
    success_url = reverse_lazy('user-list')

    def save_user(self, request, *args, **kwargs):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                return redirect(self.success_url)
            else:
                form = UserForm()


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = 'user-list'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user
