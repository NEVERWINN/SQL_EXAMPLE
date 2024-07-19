import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path) #осуществляет связь между фактическ.базой данных и кодом
        print("connection success.")
        return connection
    except Error as e:
        print(f'Error {e} is occured.')

def add_data(path):
    cursor = connection.cursor() #объект который позволяет совершать запросы в базе
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER
    );
    ''')
    cursor.execute("INSERT INTO  Users (name, surname, age) VALUES (?, ?, ?)", ('Dima', 'Ivanov', 25))
    cursor.execute("UPDATE Users SET age = ? WHERE name = ?", (26, 'Dima'))
    #cursor.execute("DELETE FROM Users WHERE name = ?", ('Dima',))
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    print(users)
    connection.commit()
    print("changes comitted")
    connection.close()



connection = create_connection("server.sqlite")
add_data(connection)


