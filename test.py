import requests
import pandas as pd

# lat = 21.361494  # Vĩ độ
# lng = 105.349980  # Kinh độ

url = f'https://nominatim.openstreetmap.org/reverse?lat=21.361494&lon=105.349980&format=json'
response = requests.get(url)

# data = response.json()
print(response)