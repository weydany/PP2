import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    database = 'kbtu',
    user = 'postgres',
    password = '123'
)
print('DB connected!')

cursor = con.cursor()