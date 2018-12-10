import sqlite3
sql = sqlite3.connect("db3.sql")
db = sql.cursor()

#query = "CREATE TABLE telefony (id int, nazwisko text, imie text, numer int)"
#db.execute(query)
#query = "INSERT INTO telefony (id, nazwisko, imie, numer) VALUES (1,'Szatam', 'Stefan', 666)"
#db.execute(query)
#query = "INSERT INTO telefony (id, nazwisko, imie, numer) VALUES (2,'Kowalski', 'Tomasz', 541)"
#db.execute(query)
#query = "INSERT INTO telefony (id, nazwisko, imie, numer) VALUES (3,'Dyzurny', 'Oficer', 534)"
#db.execute(query)
#sql.commit()

# query = "CREATE TABLE studenci (indeks int, imie varchar(20), nazwisko varchar(20), odznaka int)"
# db.execute(query)
#
# query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (1, 'Damian', 'Puc', 19)"
# db.execute(query)
# query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (2, 'Marek', 'Prawocz', 17)"
# db.execute(query)
# query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (3, 'Monika', 'Kowalska', 16)"
# db.execute(query)
# query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (4, 'Dominika', 'Nowak', 10)"
# db.execute(query)
# query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (5, 'Kamil', 'AU', 26)"
# db.execute(query)
#
# query = "CREATE TABLE przedmioty (nazwa text)"
# db.execute(query)
#
# query = "INSERT INTO przedmioty (nazwa) VALUES ('informatyka')"
# db.execute(query)
# query = "INSERT INTO przedmioty (nazwa) VALUES ('matematyka')"
# db.execute(query)
# query = "INSERT INTO przedmioty (nazwa) VALUES ('fizyka')"
# db.execute(query)
# query = "INSERT INTO przedmioty (nazwa) VALUES ('wf')"
# db.execute(query)
#
# query = "CREATE TABLE oceny (id_studenta int, id_przedmiotu int, ocena int, data)"
# db.execute(query)
#
# query = "CREATE TABLE studenci_przedmioty (id_studenta int, id_przedmiotu int)"
# db.execute(query)
#
# sql.commit()

# query = "INSERT INTO studenci_przedmioty(id_studenta, id_przedmiotu) VALUES (2,3)"
# db.execute(query)
# query = "INSERT INTO studenci_przedmioty(id_studenta, id_przedmiotu) VALUES (3,2)"
# db.execute(query)
# query = "INSERT INTO studenci_przedmioty(id_studenta, id_przedmiotu) VALUES (2,4)"
# db.execute(query)
# query = "INSERT INTO studenci_przedmioty(id_studenta, id_przedmiotu) VALUES (1,4)"
# db.execute(query)
#
# query = "INSERT INTO oceny VALUES (1,4, 3, '2 styczen')"
# db.execute(query)
# query = "INSERT INTO oceny VALUES (1,2, 1, '2 styczen')"
# db.execute(query)
# query = "INSERT INTO oceny VALUES (2,4, 5, '2 styczen')"
# db.execute(query)
# query = "INSERT INTO oceny VALUES (2,1, 3.5, '20 styczen')"
# db.execute(query)
# query = "INSERT INTO oceny VALUES (3,4, 2, '20 styczen')"
# db.execute(query)
#
# sql.commit()

# query = "CREATE VIEW v_studenci_przedmioty(id_studenta, nazwisko, id_przedmiotu, nazwa)"
# #db.execute(query)

# query = "SELECT * FROM studenci"
# z = db.execute(query)
# print(z.fetchall())
#
# query = "SELECT * FROM oceny"
# z = db.execute(query)
# print(z.fetchall())
#
query = "SELECT rowid, nazwa FROM przedmioty"
z = db.execute(query)
print(z.fetchall())
#
# query = "SELECT * FROM studenci_przedmioty"
# z = db.execute(query)
# print(z.fetchall())
#
# query = "SELECT rowid, nazwisko FROM studenci"
# z = db.execute(query)
# print(z.fetchall())
#
# query = "SELECT * FROM przedmioty"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT s.nazwisko, s.imie, s.rowid, p.nazwa, p.rowid FROM studenci s, przedmioty p, studenci_przedmioty WHERE s.rowid=studenci_przedmioty.id_studenta AND " \
#         "p.rowid=studenci_przedmioty.id_przedmiotu ORDER BY p.rowid DESC"
# z = db.execute(query)
# print(z.fetchall())

#query = "SELECT AVG(ocena) FROM oceny WHERE id_przedmiotu=1 OR id_przedmiotu=2"
# query = "SELECT AVG(ocena) FROM oceny WHERE id_przedmiotu IN (SELECT rowid FROM przedmioty WHERE nazwa IN ('informatyka','matematyka'))"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT AVG(o.ocena) FROM oceny o JOIN studenci s ON o.id_studenta=s.rowid"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT AVG(o.ocena) FROM oceny o JOIN przedmioty p ON o.id_przedmiotu=p.rowid AND p.rowid IN (1)"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT AVG(o.ocena) FROM oceny o JOIN przedmioty p ON o.id_przedmiotu=p.rowid AND p.rowid IN " \
#         "(SELECT rowid FROM przedmioty WHERE nazwa IN ('informatyka','matematyka'))"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT AVG(ocena), id_przedmiotu FROM oceny GROUP BY 2 ORDER BY 1 DESC"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT AVG(o.ocena), p.nazwa FROM oceny o JOIN przedmioty p ON o.id_przedmiotu=p.rowid GROUP BY 2 ORDER BY 1 DESC"
# z = db.execute(query)
# print(z.fetchall())

#1) średnia per przedmiot per student
# przedmiot nazwisko średnia
query = "SELECT nazwa, nazwisko, AVG(ocena) FROM oceny o JOIN przedmioty p, studenci s ON o.id_przedmiotu=p.rowid AND o.id_studenta=s.rowid GROUP BY 1, 2 ORDER BY 1"
z = db.execute(query)
print(z.fetchall())


#2)Wstawienie oceny po nazwisku (python)podzapytania
#Insert into oceny where nazwisko = nowak



#HAVING - group by na wynikach
