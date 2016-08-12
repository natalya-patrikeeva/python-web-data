import urllib
import json

url = raw_input("Enter location: ")

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved', len(data), 'characters'

info = json.loads(data)

# print info
# pretty print
#print json.dumps(info, indent=4)
#print info["comments"]
#print "=========="
#print len(info["comments"])

sumcount = 0
for i in range(len(info["comments"])):
    count = int(info["comments"][i]["count"])
    sumcount = sumcount + count

print sumcount
