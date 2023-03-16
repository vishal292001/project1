
import requests
  


def test_server():
    response = requests.get('http://localhost:8081')
    code = response.status_code
    assert 200 == code