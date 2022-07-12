# Databases
# https://www.py4e.com/lessons/database
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
dic=dict()
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if line.startswith('From:'):
        r=line.split()[1].split("@")[1]
        if(r in dic):
            dic[r]+=1
            cur.execute(f'''
UPDATE Counts
SET count = {dic[r]}
WHERE org = "{r}";''')
        else:
            dic[r]=1
            cur.execute(f"insert into Counts values('{r}',1)")
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()