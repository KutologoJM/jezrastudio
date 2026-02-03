from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Homepage(TemplateView):
    template_name = 'pages/homepage.html'


class AboutMe(TemplateView):
    template_name = 'pages/about-me.html'


class Resume(TemplateView):
    template_name = 'pages/resume.html'


class Projects(TemplateView):
    template_name = 'pages/projects.html'


class Blog(TemplateView):
    template_name = 'pages/blog.html'
