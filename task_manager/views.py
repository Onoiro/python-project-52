from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.http import HttpResponse


# use this path '/trigger-error' when need to check connect to rollbar
def trigger_error(request):
    1 / 0
    return HttpResponse("This should not be reached")


class IndexView(View):

    def get(self, request, *args, **kwargs):
        content = {
            'welcome': _("Welcome to Task Manager!"),
            'description': _('Task Manager is a web application designed '
                             'to manage tasks in an organization or team.<br>'
                             'Task Manager allows users to register, create '
                             'and effectively manage tasks.'),
            'read_more': _("Read more"),
        }
        return render(request, 'index.html', context=content)


class UserLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form: AuthenticationForm):
        messages.success(self.request, _("You successfully logged in"))
        return super().form_valid(form)


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
