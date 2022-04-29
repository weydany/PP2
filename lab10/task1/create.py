from config import con, cursor

cursor.execute('''
    CREATE TABLE phonebook(
        username VARCHAR(100) UNIQUE,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone_number INT UNIQUE
    );
''')

con.commit()