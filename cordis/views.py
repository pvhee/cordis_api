from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cordis.models import Project
from cordis.serializers import ProjectSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# enable if doing POST
# @csrf_exempt

def project_list(request):
    """
    List all existing projects
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JSONResponse(serializer.data)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data, status=201)
    #     else:
    #         return JSONResponse(serializer.errors, status=400)


def project_detail(request, pk):
    """
    Retrieve a project, and parse from Cordis if not yet available
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:

    	# Parse on the fly now
    	project = Project(rcn=pk)
    	project.parse_cordis()
    	project.save()
        # return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return JSONResponse(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(snippet, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data)
    #     else:
    #         return JSONResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return HttpResponse(status=204)