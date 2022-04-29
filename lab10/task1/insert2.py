
from config import con, cursor

username = input('Enter your username: ')
phone_num = int(input('Enter your phone number: '))
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

cursor.execute(f"""
    INSERT INTO phonebook (username, first_name, last_name, phone_number)
    VALUES ('{username}', '{first_name}', '{last_name}', {phone_num})
""")

con.commit()

print('Data inserted successfully!')