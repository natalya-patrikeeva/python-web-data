import urllib
from BeautifulSoup import *

url = raw_input('Enter - ') # i.e. "http://www.dr-chuck.com/page1.htm"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
# tags = soup('a')
tags = soup('span')
sum = 0
for tag in tags:
#    print tag.get('href', None)

#    print 'TAG:', tag
#    print 'URL:', tag.get('href', None)
    print 'Content:', tag.contents[0]
#    print 'Attrs:', tag.attrs

    num = int(tag.contents[0])
    sum = sum + num

print sum
