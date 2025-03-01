import requests

url = 'http://127.0.0.1:5000/update_traffic'
data = {
    'lane': 'lane1',
    'vehicle_count': 45
}

response = requests.post(url, json=data)
print(response.json())