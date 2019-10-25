import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.google.com/search?q=python')
for line in fhand:
    print(line.decode().strip())

