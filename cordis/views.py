from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView

from rest_framework import renderers
from rest_framework.reverse import reverse

from cordis.models import Project
from cordis.serializers import ProjectSerializer

class ProjectList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectDetail(APIView):
    """
    Retrieves project data, or parses the project data from <a href="http://cordis.europa.eu" target="_blank">Cordis</a> if not yet available in the local data storage.
    """	

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
	    	try:
				# Parse on the fly now
				project = Project(rcn=pk)
				project.parse_cordis()
				project.save()
				return project
	    	except:
	    		raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


# @api_view(('GET',))
# def api_root(request, format=None):
#     return Response({
#         'projects': reverse('projects.views.ProjectList', request=request, format=format)
#     })