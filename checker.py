import requests
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url) # Sends HTTP GET request to the url
        status_code = response.status_code # Retrieves the HTTP status code from the response
        response_time = response.elapsed.total_seconds() * 1000 # Converted to milliseconds (* 1000)
        status = "Online" if status_code < 400 else "Offline" # Determines status based off the code
        return {
                "url": url,
                "status": status,
                "status_code": status_code,
                "response_time_ms": response_time,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Formats current time as readable string
            }
    except requests.exceptions.RequestException as exception:
        # Catches any network error - site unreachable, timeout etc...
        return {
                "url": url,
                "status": "Offline",
                "status_code": None, # No status code available if site is unreachable
                "response_time_ms": None, # No response time available if site is unreachable
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }