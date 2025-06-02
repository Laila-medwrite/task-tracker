import pytest 
from rest_framework.test import APIClient 
from tasks.models import Task 



@pytest.mark.django_db 
def test_create_task(client):
    """Test creating a new task."""
    
    data = {"title": "Test Task","status": "pending"}
    response = client.post("/api/tasks/", data, format='json')
    assert response.status_code == 201
    assert response.data["title"] == "Test Task"
    assert response.data["status"] == "pending"

@pytest.mark.django_db
def test_list_tasks(client):
    """Test listing all tasks."""

    Task.objects.create(title="Sample", status="done")
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_task_by_id(client):
    """Test retrieving a task by its ID."""

    task = Task.objects.create(title="One task", status="pending")
    response = client.get(f"/api/tasks/{task.id}/")
    assert response.status_code == 200
    assert response.data["title"] == "One task"

@pytest.mark.django_db
def test_update_task(client):
    """Test updating an existing task."""

    task_data = {"title": "Original Task", "status": "pending"}
    create_response = client.post("/api/tasks/", task_data, format='json')
    task_id = create_response.data["id"]  

    updated_data = {"title": "Updated Task", "status": "done"}
    response = client.put(f"/api/tasks/{task_id}/", updated_data, content_type='application/json')
    
    assert response.status_code == 200
    assert response.data["title"] == "Updated Task"
    assert response.data["status"] == "done"  

@pytest.mark.django_db
def test_delete_task(client):
    """Test deleting an existing task."""

    task_data = {"title": "Task to Delete", "status": "pending"}
    create_response = client.post("/api/tasks/", task_data, format='json')
    task_id = create_response.data["id"] 

    response = client.delete(f"/api/tasks/{task_id}/")

    assert response.status_code == 204 
    check_response = client.get(f"/api/tasks/{task_id}/")
    assert check_response.status_code == 404 
