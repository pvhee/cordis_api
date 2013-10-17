from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from cordis.models import Project

from cordis import views


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browseable API.
# urlpatterns = patterns('',
#     # url(r'^', include(router.urls)),
#     # url(r'^', include('snippets.urls')),
#     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#     # 


    
#     # (r'^projects/$', 
#     # 	ListView.as_view(
#     # 		queryset=Project.objects.all(),
#     # 		template_name='cordis/projects.html')),
# )


urlpatterns = patterns('cordis.views',
	url(r'^projects/$', views.ProjectList.as_view()),
    # url(r'^projects/$', 'project_list'),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),

    # @todo fix this, not sure why api_root doesn't work?
    # url(r'^$', 'api_root'),
    url(r'^$', views.ProjectList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)