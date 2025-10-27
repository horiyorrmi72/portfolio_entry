from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Experience
from .serializers import ExperienceSerializer

# Create your views here.
class RootView(APIView):
    def get(self,request):
        return Response({"message":"Welcome, is it a sunny day :)?"})
    
class ExperienceListView(generics.ListAPIView):
    queryset=Experience.objects.all().order_by('id')
    serializer_class=ExperienceSerializer

