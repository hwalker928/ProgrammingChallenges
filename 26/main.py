import sqlite3
from datetime import date



def menu():
    while True:
        print("================")
        print("Password Manager")
        print("================")
        print("1) Add password")
        print("2) Lookup password")
        menuOption = input("Enter option: ")
        if menuOption == str(1):
            website = input("\nEnter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            with sqlite3.connect('26/passwords.db') as db:
                db.execute(f"INSERT INTO passwords VALUES ('{website}', '{username}', '{password}', '{d1}')")
                db.commit()
            print("\nSuccessfully added.")
            break
        elif menuOption == "2":
            website = input("\nEnter website: ")
            conn = sqlite3.connect('26/passwords.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM passwords")
            exists = False
            rows = cur.fetchall()
            for row in rows:
                if str(website) in row:
                    exists = True
            if exists:
                print(f"\nUsername: {row[1]}\nPassword: {row[2]}\nDate created: {row[3]}")
            break
        else:
            print("Invalid option!")
            break

menu()