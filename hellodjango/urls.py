from django.conf.urls import patterns, include, url
from rest_framework import routers
from quickstart import views
from django.views.generic import DetailView, ListView
from cordis.models import Project


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
    url(r'^projects/$', 'project_list'),
    url(r'^projects/(?P<pk>[0-9]+)/$', 'project_detail'),
)