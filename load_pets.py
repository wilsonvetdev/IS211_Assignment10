import sqlite3 as lite 

people = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
)

pets = ( 
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)

if __name__ == '__main__':

    con = lite.connect('pets.db')

    with con:
        cur = con.cursor()

        cur.executescript('''
        DROP TABLE IF EXISTS person;
        DROP TABLE IF EXISTS pet;
        DROP TABLE IF EXISTS person_pet;
        CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER);
        CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER);
        CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER);
        ''')

        cur.executemany('INSERT INTO person VALUES(?, ?, ?, ?)', people)
        cur.executemany('INSERT INTO pet VALUES(?, ?, ?, ?, ?)', pets)
        cur.executemany('INSERT INTO person_pet VALUES(?, ?)', person_pet)
