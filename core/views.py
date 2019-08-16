from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['skills'] = Skill.objects.all()
        context['works'] = RecentWork.objects.all()
        context['moocs'] = MOOC.objects.all()
        context['contacts'] = ContactMethod.objects.all()
        return context

def redirect_portfolio(request):
    response = redirect('/portfolio')
    return response