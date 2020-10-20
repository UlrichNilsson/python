import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate error
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


#url = 'http://www.dr-chuck.com/page1.htm'
url = 'http://www.dr-chuck.com/'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags=soup('a')
    
for tag in tags:
    print(tag.get('href',None))
    