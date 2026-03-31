import requests

response = requests.get('https://oim.108122.xyz/words/random')

print(response.json())   # a random word

response = requests.get(
    'https://oim.108122.xyz/words/mass', 
#    headers={'X-Token': 'mirandamiranda'})  # your first name x2
)
data=response.json()

print(data['name'])
print(data['governor'])

print(len(data))
print(data.keys())
print(type(data['data'])) # to explore the data structure

towns = data['data']
print(type(towns))

#pprint(towns)
print(len(towns))

smallest = min(towns, key=lambda x: x['population'])
print(smallest['name'], smallest['population'])