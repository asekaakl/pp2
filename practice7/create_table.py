from connect import get_connection


def create_table():
    conn = get_connection()
    if not conn:
        return

    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS contacts;
        CREATE TABLE contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица создана!")


if __name__ == '__main__':
    create_table()