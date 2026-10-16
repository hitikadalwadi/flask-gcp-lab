import requests
import json

url = 'http://127.0.0.1:8080/predict'

# A sample district (values from the first row of the dataset)
payload = {
    'med_inc': 8.3252,
    'house_age': 41,
    'ave_rooms': 6.98,
    'ave_bedrms': 1.02,
    'population': 322,
    'ave_occup': 2.56,
    'latitude': 37.88,
    'longitude': -122.23
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Status:", response.status_code)
print("Body:", response.text)

if response.status_code == 200:
    try:
        prediction = response.json()['prediction']
        print(f'Predicted median house value: ${prediction:,.0f}')
    except Exception as e:
        print("Could not parse JSON:", e)
else:
    print('Error:', response.status_code)
