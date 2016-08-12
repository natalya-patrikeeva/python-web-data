import urllib
from BeautifulSoup import *

# http://python-data.dr-chuck.net/known_by_Evelyn.html
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

# Find position 3
print tags[17]
#for tag in tags:
    #print tag.get('href', None)
#    print 'TAG:', tag
#    print 'URL:', tag.get('href', None)
#    print 'Content:', tag.contents[0]
#    print 'Attrs:', tag.attrs
for i in range(6):
    url = tags[17].get('href', None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    print tags[17]
