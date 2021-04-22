from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from app.models import Student
from django.template import loader

def home(request):
    return HttpResponse("<h1>hello</h1> there")

def detail(request, selected):
    return HttpResponse("You're looking at selection of {}".format(selected))

def all_student(request):
    student_list = Student.objects.all()
    template = loader.get_template('app/normal_view.html')
    return HttpResponse(template.render({"all_student": Student.objects.all()}, request))
    # Yilin, lemme know if you still don't get it. khaaa

class Index(generic.ListView):
    model = Student
    template_name = 'app/base.html'

class Student_profile(generic.DetailView):
    queryset = Student.objects.all()
    context_object_name = 'student'
    template_name = 'app/student_profile.html'


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

