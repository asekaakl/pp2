import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="asauturlan2007"
)
cur = conn.cursor()

cur.execute("""
    DROP TABLE IF EXISTS phonebook;
    CREATE TABLE phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        phone VARCHAR(20) UNIQUE NOT NULL
    );
""")

conn.commit()
cur.close()
conn.close()
print("Таблица создана!")