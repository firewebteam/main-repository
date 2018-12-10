import sqlite3
sql = sqlite3.connect("db2.sql")
db = sql.cursor()

query = "CREATE TABLE telefony (id int, nazwisko text, imie text, numer int)"
#db.execute(query)
query = "INSERT INTO telefony (id, nazwisko, imie, numer) VALUES (1,'Szatam', 'Stefan', 666)"
#db.execute(query)
#query = "INSERT INTO telefony (id, nazwisko, imie, numer) VALUES (2,'Kowalski', 'Tomasz', 541)"
#db.execute(query)
#query = "INSERT INTO telefony (id, nazwisko, imie, numer) VALUES (3,'Dyzurny', 'Oficer', 534)"
#db.execute(query)
sql.commit()

query = "CREATE TABLE studenci(indeks int, imie varchar(20), nazwisko xarchar(20), odznaka int)"
#.execute(query)
query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (1,'Kowalski', 'Stefan', 666)"
query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (2,'Kowalski', 'Arkadiusz', 12)"
query = "INSERT INTO studenci (indeks, imie, nazwisko, odznaka) VALUES (1,'Nowak', 'Maciej', 666)"
#db.execute(query)
sql.commit()
query = "SELECT * FROM studenci"
#db.execute(query)
z = db.execute(query)
print(z.fetchall())

query = "SELECT * FROM studenci WHERE imie LIKE 'kow%' "
Z = db.execute(query)
print(z.fetchall())

query = "DROP TABLE studenci" #usuwa tabelę
query = "ALTER TABLE studenci ADD COLUMN wysoki" #dodaje kolumnę do tabeli
query = "ALTER TABLE studenci ADD COLUMN wysoki"
query = "SELECT s.nazwisko, s.imie, s.rowid, p.nazwa, p.rowid FROM studenci s, przedmioty p WHERE s.rowid=2"

query = "SELECT s.nazwisko, s.imie, s.rowid, p.nazwa, p.rowid FROM studenci s, przedmioty p WHERE s.rowid=studenci_przedmioty.id_studenta AND" \
        "p.rowid=studenci_przedmioty.id_przedmiotu AND s.rowid=2 ORDER BY p.rowid DESC"