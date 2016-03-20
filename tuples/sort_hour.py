#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)

handle = open('mbox-short.txt')
lst = list()
tmp = list()
counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split(' ')
        line = line[6].split(':')
        lst.append(line[0])

for key in lst:
    counts[key] = counts.get(key, 0) + 1

for k, v in counts.items():
    tmp.append( (k,v))

tmp.sort()

for k,v in tmp:
    print k, v
