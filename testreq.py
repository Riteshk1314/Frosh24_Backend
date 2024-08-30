import requests

# The URL of your API endpoint
url = "http://127.0.0.1:8000/event/list"

# The data for the new event
data = {
    "event_id": "unique_event_id_here",  # Make sure this is unique
    "name": "New Test Event",
    "date": "2024-09-15",
    "venue": "Test Venue",
    "is_booking": True,
    "slot_id": "TEST001",
    "is_live": True,
    "image": "https://example.com/test-image.jpg",
    "is_display": True,
    "time": "10:00 AM",
    "description": "This is a test event description"
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
print(f"Status Code: {response.status_code}")
print("Response:")
print(response.json())