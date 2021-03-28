import sqlite3 as lite 
import sys

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

if __name__ == '__main__':

    while True:

        user_input = input(f'Provide an id --> ')

        try:

            con = lite.connect('pets.db')

            with con: 

                cur = con.cursor()
                
                cur.execute('SELECT * FROM person WHERE Id=:Id', {'Id': user_input})
                row = cur.fetchone()

                full_name = f'{row[1]} {row[2]}'
                age = f'{row[3]}' 

                cur.execute('''
                SELECT * 
                FROM pet 
                JOIN person_pet ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = :Id
                ''', {'Id': user_input})

                pets = cur.fetchall()
                print(f'{full_name}, {age} years old.')

                for pet in pets:
                    dead = bool(pet[4])
                    if dead:
                        prGreen(f'{full_name} owned {pet[1]}, a {pet[2]}, that was {pet[3]} years old.')
                    else:
                        prGreen(f'{full_name} currently owns {pet[1]}, a {pet[2]}, that is {pet[3]} years old.')

        except TypeError:
            if int(user_input) == -1:
                sys.exit('Exiting program')
            else:
                prYellow('This person doesn\'t exist.')

