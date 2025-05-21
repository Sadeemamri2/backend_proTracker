from django.urls import path
from .views import Home
from .views import ProjectListCreateView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
]