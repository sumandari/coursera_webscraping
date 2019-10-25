import json

input = '''
[
  {"id": "001",
   "x": "2",
   "name": "Chunk"
  },
  {"id": "001", 
   "x": "2",
   "name": "Chunk"
  }
]   
'''

info = json.loads(input)
print('User counts:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

