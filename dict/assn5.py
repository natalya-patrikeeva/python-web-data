name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,'r')
#text = handle.read()

counts = dict()
for line in handle:
    line = line.rstrip()
    if line == '' : continue # want to keep non blank lines
    words = line.split()
    if words[0] != 'From' : continue # continue to the next line
                                     # if the line does not start with From
    emailer = words[1]
    counts[emailer] = counts.get(emailer,0) + 1
#print counts.items()

person_most = None
biggest_count = None

for person, count in counts.items():
    if biggest_count is None or count > biggest_count:
        person_most = person
        biggest_count = count

print person_most, biggest_count
