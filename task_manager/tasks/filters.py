import django_filters
from django import forms
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status'),
        widget=forms.Select
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor'),
        widget=forms.Select
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label'),
        widget=forms.Select
    )

    self_tasks = django_filters.BooleanFilter(
        field_name='author',
        label=_('Just my tasks'),
        widget=forms.CheckboxInput(),
        method='filter_own_tasks',
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
