
from config import con, cursor

username = input('Enter your username: ')
new_name = input('Enter your new name: ')

cursor.execute(f"""
    UPDATE phonebook
    SET first_name = '{new_name}'
    WHERE username = '{username}';
""")

con.commit()

print('Your first name changed successfully!')