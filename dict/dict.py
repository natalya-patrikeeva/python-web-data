# Count the number of times a word occurs in a text
# Return the most frequent word with its count

name = raw_input("Enter file: ")
handle = open(name,'r')
text = handle.read()
# print len(text), text[:40]
words = text.split()
# print len(words)
# print words
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
    # print word, counts[word]
print counts # dictionary

print counts.items() # list of tuples

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount
