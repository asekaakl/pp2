import psycopg2
import csv

# Подключение
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="твой_пароль"
    )

# 1. Загрузить из CSV
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (first_name, last_name, phone)
                VALUES (%s, %s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (row['first_name'], row['last_name'], row['phone']))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные из CSV загружены!")

# 2. Добавить вручную с консоли
def insert_from_console():
    first = input("Имя: ")
    last = input("Фамилия: ")
    phone = input("Телефон: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT (phone) DO NOTHING;
    """, (first, last, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Контакт добавлен!")

# 3. Обновить контакт
def update_contact():
    phone = input("Введите телефон контакта для обновления: ")
    print("Что обновить? 1-Имя, 2-Телефон")
    choice = input("Выбор: ")
    conn = connect()
    cur = conn.cursor()
    if choice == '1':
        new_name = input("Новое имя: ")
        cur.execute("UPDATE phonebook SET first_name=%s WHERE phone=%s", (new_name, phone))
    elif choice == '2':
        new_phone = input("Новый телефон: ")
        cur.execute("UPDATE phonebook SET phone=%s WHERE phone=%s", (new_phone, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Контакт обновлён!")

# 4. Поиск / фильтрация
def search_contacts():
    print("Поиск: 1-По имени, 2-По префиксу телефона, 3-Все контакты")
    choice = input("Выбор: ")
    conn = connect()
    cur = conn.cursor()
    if choice == '1':
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f'%{name}%',))
    elif choice == '2':
        prefix = input("Введите префикс телефона (например +7701): ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f'{prefix}%',))
    else:
        cur.execute("SELECT * FROM phonebook ORDER BY first_name;")
    
    rows = cur.fetchall()
    print(f"\n{'ID':<5} {'Имя':<15} {'Фамилия':<15} {'Телефон':<15}")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<15}")
    cur.close()
    conn.close()

# 5. Удалить контакт
def delete_contact():
    print("Удалить: 1-По имени, 2-По телефону")
    choice = input("Выбор: ")
    conn = connect()
    cur = conn.cursor()
    if choice == '1':
        name = input("Введите имя: ")
        cur.execute("DELETE FROM phonebook WHERE first_name ILIKE %s", (f'%{name}%',))
    elif choice == '2':
        phone = input("Введите телефон: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    conn.commit()
    print(f"Удалено записей: {cur.rowcount}")
    cur.close()
    conn.close()

# Главное меню
def menu():
    while True:
        print("\n=== PhoneBook ===")
        print("1. Загрузить из CSV")
        print("2. Добавить вручную")
        print("3. Обновить контакт")
        print("4. Найти контакт")
        print("5. Удалить контакт")
        print("0. Выход")
        choice = input("Выбор: ")

        if choice == '1':
            insert_from_csv('contacts.csv')
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '0':
            break

if __name__ == "__main__":
    menu()