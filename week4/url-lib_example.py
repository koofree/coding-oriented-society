import urllib

req = urllib.urlopen('https://www.youtube.com/watch?v=bGZZxgixkew')
print req.read()