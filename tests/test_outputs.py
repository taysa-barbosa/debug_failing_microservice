import subprocess
import time
import requests
import os


def test_app_starts():
    """Test if the app starts without crashing"""
    proc = subprocess.Popen(["python", "/app/app.py"])
    time.sleep(3)
    assert proc.poll() is None, "App failed to start"
    proc.terminate()


def test_endpoint_response():
    """Test if endpoint returns correct response"""
    proc = subprocess.Popen(["python", "/app/app.py"])
    time.sleep(3)

    response = requests.get("http://localhost:5000")
    assert response.status_code == 200
    assert "App is running" in response.text

    proc.terminate()


def test_redis_required():
    """Ensure Redis is actually required"""
    # Remove env var to simulate failure
    if "REDIS_HOST" in os.environ:
        del os.environ["REDIS_HOST"]

    proc = subprocess.Popen(["python", "/app/app.py"])
    time.sleep(3)

    # App should crash without REDIS_HOST
    assert proc.poll() is not None, "App should fail without REDIS_HOST"


def test_dependencies_fixed():
    """Check if dependency issue was resolved"""
    with open("/app/requirements.txt", "r") as f:
        content = f.read()

    assert "requests==2.31.0" in content, "Dependency not fixed"
