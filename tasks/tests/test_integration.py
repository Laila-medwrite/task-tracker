import pytest

@pytest.mark.django_db
def test_task_integration(client):
    """Test the full integration flow of creating, updating, and retrieving a task."""
    
    # Create a new task
    task_data = {
        "title": "Integration Test Task",
        "status": "pending"
    }
    create_response = client.post("/api/tasks/", task_data, format='json')
    assert create_response.status_code == 201  
    task_id = create_response.data["id"]  

    # Update the task
    updated_data = {
        "title": "Updated Integration Test Task",
        "status": "done"
    }
    update_response = client.put(f"/api/tasks/{task_id}/", updated_data, content_type='application/json')
    assert update_response.status_code == 200  

    # Retrieve the updated task
    retrieve_response = client.get(f"/api/tasks/{task_id}/")
    assert retrieve_response.status_code == 200  
    assert retrieve_response.data["title"] == "Updated Integration Test Task"
    assert retrieve_response.data["status"] == "done"
