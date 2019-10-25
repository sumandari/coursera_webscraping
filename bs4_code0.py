import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
num = input('how many result do you want? - ')
while True:
    try:
        num = int(num)
        break
    except ValueError:
        num = input('entry number only! - ')
        
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the achor tags
print('Links, anchor tags: ', num, 'items')
counts = 0
tags = soup('a')
for tag in tags:
    print(tag)
    print('-----', tag.get('href', None))
    counts +=1
    if counts > num - 1:
        break
