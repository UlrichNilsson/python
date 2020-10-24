import json

name = "example.json"
handle = open(name)

data=handle.read().rstrip()

#print(data)

info=json.loads(data)

print('User count',len(info))