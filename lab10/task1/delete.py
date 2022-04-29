
from config import con, cursor

choose = int(input('1) Delete by username\n2) Delete by phone_number\nYour choose: '))

if choose == 1:
    usernmae = input('Enter your username: ')
    cursor.execute(f"""
        DELETE FROM phonebook
        WHERE username = '{usernmae}';
    """)

elif choose == 2:
    phone = int(input('Enter your phone number: '))
    cursor.execute(f"""
        DELETE FROM phonebook
        WHERE phone_number = {phone};
    """)

print('Your data deleted successfully!')
con.commit()