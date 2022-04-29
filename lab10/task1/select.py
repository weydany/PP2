

from config import con, cursor

cursor.execute(f"""
    SELECT * FROM phonebook
    WHERE username = 'decode';
""")

data = cursor.fetchall()

print(data)