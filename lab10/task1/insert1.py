
from config import con, cursor

file= open('phone_book.csv')
data = file.readlines()
info = data[1:]

for x in info:
    row = x.strip('\n').split(',')
    cursor.execute(f"""
        INSERT INTO phonebook(username, first_name, last_name, phone_number)
        VALUES ('{row[0]}', '{row[2]}', '{row[3]}', {row[1]}) 
    """)
    con.commit()



print('All data from csv inserted successfully!')
file.close()