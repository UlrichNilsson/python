import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#address = 'http://py4e-data.dr-chuck.net/comments_42.xml'#input('Enter location: ')
address = input('Enter location: ')
#'http://py4e-data.dr-chuck.net/comments_1024437.xml'
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieving', address)
print('Retrieved', len(data), 'characters')

#print(data.decode())
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')

print('Count:', len(comments))
sum=0
for comment in comments:
    sum=sum + int(comment.find('count').text)
    #print('Count:',comment.find('count').text)

print('Sum:',sum)