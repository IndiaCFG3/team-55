from django.shortcuts import render
from django.views.generic import TemplateView

class StaticView(TemplateView):
	template_name = “views.html”
# Create your views here.
