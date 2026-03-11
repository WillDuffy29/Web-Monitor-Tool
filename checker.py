import requests
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url) # Fetches all url information
        status_code = response.status_code # Parses response to find url status code
        response_time = response.elapsed.total_seconds() * 1000 # Converted to milliseconds
        status = "Online" if status_code < 400 else "Offline"
        return {
                "url": url,
                "status": status,
                "status_code": status_code,
                "response_time_ms": response_time,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    except requests.exceptions.RequestException as exception:
        return {
                "url": url,
                "status": "Offline",
                "status_code": None,
                "response_time_ms": None,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }