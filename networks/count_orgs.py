# Read the mailbox data (mbox.txt) and count up the number of email messages
# per organization (i.e. domain name of the email address) using a database

import sqlite3

conn = sqlite3.connect('orgsdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    # finds lines that start with 'From: email.address'
    if not line.startswith('From: ') : continue
    pieces = line.split()

    email = pieces[1]
    org = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    try:
        count = cur.fetchone()[0]
        # either increment the count by 1 if the org already exists in DB
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
    except:
        # or insert a new row with a new organization and count 1
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( org, ) )
    conn.commit()

# select the top 10 organizations
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
