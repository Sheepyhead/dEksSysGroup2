from django.conf.urls import url
from django.http import HttpResponse

from . import views

urlpatterns = [
    url(r'^$', views.index, name="guides"),
    url(r'^guide', views.guide, name="guide"),
    url(r'^create_guide', views.create_guide, name="create_guide")
]
