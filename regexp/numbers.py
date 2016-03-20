# Find numbers in text using regular expressions and compute their sum.
import re
#handle = open('regex_sum_42.txt')
handle = open('regex_sum_232723.txt')
#text = raw_input("Enter file:")
#handle = open(text,'r')
sum = 0
for line in handle:
    line = line.rstrip()
    num = re.findall('([0-9]+)',line)
    if len(num) > 0:
        print num
        for stri in num:
            sum = sum + int(stri)
            print sum
print 'Sum: ', sum


print "++++++++++++++"
# Do this in 2 lines using list comprehension?
