from config import con, cursor


cursor.execute("""
    insert into users(id, username)
    values (1, 'decode');

    insert into user_score (user_name, score)
    values ('decode', 15);
""")


con.commit()