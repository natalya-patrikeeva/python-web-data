hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if line.find('From:') >= 0:
    if line.startswith('From:'):
        print line

print '+++++++++++++++++++++++++'
import re       # regular expression
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('^From:', line):   # find a line that starts with (^) From
#   if re.search('^X.*:', line):
#    if re.search('^X-\S+:', line):
    emails = re.findall('^From: (\S+@\S+)', line)
    if emails != []:    print emails

    address = re.findall('^From: .*@([^ ]*)',line)
    if address !=[]:    print address

x = 'My 2 favorite numbers are 3 and 28'
y = re.findall('[0-9]+',x)                  # [0-9] means one digit
#print z
xx = 'From: Using the : character'
#yy = re.findall('^F.+:', xx)             # + one or more char greedy
yy = re.findall('^F.+?:', xx)             # +? one or more char not greedy
#print yy

print '+++++++++++++++++++++++++'
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)

    if len(stuff) != 1 : continue
    print stuff
    num = float(stuff[0])
    numlist.append(num)

print 'Maximum:', max(numlist)

print '+++++++++++++++++++++++++'
phrase = 'We just received $10.00 for coookies.'
ext = re.findall('\$[0-9.]+', phrase)
print ext
