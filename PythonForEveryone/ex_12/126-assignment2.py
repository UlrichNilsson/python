
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def getsoup(url):
    #print(url,'get')
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

# Retrieve all of the anchor tags

#countto=4
#count=0
#positionto=2

#url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'

countto=7
count=0
positionto=17

url='http://py4e-data.dr-chuck.net/known_by_Raya.html'
print(url)
while(count<countto):
    position=0
    for tag in getsoup(url):
        if position==positionto:
            url=re.findall('"(\S+)"',tag.decode())[0]
            print(url)
            position=position+1
            count=count+1
            continue
        else:
            position=position+1
