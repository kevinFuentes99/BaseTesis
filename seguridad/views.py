from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Panel_principal_view(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"
