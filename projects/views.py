from rest_framework import status, generics
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.
class ProjectListView(generics.ListAPIView):
    queryset=Project.objects.all().order_by("id")
    serializer_class=ProjectSerializer