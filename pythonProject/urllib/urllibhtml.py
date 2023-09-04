import urllib.request

try:
    url=urllib.request.urlopen("https://www.python.org/")
    content=url.read()
    url.close()
except urllib.error.HTTPError:
    print("Webpage is not available")
    exit()

f=open("phython.html","wb")
f.write(content)
f.close()