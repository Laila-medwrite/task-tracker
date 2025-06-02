from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import uuid
# Create your views here.

tasks = [] #initialize an empty in-memory list

VALID_STATUSES = ['pending', 'in_progress', 'done']

def find_task(task_id):
    """
    Helper function to find a task by its ID.
    returns none if not found.
    """
    return next((task for task in tasks if task['id']== task_id), None)

class TaskListView(APIView):
    def get(self, request):
        """Retrieve the list of tasks."""

        return Response(tasks, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new task."""

        title = request.data.get('title')
        status_value = request.data.get('status', 'pending')

        if not title:
            return Response({"error": "Title is required."}, status=400)
        
        if status_value not in VALID_STATUSES:
            return Response({"error": f"Invalid status. Valid statuses are: {', '.join(VALID_STATUSES)}"}, status=400)
        
        task = {
            "id": str(uuid.uuid4()),  # Generate a unique ID for the task
            "title": title,
            "status": status_value,
            "created_at": datetime.now().isoformat() + "Z",
        }
        tasks.append(task)
        return Response(task, status=status.HTTP_201_CREATED)
    
class TaskDetailView(APIView):
    def get(self, request, task_id):
        """Retrieve a task by task id."""

        task = find_task(task_id)
        if not task:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(task, status=status.HTTP_200_OK) 

    def put(self, request, task_id):
        task = find_task(task_id)
        if not task:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        title = request.data.get('title', task['title'])
        status_value = request.data.get('status', task['status'])

        if status_value not in VALID_STATUSES:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        task['title'] = title
        task['status'] = status_value
        return Response(task, status=status.HTTP_200_OK) 

    def delete(self, request, task_id):
        """Delete a task by task id."""
        task = find_task(task_id)
        if not task:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        tasks.remove(task)
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
