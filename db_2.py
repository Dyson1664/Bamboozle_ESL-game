import sqlite3

def create_db():
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    create_table = '''
    CREATE TABLE IF NOT EXISTS summer_clothes (
    id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    amount INTEGER NOT NULL,
    colour TEXT NOT NULL
    );
    '''
    cursor.execute(create_table)
    conn.commit()


def enter_data(entries):
    with sqlite3.connect('clothes.db') as conn:
        cursor = conn.cursor()
        insert_into = 'INSERT INTO summer_clothes (item, amount, colour) VALUES (?, ?, ?)'
        cursor.executemany(insert_into, (entries))
        conn.commit()


entries = [('t-shirt', 5, 'blue'),
            ('hat', 2, 'red'),
            ('shorts', 1, 'blue')]


def get_data(colour):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    query = 'SELECT * FROM summer_clothes WHERE colour=?'
    cursor.execute(query, (colour,))

    results = cursor.fetchall()
    cursor.close()
    cursor.close()
    for item in results:
        print(item)
        print(f'Item: {item[1]} is {colour} and there are {item[2]} in db')
    # print(f'item: {item}, amount: {amount}')
    # print(f'colour: {"".join(results[0])}')

get_data('blue')






# create_db()
# enter_data(entries)




