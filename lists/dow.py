fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line == '' : continue # want to keep non blank lines
    words = line.split()
    if words[0] != 'From' : continue # continue to the next line
                                     # if the line does not start with From
    print words[2] # day of the week
