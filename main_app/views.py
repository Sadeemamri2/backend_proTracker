
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.generics import ListCreateAPIView


# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to home route!'}
    return Response(content)



class ProjectListCreateView(ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer