import psycopg2

def create_db():
    print("Создание базы данных")
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1", host="localhost", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE DATABASE "Asic"')
        print("База данных создана")
    except psycopg2.errors.DuplicateDatabase:
        print("База данных 'API' уже существует.")
    finally:
        cursor.close()
        conn.close()

def create_table():
    conn = psycopg2.connect(dbname="Asic", user="postgres", password="1", host="localhost", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    create_bot_status_table = '''
        CREATE TABLE IF NOT EXISTS bot_status (
        id INT,
        status INT
        )'''
    print("Создание таблицы статуса бота")
    cursor.execute(create_bot_status_table)
    print("Таблица статуса бота создана")
    cursor.close()
    conn.close()

create_db()
create_table()
