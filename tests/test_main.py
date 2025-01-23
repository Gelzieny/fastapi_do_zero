import sys
import os
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manage import app


client = TestClient(app)

def test_root():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}