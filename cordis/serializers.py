from django.forms import widgets
from rest_framework import serializers
from cordis.models import Project

class ProjectSerializer(serializers.Serializer):
    rcn = serializers.IntegerField()
    # project_acronym = serializers.CharField()
    data = serializers.CharField()