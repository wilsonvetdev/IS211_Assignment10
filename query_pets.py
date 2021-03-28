import sqlite3 as lite 

user_input = input(f'Provide an id --> ')
con = lite.connect('pets.db')

with con: 
    cur = con.cursor()
    
    cur.execute('SELECT * FROM person WHERE Id=:Id', {'Id': user_input})

    row = cur.fetchone()

    print(row)

    cur.execute('''
    SELECT * 
    FROM pet 
    JOIN person_pet ON pet.id = person_pet.pet_id
    WHERE person_pet.person_id = :Id
    ''', {'Id': user_input})

    print(cur.fetchall())