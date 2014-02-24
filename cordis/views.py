from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView

from rest_framework import renderers
from rest_framework.reverse import reverse

from cordis.models import Project
from cordis.models import ProjectList
from cordis.serializers import ProjectSerializer
from cordis.serializers import ProjectListSerializer

import logging

class ProjectList(APIView):
    """
    List all <a href="http://cordis.europa.eu" target="_blank">Cordis projects</a> in the database.

    All projects are identified with a RCN (record control number). For example, check out the <a href="http://cordis.europa.eu/projects/latest-projects_en.html" target="_blank">latest projects</a>
    added to the Cordis database, look for the RCN (e.g. <i>105229</i> from <a href="http://cordis.europa.eu/projects/rcn/105229_en.html">POCAONTAS</a>), and construct the API call as follows:

    <a href="http://api.openconsortium.eu/cordis/1/projects/105229">http://api.openconsortium.eu/cordis/1/projects/105229</a>

    The page returns a HTML and a JSON (append <span class="prettyprint">?format=json</span>) version of the data from the Cordis database that is cached in the database for easy reference.
    """
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectDetail(APIView):
    """
    Retrieves project data, or parses the project data from <a href="http://cordis.europa.eu" target="_blank">Cordis</a> if not yet available in the local data storage.
    """	

    def get_object(self, pk, reset):
        try:
            if reset:
                raise Project.DoesNotExist
            return Project.objects.get(pk=pk)

        except Project.DoesNotExist:
            try:
                project = Project(rcn=pk)
                project.parse_cordis()
                project.save()
                return project
            except:
                raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk, request.GET.get('reset', None))
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

class SearchList(APIView):
    """
    Retrieves project rcn's from a Cordis search. Add the search key obtained in the URL as the parameter to this search.
    """ 
    def get(self, request, pk, count=10, format=None):
        from parse_cordis import listing
        data = listing.parse(pk, count)
        logging.debug(data)
        l = ProjectList(data=data)

        logging.debug(l)
        serializer = ProjectListSerializer(l)
        return Response(serializer.data)



class Search(APIView):
    """
    Retrieves detailed project information from a Cordis search. Add the search key obtained in the URL as the parameter to this search.
    """ 

    def get(self, request, pk, count=10, format=None):
        # try:
        from parse_cordis import listing
        reset = request.GET.get('reset', None)

        data = listing.parse(pk, count)

        projects = list()

        # loop through data and save new project
        for rcn in data:

            # get from cache first
            try:
                if reset:
                    raise Project.DoesNotExist

                project = Project.objects.get(pk=rcn)
            except Project.DoesNotExist:

                try:
                    project = Project(rcn=rcn)
                    project.parse_cordis()
                    project.save()
                except:
                    # save erroneous project anyways, we don't want to block on them always
                    project.save()
                    pass

            projects.append(project)
        
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


        # logging.debug(data)

        # listingObj = Listing(data=data)
        # serializer = ListingSerializer(listingObj)
        # return Response(serializer.data)
            # return l
        # except:
            # raise Http404

# @api_view(('GET',))
# def api_root(request, format=None):
#     return Response({
#         'projects': reverse('projects.views.ProjectList', request=request, format=format)
#     })