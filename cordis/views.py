from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cordis.models import Project
from cordis.serializers import ProjectSerializer

@api_view(['GET'])
def project_list(request):
    """
    List all existing projects
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def project_detail(request, pk):
    """
    Retrieves project data, or parses the project data from <a href="http://cordis.europa.eu" target="_blank">Cordis</a> if not yet available in the local data storage.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
    	try:
			# Parse on the fly now
			project = Project(rcn=pk)
			project.parse_cordis()
			project.save()
    	except:
        	return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)