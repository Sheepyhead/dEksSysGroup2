from django.shortcuts import render
from .models import Guide, Category, GuideSuggestion
from .forms import SubmitNewGuide, SubmitNewRequest
from django.template.response import SimpleTemplateResponse
from django.views import View


def index(request):
    all_guides = Guide.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'guides/index.html', {'all_guides': all_guides, 'all_categories': all_categories})


def guide(request, guide_id):
    return render(request, 'guides/guide.html', {'guide': Guide.objects.get(pk=guide_id)})


class CreateGuide(View):
    def get(self, request):
        form = SubmitNewGuide()
        context = {
            "form": form
        }
        return render(request, 'guides/create_guide.html', context)

    def post(self, request):
        form = SubmitNewGuide(request.POST)
        if form.is_valid():
            Guide.objects.create(title=form.cleaned_data['title'],
                                 short_description=form.cleaned_data['short_description'],
                                 text=form.cleaned_data['text'],
                                 category=form.cleaned_data['category'], author=request.user)
        return index(request)


def guide_suggestions(request):
    all_suggestions = GuideSuggestion.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'guides/guide_suggestions.html',
                  {'all_suggestions': all_suggestions, 'all_categories': all_categories})


class CreateRequest(View):
    def get(self, request):
        form = SubmitNewRequest()
        context = {
            "form": form
        }
        return render(request, 'guides/request_guide.html', context)

    def post(self, request):
        form = SubmitNewRequest(request.POST)
        if form.is_valid():
            GuideSuggestion.objects.create(name=form.cleaned_data['name'],
                                           description=form.cleaned_data['description'],
                                           category=form.cleaned_data['category'])
        return index(request)
