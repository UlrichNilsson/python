
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def getsoup(url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

# Retrieve all of the anchor tags

countto=4
count=0
positionto=3
position=0

for tag in getsoup('http://py4e-data.dr-chuck.net/known_by_Fikret.html'):
    print(count,countto)
    if countto==count:
        print(tag.get('href', None))
        #for tag2 in getsoup(tag.get('href', None)):
        #    print(' -> ',tag2.get('href', None))
    else:
        count=count+1
