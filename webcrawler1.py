import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter URL: ')
lpos=int(input('Enter position: '))
jp=int(input('Enter count: '))

count=0
while count<=jp:
    html=urllib.request.urlopen(url, context=ctx).read()
    print('Retrieving: ', url)
    soup=BeautifulSoup(html , 'html.parser')
    tags=soup('a')
    tag=tags[lpos-1]
    url=tag.get('href', None)
    count=count+1

nstrs=soup('h1')
nstr=nstrs[0]
nmst=str(nstr)
name=nmst.split()
print('target', name[2])
#http://py4e-data.dr-chuck.net/known_by_Rose.html
