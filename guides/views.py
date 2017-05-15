from django.shortcuts import render
from .models import Guide, Category, GuideSuggestion
from .models import Guide, Category
from .forms import SubmitNewGuide
from django.template.response import SimpleTemplateResponse
from django.views import View


def index(request):
    all_guides = Guide.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'guides/index.html', {'all_guides': all_guides, 'all_categories': all_categories})


def guide(request, guideID):

    return render(request, 'guides/guide.html', {'guide' : Guide.objects.get(pk=guideID)})

class CreateGuide(View):
    def get(self, request):
        form = SubmitNewGuide()
        context = {
            "form": form
        }
        return render(request, 'guides/create_guide.html', context)

    def post(self, request):
        form = SubmitNewGuide(request.POST)
        context = {
            "form": form
        }
        return render(request, 'guides/index.html', context)
