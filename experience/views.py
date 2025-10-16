from rest_framework import generics, status
from rest_framework.response import Response
from .models import Experience
from .serializers import ExperienceSerializer

# Create your views here.
class ExperienceListView(generics.ListAPIView):
    queryset=Experience.objects.all().order_by('id')
    serializer_class=ExperienceSerializer

