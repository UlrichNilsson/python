import urllib.request, urllib.parse, urllib.error
import json

#url='http://py4e-data.dr-chuck.net/comments_42.json'#input('Enter location : ')

url='http://py4e-data.dr-chuck.net/comments_1024438.json'

print('Retrieving',url)

uh = urllib.request.urlopen(url)

data = uh.read().decode()
                
info=json.loads(data)

print('Retrieved', len(data),'characters')

#print(data)
#print('Name:', info['comments'][0]['name'])

sum = 0
count = 0
    
for item in info['comments']:
    #print('Name:', item['name'])
    #print('Count:', item['count'])
    sum= sum + item['count']
    count=count + 1

print('Count:', count)
print('Sum:', sum)
