import requests
from pprint import pprint
from dotenv import load_dotenv
import os

# response = requests.get('https://oim.108122.xyz/words/random')

# print(response.json())   # a random word

# response = requests.get(
#     'https://oim.108122.xyz/words/mass', 
# #    headers={'X-Token': 'mirandamiranda'})  # your first name x2
# )
# data=response.json()

# print(data['name'])
# print(data['governor'])

# print(len(data))
# print(data.keys())
# print(type(data['data'])) # to explore the data structure

# towns = data['data']
# print(type(towns))

# #pprint(towns)
# print(len(towns))

# smallest = min(towns, key=lambda x: x['population'])
# print(smallest['name'], smallest['population'])


# # GET: read all messages
# data = requests.get('https://oim.108122.xyz/messages').json()
# for msg in data:
#     print(msg)

# requests.post('https://oim.108122.xyz/message',
#               json={'message': 'Hello from Miranda!'},
#               headers={'X-Token': 'mirandamiranda'})

#openweather

load_dotenv()

cities = ['Wellesley', 'Boston']

API_KEY = os.getenv("OPENWEATHER_API_KEY", "").strip()

if not API_KEY:
       raise SystemExit("Missing OPENWEATHER_API_KEY in .env")

for city in cities:
       url = (f'https://api.openweathermap.org/data/2.5/weather'
              f'?q={city}&appid={API_KEY}&units=imperial')
       response = requests.get(url, timeout=10)
       response.raise_for_status()
       data = response.json()

       temp = data.get('main', {}).get('temp')
       if temp is None:
              raise SystemExit(f"No temperature in response for {city}: {data}")

       print(f"{city}: {temp}°F")