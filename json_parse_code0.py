import json

data = '''
{
 "name" : "chunk",
 "phone": {
    "type" : "intl",
    "number" : "+1 123 2345 1234"
  },
  "email" : {
    "hide" : "yes"
  }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
