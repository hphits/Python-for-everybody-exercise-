import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_244357.html', context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

total = 0
tags = soup('span')
for tag in tags:
    #print(tag.get('href', None))
     number= int(tag.contents[0])
     total = total + number
print(total)
