import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate error
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1024435.html' #'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags=soup('span')

sum=0
count=0
    
for tag in tags:
    try:
        #print(tag.decode())
        y=re.findall('>(\S+)<',tag.decode())
        sum=sum + int(y[0])
        count=count+1
    except:
        continue
    

print('Count',count)
print('Sum',sum)

    