from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _


class IndexView(View):
    def get(self, request, *args, **kwargs):
        hello_from_hexlet = _("Hello from Hexlet!")
        coding_courses = _('Practical programming courses')
        read_more = _("Read more")
        exit = _("Exit")
        return render(request, 'index.html',
                      context={'hello_from_hexlet': hello_from_hexlet,
                               'coding_courses': coding_courses,
                               'read_more': read_more,
                               'exit': exit,
                               })
