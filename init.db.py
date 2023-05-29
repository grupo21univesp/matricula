import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO matricula (name, born, grad, sch, addr, city, uf, resp, email, tel) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
('Alexandre Estima Kawamura', '09/04/1975', 'EJA', 'UNIVESP', 'Av. Fabio Esquivel, 2900', 'Diadema', 'SP', 'Maria', 'alexandreek@hotmail.com', '(11)99202-1252')
           )

cur.execute("INSERT INTO login (id, pwd) VALUES (?, ?)",
('alexandre.kawamura', '2104845')
           )

cur.execute("INSERT INTO login (id, pwd) VALUES (?, ?)",
('alexandre.martins', '2100672')
           )

cur.execute("INSERT INTO login (id, pwd) VALUES (?, ?)",
('luiz.felizardo', '2100973')
           )

cur.execute("INSERT INTO login (id, pwd) VALUES (?, ?)",
('marcelo.tashiro', '2106280')
           )

cur.execute("INSERT INTO login (id, pwd) VALUES (?, ?)",
('washington.freire', '2018557')
            )

connection.commit()
connection.close()