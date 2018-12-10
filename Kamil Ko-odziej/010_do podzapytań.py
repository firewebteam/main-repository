import sqlite3
sql = sqlite3.connect("kompanie.sql")
db = sql.cursor()

# query = "DROP TABLE studenci"
# db.execute(query)
# query = "CREATE TABLE studenci (id, nazwisko, imie, id_studiów)"
# db.execute(query)
# query = "CREATE TABLE studia (id, studia)"
# db.execute(query)
# query = "CREATE TABLE przedmioty (id, przedmiot)"
# db.execute(query)



# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (1,'Kowalski', 'Hubert', 1)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (2,'Zawistowski', 'Hubert', 1)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (3,'Mackiewicz', 'Mateusz', 1)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (4,'Kamieński', 'Aleksander', 2)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (5,'Puc', 'Damian', 2)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (6,'Kołodziej', 'Kamil', 2)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (7,'Bartkowicz', 'Jakub', 3)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie, id_studiów) VALUES (8,'Kreński', 'Karol', NULL)"
# db.execute(query)
# sql.commit()



# query = "ALTER TABLE studenci RENAME TO s2"
# db.execute(query)
# query = "CREATE TABLE studenci (id, nazwisko, imie)"
# db.execute(query)
# query = "INSERT INTO studenci (id,nazwisko, imie) SELECT id,nazwisko, imie from s2"
# db.execute(query)
# query = "DROP TABLE s2"
# db.execute(query)
# sql.commit()



# query = "INSERT INTO studia (id, studia) VALUES (1,'SP-PK16')"
# db.execute(query)
# query = "INSERT INTO studia (id, studia) VALUES (2,'SP-PK17')"
# db.execute(query)
# query = "INSERT INTO studia (id, studia) VALUES (3,'SP-PK18')"
# db.execute(query)
# sql.commit()



# query = "INSERT INTO przedmioty (id, przedmiot) VALUES (100,'matematyka')"
# db.execute(query)
# query = "INSERT INTO przedmioty (id, przedmiot) VALUES (101,'informatyka')"
# db.execute(query)
# query = "INSERT INTO przedmioty (id, przedmiot) VALUES (102,'fizyka')"
# db.execute(query)
# query = "INSERT INTO przedmioty (id, przedmiot) VALUES (103,'chemia')"
# db.execute(query)
# sql.commit()



# query = "UPDATE studenci SET id=6 WHERE nazwisko='Kołodziej'"
# db.execute(query)
# sql.commit()



# query = "CREATE TABLE studenci_przedmioty (id, id_studenta, id_przedmiotu)"
# db.execute(query)
query = "INSERT INTO studenci_przedmioty (id, id_studenta, id_przedmiotu) VALUES (1,2,102)"
db.execute(query)
query = "INSERT INTO studenci_przedmioty (id, id_studenta, id_przedmiotu) VALUES (2,6,102)"
db.execute(query)
query = "INSERT INTO studenci_przedmioty (id, id_studenta, id_przedmiotu) VALUES (3,1,100)"
db.execute(query)
query = "INSERT INTO studenci_przedmioty (id, id_studenta, id_przedmiotu) VALUES (4,6,100)"
db.execute(query)
query = "INSERT INTO studenci_przedmioty (id, id_studenta, id_przedmiotu) VALUES (5,8,100)"
db.execute(query)
query = "INSERT INTO studenci_przedmioty (id, id_studenta, id_przedmiotu) VALUES (6,8,101)"
db.execute(query)























# query = "CREATE VIEW v_studenci_przedmioty(id_studenta, nazwisko, id_przedmiotu, nazwa)"
# #db.execute(query)

query = "SELECT * FROM studenci ORDER BY id"
z = db.execute(query)
print("studenci",z.fetchall())

query = "SELECT * FROM studia ORDER BY id"
z = db.execute(query)
print("studia",z.fetchall())

query = "SELECT * FROM przedmioty ORDER BY id"
z = db.execute(query)
print("przedmioty",z.fetchall())

query = "SELECT * FROM studenci_przedmioty ORDER BY id"
z = db.execute(query)
print("studenci_przedmioty",z.fetchall())

# query = "SELECT * FROM oceny"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT rowid, nazwa FROM przedmioty"
# z = db.execute(query)
# print(z.fetchall())

# query = "SELECT rowid, nazwisko FROM studenci"
# z = db.execute(query)
# print(z.fetchall())

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
# query = "SELECT nazwa, nazwisko, AVG(ocena) FROM oceny o JOIN przedmioty p, studenci s ON o.id_przedmiotu=p.rowid AND o.id_studenta=s.rowid GROUP BY 1, 2 ORDER BY 1"
# z = db.execute(query)
# print(z.fetchall())


#2)Wstawienie oceny po nazwisku (python)podzapytania
#Insert into oceny where nazwisko = nowak



#HAVING - group by na wynikach
