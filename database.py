import sqlite3

def create_db():
#connect to or creat db
    conn = sqlite3.connect('vocabulary.db')
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



def insert_vocab(book, unit, word):
    with sqlite3.connect('vocabulary.db') as conn:
        cursor = conn.cursor()
        insert_query = 'INSERT INTO vocab (book, unit, word) Values (?, ?, ?)'
        cursor.execute(insert_query, (book, unit, word))
        conn.commit()



create_db()
#need to add insert as tuples (book, unit, word)