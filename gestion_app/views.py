# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView



def index(request):
	return render(request, 'index.html')

#class HomeView(TemplateView):
 #   template_name = 'index.html'