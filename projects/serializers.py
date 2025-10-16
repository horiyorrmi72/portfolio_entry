# serializers.py
from rest_framework import serializers
from .models import Project, ProjectStack

class ProjectStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStack
        fields = ['id', 'stack']

class ProjectSerializer(serializers.ModelSerializer):
    stacks = ProjectStackSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'category', 'project_sample_media', 'project_sample_url', 'stacks']
