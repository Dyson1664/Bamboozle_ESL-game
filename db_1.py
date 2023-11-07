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



def insert_vocab(entries):
    with sqlite3.connect('vocabulary.db') as conn:
        cursor = conn.cursor()
        insert_query = 'INSERT INTO vocab (book, unit, word) Values (?, ?, ?)'
        cursor.executemany(insert_query, (entries))
        conn.commit()

vocab_entries = [
    ('Look2', 1, 'art'),
    ('Look2', 1, 'computers'),
    ('Look2', 1, 'English'),
    ('Look2', 1, 'gym'),
    ('Look2', 1, 'math'),
    ('Look2', 1, 'music'),
    ('Look2', 1, 'reading'),
    ('Look2', 1, 'science'),
    ('Look2', 1, 'class'),
    ('Look2', 1, 'homework'),
    ('Look2', 1, 'grade'),
    ('Look2', 1, 'garden'),
    ('Look2', 1, 'Thursday'),
    ('Look2', 1, 'bath'),
    ('Look2', 1, 'birthday'),
    # Unit 2
    ('Look2', 2, 'bike'),
    ('Look2', 2, 'building bricks'),
    ('Look2', 2, 'camera'),
    ('Look2', 2, 'guitar'),
    ('Look2', 2, 'markers'),
    ('Look2', 2, 'robot'),
    ('Look2', 2, 'skateboard'),
    ('Look2', 2, 'tablet'),
    ('Look2', 2, 'cool'),
    ('Look2', 2, 'old'),
    ('Look2', 2, 'new'),
    ('Look2', 2, 'borrow'),
    ('Look2', 2, 'this'),
    ('Look2', 2, 'these'),
    ('Look2', 2, 'brother'),
    # Unit 3
    ('Look2', 3, 'armchair'),
    ('Look2', 3, 'balcony'),
    ('Look2', 3, 'bookcase'),
    ('Look2', 3, 'dining room'),
    ('Look2', 3, 'door'),
    ('Look2', 3, 'floor'),
    ('Look2', 3, 'mirror'),
    ('Look2', 3, 'rug'),
    ('Look2', 3, 'window'),
    ('Look2', 3, 'inside'),
    ('Look2', 3, 'stairs'),
    ('Look2', 3, 'wall'),
    ('Look2', 3, 'outside'),
    ('Look2', 3, 'chair'),
    ('Look2', 3, 'lunch'),
    ('Look2', 3, 'ship'),
    ('Look2', 3, 'fish'),
    # Unit 4
    ('Look2', 4, 'baseball'),
    ('Look2', 4, 'basketball'),
    ('Look2', 4, 'hockey'),
    ('Look2', 4, 'tennis'),
    ('Look2', 4, 'bounce'),
    ('Look2', 4, 'catch'),
    ('Look2', 4, 'hit'),
    ('Look2', 4, 'jump'),
    ('Look2', 4, 'kick'),
    ('Look2', 4, 'throw'),
    ('Look2', 4, 'team'),
    ('Look2', 4, 'different'),
    ('Look2', 4, 'easy'),
    ('Look2', 4, 'fantastic'),
    ('Look2', 4, 'duck'),
    ('Look2', 4, 'socks'),
    ('Look2', 4, 'sink'),
    ('Look2', 4, 'pink'),
    # Unit 5
    ('Look2', 5, 'builder'),
    ('Look2', 5, 'doctor'),
    ('Look2', 5, 'farmer'),
    ('Look2', 5, 'soccer player'),
    ('Look2', 5, 'taxi driver'),
    ('Look2', 5, 'young'),
    ('Look2', 5, 'work'),
    ('Look2', 5, 'job'),
    ('Look2', 5, 'use'),
    ('Look2', 5, 'skirt'),
    ('Look2', 5, 'slide'),
    ('Look2', 5, 'small'),
    ('Look2', 5, 'snack'),
    ('Look2', 5, 'spoon'),
    ('Look2', 5, 'stop'),
    ('Look2', 5, 'swim'),
    # Unit 6
    ('Look2', 6, 'get up'),
    ('Look2', 6, 'get dressed'),
    ('Look2', 6, 'eat breakfast'),
    ('Look2', 6, 'eat lunch'),
    ('Look2', 6, 'eat dinner'),
    ('Look2', 6, 'do homework'),
    ('Look2', 6, 'take a bath'),
    ('Look2', 6, 'go to bed'),
    ('Look2', 6, 'hurt'),
    ('Look2', 6, 'find'),
    ('Look2', 6, 'wait'),
    ('Look2', 6, 'love'),
    ('Look2', 6, 'black'),
    ('Look2', 6, 'clock'),
    ('Look2', 6, 'flag'),
    ('Look2', 6, 'glass'),
    ('Look2', 6, 'plum'),
    # Unit 7
    ('Look2', 7, 'beans'),
    ('Look2', 7, 'cheese'),
    ('Look2', 7, 'chicken'),
    ('Look2', 7, 'egg'),
    ('Look2', 7, 'fries'),
    ('Look2', 7, 'grapes'),
    ('Look2', 7, 'juice'),
    ('Look2', 7, 'mango'),
    ('Look2', 7, 'pear'),
    ('Look2', 7, 'sausage'),
    ('Look2', 7, 'put'),
    ('Look2', 7, 'money'),
    ('Look2', 7, 'get'),
    ('Look2', 7, 'burger'),
    ('Look2', 7, 'bread'),
    ('Look2', 7, 'crab'),
    ('Look2', 7, 'dress'),
    ('Look2', 7, 'frog'),
    ('Look2', 7, 'present'),
    ('Look2', 7, 'tree'),
    # Unit 8
    ('Look2', 8, 'dance'),
    ('Look2', 8, 'drink'),
    ('Look2', 8, 'eat'),
    ('Look2', 8, 'hold'),
    ('Look2', 8, 'listen to music'),
    ('Look2', 8, 'take photos'),
    ('Look2', 8, 'balloon'),
    ('Look2', 8, 'lemonade'),
    ('Look2', 8, 'festival'),
    ('Look2', 8, 'enjoy'),
    ('Look2', 8, 'bucket'),
    ('Look2', 8, 'sing'),
    ('Look2', 8, 'long'),
    ('Look2', 8, 'angry'),
    # Unit 9
    ('Look2', 9, 'crocodile'),
    ('Look2', 9, 'elephant'),
    ('Look2', 9, 'giraffe'),
    ('Look2', 9, 'hippo'),
    ('Look2', 9, 'lion'),
    ('Look2', 9, 'monkey'),
    ('Look2', 9, 'snake'),
    ('Look2', 9, 'tiger'),
    ('Look2', 9, 'zebra'),
    ('Look2', 9, 'rhino'),
    ('Look2', 9, 'fast'),
    ('Look2', 9, 'slow'),
    ('Look2', 9, 'sleep'),
    ('Look2', 9, 'cake'),
    ('Look2', 9, 'game'),
    # Unit 10
    ('Look2', 10, 'cloudy'),
    ('Look2', 10, 'cold'),
    ('Look2', 10, 'hot'),
    ('Look2', 10, 'raining'),
    ('Look2', 10, 'snowing'),
    ('Look2', 10, 'sunny'),
    ('Look2', 10, 'windy'),
    ('Look2', 10, 'bring an umbrella'),
    ('Look2', 10, 'put on a scarf'),
    ('Look2', 10, 'wear a coat'),
    ('Look2', 10, 'sky'),
    ('Look2', 10, 'rainbow'),
    ('Look2', 10, 'bright'),
    ('Look2', 10, 'forget'),
    ('Look2', 10, 'kite'),
    ('Look2', 10, 'time'),
    # Unit 11
    ('Look2', 11, 'bus'),
    ('Look2', 11, 'car'),
    ('Look2', 11, 'helicopter'),
    ('Look2', 11, 'motorcycle'),
    ('Look2', 11, 'plane'),
    ('Look2', 11, 'ship'),
    ('Look2', 11, 'truck'),
    ('Look2', 11, 'come home'),
    ('Look2', 11, 'get to school'),
    ('Look2', 11, 'ride a bike'),
    ('Look2', 11, 'healthy'),
    ('Look2', 11, 'snack'),
    ('Look2', 11, 'month'),
    ('Look2', 11, 'ready'),
    ('Look2', 11, 'home'),
    ('Look2', 11, 'nose'),
    ('Look2', 11, 'cone'),
    # Unit 12
    ('Look2', 12, 'clean'),
    ('Look2', 12, 'dirty'),
    ('Look2', 12, 'kind'),
    ('Look2', 12, 'little'),
    ('Look2', 12, 'loud'),
    ('Look2', 12, 'naughty'),
    ('Look2', 12, 'quiet'),
    ('Look2', 12, 'scary'),
    ('Look2', 12, 'silly'),
    ('Look2', 12, 'smart'),
    ('Look2', 12, 'funny'),
    ('Look2', 12, 'cartoon'),
    ('Look2', 12, 'grown-up'),
    ('Look2', 12, 'famous'),
    ('Look2', 12, 'cube'),
    ('Look2', 12, 'cute'),
    ('Look2', 12, 'tube'),
    ]


def remove_duplicates():
    with sqlite3.connect('vocabulary.db') as conn:
        cursor = conn.cursor()
        delete_query = '''
        DELETE FROM vocab
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM vocab
            GROUP BY book, unit, word
        )
        '''
        cursor.execute(delete_query)
        conn.commit()


# remove_duplicates()

# create_db()
# insert_vocab(vocab_entries)
#
def get_vocab(book, unit):
    conn = sqlite3.connect('vocabulary.db')
    cursor = conn.cursor()

    query = f"SELECT word FROM vocab WHERE book=? AND unit=?"
    cursor.execute(query, (book, unit))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    title = book + ' Unit ' + str(unit) + ' Vocab'
    list1 = []
    for word in results:
        list1.append(''.join(word))

    print(list1)
    print(title)
    return title, list1

# get_vocab('Look2', 2)

if __name__ == '__main__':
    create_db()  # Create the database and tables
    insert_vocab(vocab_entries)  # Insert initial vocabulary entries
    remove_duplicates()  # Optionally remove duplicates if needed