from django.shortcuts import render
from .models import Guide, Category
from django.template.response import SimpleTemplateResponse
from django.views.generic import TemplateView


def index(request):
    all_guides = Guide.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'guides/index.html', {'all_guides': all_guides, 'all_categories': all_categories})
