import urllib.request, urllib.parse, urllib.error
import json

address = "http://py4e-data.dr-chuck.net/comments_244360.json"

uh = urllib.request.urlopen(address)
data = uh.read()

js = json.loads(data)

total = 0
for number in js['comments']:
    count = (number['count'])
    total = count + total
print(total)
