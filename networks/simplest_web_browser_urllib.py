import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#for line in fhand:
#    print line.strip()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts

#fhand2 = urllib.urlopen('https://www.facebook.com')
#for line in fhand2:
#    print line.strip()
