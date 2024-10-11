from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Class_html(TemplateView):
    template_name = 'class_templ.html'


def html_func(request):
    return render(request, 'func_templ.html')