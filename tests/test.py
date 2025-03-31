import pytest
import requests

BASE_URL = "http://localhost:8000"

@pytest.fixture
def theme_data():
    return {"name": "Test Theme"}

@pytest.fixture
def method_data():
    return {"name": "Test Method", "description": "A test method", "theme_id": 1}

@pytest.fixture
def task_data():
    return {"name": "Test Task", "description": "A test task", "theme_id": 1}

@pytest.fixture
def created_theme(theme_data):
    response = requests.post(f"{BASE_URL}/api/themes/", json=theme_data)
    assert response.status_code == 200, f"Failed to create theme: {response.text}"
    return response.json()

@pytest.fixture
def created_method(theme_data, method_data):
    theme_id = create_theme(theme_data)
    method_data["theme_id"] = theme_id
    response = requests.post(f"{BASE_URL}/api/methods/", json=method_data)
    assert response.status_code == 200, f"Failed to create method: {response.text}"
    return response.json()

@pytest.fixture
def created_task(theme_data, task_data):
    theme_id = create_theme(theme_data)
    task_data["theme_id"] = theme_id
    response = requests.post(f"{BASE_URL}/api/tasks/", json=task_data)
    assert response.status_code == 200, f"Failed to create task: {response.text}"
    return response.json()

def create_theme(theme_data):
    response = requests.post(f"{BASE_URL}/api/themes/", json=theme_data)
    assert response.status_code == 200, f"Failed to create theme: {response.text}"
    return response.json()["id"]

def test_create_theme(theme_data):
    response = requests.post(f"{BASE_URL}/api/themes/", json=theme_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == theme_data["name"]
    assert "id" in data

def test_read_themes():
    response = requests.get(f"{BASE_URL}/api/themes/?skip=0&limit=10")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_read_theme(created_theme):
    theme_id = created_theme["id"]
    response = requests.get(f"{BASE_URL}/api/themes/{theme_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == theme_id

def test_create_theme_invalid_data():
    invalid_data = {"name": ""}
    response = requests.post(f"{BASE_URL}/api/themes/", json=invalid_data)
    assert response.status_code == 422, f"Expected 422, got {response.status_code}: {response.text}"

def test_create_method(theme_data, method_data):
    theme_id = create_theme(theme_data)
    method_data["theme_id"] = theme_id
    response = requests.post(f"{BASE_URL}/api/methods/", json=method_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == method_data["name"]
    assert data["theme_id"] == theme_id

def test_read_methods():
    response = requests.get(f"{BASE_URL}/api/methods/?skip=0&limit=10")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_update_method(created_method):
    method_id = created_method["id"]
    theme_id = created_method["theme_id"]
    updated_data = {"name": "Updated Method", "description": "Updated desc", "theme_id": theme_id}
    response = requests.put(f"{BASE_URL}/api/methods/{method_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Method"

def test_delete_method(created_method):
    method_id = created_method["id"]
    response = requests.delete(f"{BASE_URL}/api/methods/{method_id}")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/api/methods/{method_id}")
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"

def test_create_task(theme_data, task_data):
    theme_id = create_theme(theme_data)
    task_data["theme_id"] = theme_id
    response = requests.post(f"{BASE_URL}/api/tasks/", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == task_data["name"]

def test_read_task(created_task):
    task_id = created_task["id"]
    response = requests.get(f"{BASE_URL}/api/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id

def test_create_theme_param(created_theme):
    theme_id = created_theme["id"]
    param_data = {"name": "color", "type": "string", "default_value": "blue", "theme_id": theme_id}
    response = requests.post(f"{BASE_URL}/api/theme-params/", json=param_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "color"

def test_delete_theme_param(created_theme):
    theme_id = created_theme["id"]
    param_data = {"name": "color", "type": "string", "default_value": "blue", "theme_id": theme_id}
    response = requests.post(f"{BASE_URL}/api/theme-params/", json=param_data)
    assert response.status_code == 200
    param_id = response.json()["id"]
    response = requests.delete(f"{BASE_URL}/api/theme-params/{param_id}")
    assert response.status_code == 200

if __name__ == "__main__":
    pytest.main(["-v"])