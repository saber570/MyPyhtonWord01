import sqlite3
conn = sqlite3.connect('food.db')
curs = conn.cursor()
try:
    curs.execute('''
    create table food(
    id   text primary key,
    name text,
    age text,
    sex text
    )
    ''')
    query = 'insert into food values(?,?,?,?)'

    for line in open('data.txt'):
        field = line.split(',')
        vals = field
        curs.execute(query,vals)

    conn.commit()
except:
    print "wrong"
finally:
    conn.close()
