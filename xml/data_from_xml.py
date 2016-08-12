import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')

url = urllib.urlopen(address)
data = url.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')
#print counts

sum = 0
for i in counts:
    num = int(i.text)
    sum = sum + num
print sum
