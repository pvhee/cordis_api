from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from cordis.models import Project
from cordis import views

router = routers.DefaultRouter()

urlpatterns = patterns('cordis.views',
	url(r'^cordis/1/projects/$', views.ProjectList.as_view()),
    url(r'^cordis/1/projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),

    # @todo fix this, not sure why api_root doesn't work?
    # url(r'^$', 'api_root'),
    url(r'^$', views.ProjectList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)