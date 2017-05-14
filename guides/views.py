from django.shortcuts import render
from .models import Guide, Category, GuideSuggestion
from django.template.response import SimpleTemplateResponse


def index(request):
    all_guides = Guide.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'guides/index.html', {'all_guides': all_guides, 'all_categories': all_categories})


def guide(request, guideID):

    return render(request, 'guides/guide.html', {'guide' : Guide.objects.get(pk=guideID)})


def create_guide(request):
    return SimpleTemplateResponse('guides/create_guide.html')

def guide_suggestions(request):
    all_suggestions = GuideSuggestion.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'guides/guide_suggestions.html', {'all_suggestions': all_suggestions, 'all_categories': all_categories})
