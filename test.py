import sqlite3

def test_db():
    try:
        conn = sqlite3.connect('vocabulary.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables in the database:", tables)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

test_db()

def create_database(vocab):
    conn = sqlite3.connect('vocabulary.db2')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS vocab (
        id INTEGER PRIMARY KEY,
        book TEXT NOT NULL,
        unit INTEGER NOT NULL,
        word TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()


def enter_vocab_to_database(vocab):
    with sqlite3.connect('vocabulary.db2') as conn:
        cursor = conn.cursor()
        insert_query = 'INSERT INTO vocab (book, unit, word) Values (?, ?, ?)'
        cursor.executemany(insert_query, (vocab))
        conn.commit()






