from django.shortcuts import render
from django.views import generic


class Index(generic.TemplateView):
    template_name = 'app/base.html'

class danTest(generic.TemplateView):
    template_name = 'app/test.html'

class YilinView(generic.TemplateView):
    template_name = 'app/ybase.html'


class index1(generic.TemplateView):
    template_name = 'app/index1.html'


class SvenGates(generic.TemplateView):
    template_name = 'app/svengates.html'





class Tarun(generic.TemplateView):
    template_name = 'app/tarun.html'

class enowell(generic.TemplateView):
    template_name = 'app/enowell.html'