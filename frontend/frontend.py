import time
import requests

backend_url = "http://backend-container:5000"

while True:
    try:
        response = requests.get(backend_url)

        if response.status_code == 200:
            print("Frontend received the following response from the backend:")
            print(response.text)
        else:
            print("Failed to communicate with the backend.")

    except Exception as e:
        print("Error connecting to backend:", e)

    time.sleep(10)
