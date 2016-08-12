import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    # finds lines that start with 'From: email.address'
    if not line.startswith('From: ') : continue
    pieces = line.split()
#    print pieces
    email = pieces[1]
#    print email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    try:
        count = cur.fetchone()[0]
        # either increment the count by 1 if the email already exists in DB
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email, ))
    except:
        # or insert a new row with a new email address and count 1
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES ( ?, 1 )''', ( email, ) )
    conn.commit()

# select 10 the most frequent emails
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
