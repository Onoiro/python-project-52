from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect


class CustomPermissions(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authorized! Please login.'))
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
