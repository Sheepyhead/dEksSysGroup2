from django.shortcuts import render
from django.template.response import SimpleTemplateResponse
from django.views.generic import TemplateView


def index(request):
    return SimpleTemplateResponse(template="index.html")
