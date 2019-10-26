import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input('Enter count: '))
position = int(input('Enter position: '))

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Abdul.html', context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

while count>0:
    tags = soup('a')
    mytag=tags[position-1])
    requiredtag=mytag.get('href',None)
    url=str(requiredtag)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    count=count-1
    print(mytag.get('href', None))
