import os
import sys
from http import HTTPStatus
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manage import app


client = TestClient(app)

def test_root():
  response = client.get("/")
  assert response.status_code == HTTPStatus.OK
  assert '<h1> Olá Mundo </h1>' in response.text