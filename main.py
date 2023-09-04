import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS gta (release_year integer, release_name text, city text)")
release_list = [
  (1997, "Grand Theft Auto", "state of New Guernsey"),
  (1999, "Grand Theft Auto 2", "Anywhere, USA"),
  (2001, " Grand Theft Auto III", "Liberty City"),
  (2002, "Grand Theft Auto: Vice City", "Vice City"),
  (2004, "Grand Theft Auto: San Andreas", "State of San Andreas"),
  (2008, "Grand Theft Auto IV", "Liberty City"),
  (2013, "Grand Theft Auto V", "Los Santos")
]

cursor.executemany("insert into gta values (?,?,?)", release_list)

#print database rows
for row in cursor.execute("select * from gta"):
  print(row)

#print specific rows
print("**************")
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search=cursor.fetchall()
print(gta_search)
connection.close()