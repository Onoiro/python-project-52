from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.permissions import CustomPermissions
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from task_manager.tasks.forms import TaskForm
from django.shortcuts import redirect
from django_filters.views import FilterView
from task_manager.tasks.filters import TaskFilter


class TaskPermissions(CustomPermissions):
    pass


class TaskDeletePermissionMixin():
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if not task.author == request.user:
            messages.error(request,
                           _("Task can only be deleted by its author."))
            return redirect('tasks:tasks-list')
        return super().dispatch(request, *args, **kwargs)


class TaskFilterView(TaskPermissions, FilterView):
    model = Task
    template_name = 'tasks/task_filter.html'
    filterset_class = TaskFilter


class TaskDetailView(TaskPermissions, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_create_form.html'
    success_url = reverse_lazy('tasks:tasks-list')
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(TaskPermissions, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks:tasks-list')
    success_message = _('Task updated successfully')


class TaskDeleteView(TaskDeletePermissionMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:tasks-list')
    success_message = _('Task deleted successfully')
