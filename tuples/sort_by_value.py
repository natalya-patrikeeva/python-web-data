# The top 10 most common words.
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append( (val, key))

lst.sort(reverse=True)

for val, key in lst[:10] :
    print key, val


# Even shorter version
c = {'a':10, 'b':1, 'c':22}
print sorted( [ (v,k) for k,v in c.items() ] )

print dir(lst)
print "---------------"
print dir(lst[0])


t = ('Mon', 'Tue', 'Wed', 'Thu')
print t[2]
