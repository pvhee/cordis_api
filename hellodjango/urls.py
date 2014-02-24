from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from cordis.models import Project
from cordis import views
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()

urlpatterns = patterns('cordis.views',
	url(r'^cordis/1/projects/$', views.ProjectList.as_view()),
    url(r'^cordis/1/projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
	url(r'^cordis/1/search/(?P<pk>[\w\-]+)/$', views.Search.as_view()),
	url(r'^cordis/1/search/(?P<pk>[\w\-]+)/(?P<count>[0-9]+)/$', views.Search.as_view()),
	url(r'^cordis/1/search-list/(?P<pk>[\w\-]+)/$', views.SearchList.as_view()),
	url(r'^cordis/1/search-list/(?P<pk>[\w\-]+)/(?P<count>[0-9]+)/$', views.SearchList.as_view()),

	# Redirect to the projects overview, we don't (yet) have a homepage for this API
	url(r'^$', RedirectView.as_view(url='/cordis/1/projects/')),
)

urlpatterns = format_suffix_patterns(urlpatterns)