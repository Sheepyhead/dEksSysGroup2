from django.conf.urls import url
from django.http import HttpResponse

from . import views

urlpatterns = [
    url(r'^$', views.index, name="guides"),
    url(r'^guide/(?P<guide_id>\d+)/$', views.guide, name="guide"),
    url(r'^create_guide', views.CreateGuide.as_view(), name="create_guide"),
    url(r'^guide_suggestions', views.guide_suggestions, name="guide_suggestions"),
    url(r'^request_guide', views.CreateRequest.as_view(), name="request_guide")
]
