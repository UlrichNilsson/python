import urllib.request, urllib.parse, urllib.error
import json

# API key
#https://cloud.google.com/maps-platform/user-guide/account-changes/#no-plan

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input('Enter location : ')
    if(len(address)<1):break
    
    url = serviceurl + urllib.parse.urlencode({'address':address})
    
    print('Retrieving',url)
    
    uh = urllib.request.urlopen(url)
    
    data = uh.read().decode()
    
    print('Retrieved', len(data),'characters')
    
    try:
        js = data.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] !='OK':
        print('========Failure to retrieve=====')
        print(data)
        continue
    
    print(json.dumps(js,inent=4))
    
    lat = js["result"][0]["gemometry"]["location"]["lat"]