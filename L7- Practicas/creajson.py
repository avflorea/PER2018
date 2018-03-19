import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Andreea',
    'surname': 'Florea',
    'from': 'Madrid',
    'IP': '212.128.255.131'

})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
