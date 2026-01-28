import time
import requests

BACKEND_URL = "http://backend:8000/"

while True:
    try:
        response = requests.get(BACKEND_URL, timeout=5)
        print(f"[Frontend] Message from backend: {response.text}")
    except Exception as e:
        print(f"[Frontend] Backend not reachable: {e}")

    time.sleep(10)
