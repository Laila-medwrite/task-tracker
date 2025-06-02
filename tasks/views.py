from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class TaskListCreateView(generics.ListCreateAPIView):
    """
    A viewset for viewing and editing task instances.
    Handles GET (list all tasks) and POST (create a new task).
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A viewset for viewing, updating, and deleting task instances.
    Manages GET (retrieve a task), PUT (update a task), and DELETE (delete a task) for a specific task ID.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
