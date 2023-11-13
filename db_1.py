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
    ('Look3', 1, 'the US'),
    ('Look3', 1, 'Brazil'),
    ('Look3', 1, 'Argentina'),
    ('Look3', 1, 'the UK'),
    ('Look3', 1, 'Spain'),
    ('Look3', 1, 'Poland'),
    ('Look3', 1, 'Italy'),
    ('Look3', 1, 'Japan'),
    ('Look3', 1, 'South Africa'),
    ('Look3', 1, 'Australia'),
    ('Look3', 1, 'son'),
    ('Look3', 1, 'daughter'),
    ('Look3', 1, 'parent'),
    ('Look3', 1, 'grandparent'),
    ('Look3', 1, 'plane'),
    ('Look3', 1, 'game'),
    ('Look3', 1, 'train'),
    ('Look3', 1, 'paint'),
    ('Look3', 1, 'play'),
    ('Look3', 1, 'Friday'),
    ('Look3', 2, 'farm'),
    ('Look3', 2, 'field'),
    ('Look3', 2, 'forest'),
    ('Look3', 2, 'lake'),
    ('Look3', 2, 'mountain'),
    ('Look3', 2, 'path'),
    ('Look3', 2, 'river'),
    ('Look3', 2, 'town'),
    ('Look3', 2, 'village'),
    ('Look3', 2, 'waterfall'),
    ('Look3', 2, 'cable car'),
    ('Look3', 2, 'subway'),
    ('Look3', 2, 'exercise'),
    ('Look3', 2, 'tree'),
    ('Look3', 2, 'beach'),
    ('Look3', 2, 'country'),
    ('Look3', 2, 'week'),
    ('Look3', 2, 'please'),
    ('Look3', 2, 'story'),
    ('Look3', 3, 'clean up my bedroom'),
    ('Look3', 3, 'cook'),
    ('Look3', 3, 'feed the dog'),
    ('Look3', 3, 'fix my bike'),
    ('Look3', 3, 'go shopping'),
    ('Look3', 3, 'make my bed'),
    ('Look3', 3, 'practice the piano'),
    ('Look3', 3, 'take out the garbage'),
    ('Look3', 3, 'wash the dishes'),
    ('Look3', 3, 'water the plants'),
    ('Look3', 3, 'pick (fruit)'),
    ('Look3', 3, 'recycling'),
    ('Look3', 3, 'put away'),
    ('Look3', 3, 'night'),
    ('Look3', 3, 'right'),
    ('Look3', 3, 'my kite'),
    ('Look3', 3, 'fly'),
    ('Look3', 3, 'ride'),
    ('Look3', 4, 'bake'),
    ('Look3', 4, 'collect stickers'),
    ('Look3', 4, 'do puzzles'),
    ('Look3', 4, 'dress up'),
    ('Look3', 4, 'make things'),
    ('Look3', 4, 'play video games'),
    ('Look3', 4, 'play hide-and-seek'),
    ('Look3', 4, 'read comic books'),
    ('Look3', 4, 'roller-skate'),
    ('Look3', 4, 'watch movies'),
    ('Look3', 4, 'stick'),
    ('Look3', 4, 'teenagers'),
    ('Look3', 4, 'interested in'),
    ('Look3', 4, 'real'),
    ('Look3', 4, 'window'),
    ('Look3', 4, 'know'),
    ('Look3', 4, 'coat'),
    ('Look3', 4, 'home'),
    ('Look3', 4, 'closed'),
    ('Look3', 5, 'ketchup'),
    ('Look3', 5, 'milkshakes'),
    ('Look3', 5, 'noodles'),
    ('Look3', 5, 'pancakes'),
    ('Look3', 5, 'pasta'),
    ('Look3', 5, 'salad'),
    ('Look3', 5, 'sandwiches'),
    ('Look3', 5, 'soup'),
    ('Look3', 5, 'vegetables'),
    ('Look3', 5, 'cup'),
    ('Look3', 5, 'plate'),
    ('Look3', 5, 'bowl'),
    ('Look3', 5, 'straw'),
    ('Look3', 5, 'bottle'),
    ('Look3', 5, 'glass'),
    ('Look3', 5, 'choose'),
    ('Look3', 5, 'blue'),
    ('Look3', 5, 'Tuesday'),
    ('Look3', 5, 'ruler'),
    ('Look3', 5, 'huge'),
    ('Look3', 6, 'ant'),
    ('Look3', 6, 'bat'),
    ('Look3', 6, 'dolphin'),
    ('Look3', 6, 'kangaroo'),
    ('Look3', 6, 'panda'),
    ('Look3', 6, 'parrot'),
    ('Look3', 6, 'penguin'),
    ('Look3', 6, 'shark'),
    ('Look3', 6, 'whale'),
    ('Look3', 6, 'waking up'),
    ('Look3', 6, 'busy'),
    ('Look3', 6, 'lizard'),
    ('Look3', 6, 'hungry'),
    ('Look3', 6, 'safe'),
    ('Look3', 6, 'elephant'),
    ('Look3', 6, 'photo'),
    ('Look3', 6, 'fish'),
    ('Look3', 6, 'fruit'),
    ('Look3', 6, 'breakfast'),
    ('Look3', 7, 'a beard'),
    ('Look3', 7, 'a moustache'),
    ('Look3', 7, 'dark hair'),
    ('Look3', 7, 'light hair'),
    ('Look3', 7, 'curly hair'),
    ('Look3', 7, 'straight hair'),
    ('Look3', 7, 'fat'),
    ('Look3', 7, 'thin'),
    ('Look3', 7, 'tall'),
    ('Look3', 7, 'round face'),
    ('Look3', 7, 'meter'),
    ('Look3', 7, 'take (two hours)'),
    ('Look3', 7, 'die'),
    ('Look3', 7, 'almost'),
    ('Look3', 7, 'birthday'),
    ('Look3', 7, 'dirty'),
    ('Look3', 7, 'short'),
    ('Look3', 7, 'morning'),
    ('Look3', 7, 'dark'),
    ('Look3', 7, 'car'),
    ('Look3', 8, 'back'),
    ('Look3', 8, 'shoulder'),
    ('Look3', 8, 'stomach'),
    ('Look3', 8, 'tooth (teeth)'),
    ('Look3', 8, 'a cold'),
    ('Look3', 8, 'a cough'),
    ('Look3', 8, 'a sore neck'),
    ('Look3', 8, 'sick'),
    ('Look3', 8, 'toothache'),
    ('Look3', 8, 'medicine'),
    ('Look3', 8, 'calm'),
    ('Look3', 8, 'worry'),
    ('Look3', 8, 'grade'),
    ('Look3', 8, 'now'),
    ('Look3', 8, 'down'),
    ('Look3', 8, 'bounce'),
    ('Look3', 8, 'playground'),
    ('Look3', 9, 'building'),
    ('Look3', 9, 'bus stop'),
    ('Look3', 9, 'café'),
    ('Look3', 9, 'hospital'),
    ('Look3', 9, 'market'),
    ('Look3', 9, 'movie theater'),
    ('Look3', 9, 'parking lot'),
    ('Look3', 9, 'sports center'),
    ('Look3', 9, 'supermarket'),
    ('Look3', 9, 'skyscraper'),
    ('Look3', 9, 'factory'),
    ('Look3', 9, 'shopping center'),
    ('Look3', 9, 'birthday'),
    ('Look3', 9, 'burger'),
    ('Look3', 9, 'world'),
    ('Look3', 9, 'person'),
    ('Look3', 10, 'bike to school'),
    ('Look3', 10, 'climb trees'),
    ('Look3', 10, 'cry'),
    ('Look3', 10, 'laugh'),
    ('Look3', 10, 'need water'),
    ('Look3', 10, 'sail'),
    ('Look3', 10, 'stay home'),
    ('Look3', 10, 'wait for the bus'),
    ('Look3', 10, 'walk to school'),
    ('Look3', 10, 'archaeologist'),
    ('Look3', 10, 'machine'),
    ('Look3', 10, 'remains'),
    ('Look3', 10, 'change'),
    ('Look3', 10, 'air'),
    ('Look3', 10, 'hair'),
    ('Look3', 10, 'square'),
    ('Look3', 10, 'parent'),
    ('Look3', 10, 'bear'),
    ('Look3', 10, 'wear'),
    ('Look3', 11, 'eat outside'),
    ('Look3', 11, 'get lost'),
    ('Look3', 11, 'go canoeing'),
    ('Look3', 11, 'go on a roller coaster'),
    ('Look3', 11, 'have a picnic'),
    ('Look3', 11, 'make friends'),
    ('Look3', 11, 'ride on a motorcycle'),
    ('Look3', 11, 'see a shooting star'),
    ('Look3', 11, 'sleep in a tent'),
    ('Look3', 11, 'swim in a lake'),
    ('Look3', 11, 'ski'),
    ('Look3', 11, 'sled'),
    ('Look3', 11, 'explorer'),
    ('Look3', 11, 'face'),
    ('Look3', 11, 'pencil'),
    ('Look3', 11, 'huge'),
    ('Look3', 11, 'giraffe'),
    ('Look3', 12, 'art gallery'),
    ('Look3', 12, 'dinosaur'),
    ('Look3', 12, 'fair'),
    ('Look3', 12, 'museum'),
    ('Look3', 12, 'ride'),
    ('Look3', 12, 'sculpture'),
    ('Look3', 12, 'summer camp'),
    ('Look3', 12, 'theme park'),
    ('Look3', 12, 'water park'),
    ('Look3', 12, 'wildlife park'),
    ('Look3', 12, 'chef'),
    ('Look3', 12, 'star'),
    ('Look3', 12, 'circus'),
    ('Look3', 12, 'juggle'),
    ('Look3', 12, 'skill'),
    ('Look3', 12, 'unicycle'),
    ('Look3', 12, 'summer'),
    ('Look3', 12, 'kangaroo'),
    ('Look3', 12, 'holiday'),
    ('Look3', 12, 'banana'),
    ('Look3', 12, 'waterfall'),
    ('Look3', 12, 'travel'),
]

#
# list101 = []
# for v in vocab_entries:
#     list101.append(v[:3])




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




# create_db()
# insert_vocab(vocab_entries)
# remove_duplicates()
# #
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

    print(', '.join(list1))
    print(title)
    return title, list1



if __name__ == '__main__':
    # create_db()  # Create the database and tables
    # insert_vocab(vocab_entries)  # Insert initial vocabulary entries
    # remove_duplicates()  # Optionally remove duplicates if needed
    get_vocab('Look2', 6)