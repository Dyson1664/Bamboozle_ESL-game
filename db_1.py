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
    # Unit 0
    ('Look1', 0, 'one', 1),
    ('Look1', 0, 'two', 2),
    ('Look1', 0, 'three', 3),
    ('Look1', 0, 'four', 4),
    ('Look1', 0, 'five', 5),
    ('Look1', 0, 'six', 6),
    ('Look1', 0, 'seven', 7),
    ('Look1', 0, 'eight', 8),
    ('Look1', 0, 'nine', 9),
    ('Look1', 0, 'ten', 10),
    ('Look1', 0, 'black', 11),
    ('Look1', 0, 'blue', 12),
    ('Look1', 0, 'brown', 13),
    ('Look1', 0, 'green', 14),
    ('Look1', 0, 'orange', 15),
    ('Look1', 0, 'purple', 16),
    ('Look1', 0, 'red', 17),
    ('Look1', 0, 'white', 18),
    ('Look1', 0, 'yellow', 19),
    # Unit 1
    ('Look1', 1, 'bag', 20),
    ('Look1', 1, 'book', 21),
    ('Look1', 1, 'crayon', 22),
    ('Look1', 1, 'eraser', 23),
    ('Look1', 1, 'pen', 24),
    ('Look1', 1, 'pencil', 25),
    ('Look1', 1, 'pencil case', 26),
    ('Look1', 1, 'ruler', 27),
    ('Look1', 1, 'poster', 28),
    ('Look1', 1, 'board', 29),
    ('Look1', 1, 'chair', 30),
    ('Look1', 1, 'desk', 31),
    ('Look1', 1, 'apple', 32),
    ('Look1', 1, 'carrot', 33),
    # Unit 2
    ('Look1', 2, 'ball', 34),
    ('Look1', 2, 'bat', 35),
    ('Look1', 2, 'doll', 36),
    ('Look1', 2, 'game', 37),
    ('Look1', 2, 'kite', 38),
    ('Look1', 2, 'plane', 39),
    ('Look1', 2, 'teddy bear', 40),
    ('Look1', 2, 'train', 41),
    ('Look1', 2, 'marble', 42),
    ('Look1', 2, 'favorite', 43),
    ('Look1', 2, 'fun', 44),
    ('Look1', 2, 'elephant', 45),
    ('Look1', 2, 'fish', 46),
    ('Look1', 2, 'goat', 47),
    ('Look1', 2, 'horse', 48),
    # Unit 3
    ('Look1', 3, 'boy', 49),
    ('Look1', 3, 'girl', 50),
    ('Look1', 3, 'man', 51),
    ('Look1', 3, 'woman', 52),
    ('Look1', 3, 'museum', 53),
    ('Look1', 3, 'dinosaur', 54),
    ('Look1', 3, 'trip', 55),
    ('Look1', 3, 'insect', 56),
    ('Look1', 3, 'jellyfish', 57),
    ('Look1', 3, 'kiwi', 58),
    ('Look1', 3, 'lamp', 59),
    # Unit 4
    ('Look1', 4, 'grandpa', 60),
    ('Look1', 4, 'grandma', 61),
    ('Look1', 4, 'dad', 62),
    ('Look1', 4, 'mom', 63),
    ('Look1', 4, 'uncle', 64),
    ('Look1', 4, 'aunt', 65),
    ('Look1', 4, 'baby', 66),
    ('Look1', 4, 'me', 67),
    ('Look1', 4, 'cousin', 68),
    ('Look1', 4, 'middle', 69),
    ('Look1', 4, 'birthday party', 70),
    ('Look1', 4, 'birthday cake', 71),
    ('Look1', 4, 'nose', 72),
    ('Look1', 4, 'orange', 73),
    # Unit 5
    ('Look1', 5, 'leg', 74),
    ('Look1', 5, 'foot', 75),
    ('Look1', 5, 'mouth', 76),
    ('Look1', 5, 'eye', 77),
    ('Look1', 5, 'head', 78),
    ('Look1', 5, 'ear', 79),
    ('Look1', 5, 'arm', 80),
    ('Look1', 5, 'hand', 81),
    ('Look1', 5, 'skeleton', 82),
    ('Look1', 5, 'hair', 83),
    ('Look1', 5, 'body', 84),
    ('Look1', 5, 'face', 85),
    ('Look1', 5, 'queen', 86),
    ('Look1', 5, 'rabbit', 87),
    ('Look1', 5, 'sofa', 88),
    ('Look1', 5, 'table', 89),
    ('Look1', 5, 'umbrella', 90),
    # Unit 6
    ('Look1', 6, 'bathroom', 91),
    ('Look1', 6, 'bedroom', 92),
    ('Look1', 6, 'kitchen', 93),
    ('Look1', 6, 'living room', 94),
    ('Look1', 6, 'bed', 95),
    ('Look1', 6, 'cabinet', 96),
    ('Look1', 6, 'shower', 97),
    ('Look1', 6, 'TV', 98),
    ('Look1', 6, 'house', 99),
    ('Look1', 6, 'clock', 100),
    ('Look1', 6, 'water', 101),
    ('Look1', 6, 'violin', 102),
    ('Look1', 6, 'wall', 103),
    ('Look1', 6, 'box', 104),
    ('Look1', 6, 'yogurt', 105),
    ('Look1', 6, 'zebra', 106),
    # Unit 7
    ('Look1', 7, 'library', 107),
    ('Look1', 7, 'park', 108),
    ('Look1', 7, 'playground', 109),
    ('Look1', 7, 'store', 110),
    ('Look1', 7, 'street', 111),
    ('Look1', 7, 'swimming pool', 112),
    ('Look1', 7, 'town center', 113),
    ('Look1', 7, 'zoo', 114),
    ('Look1', 7, 'real', 115),
    ('Look1', 7, 'model', 116),
    ('Look1', 7, 'tiny', 117),
    ('Look1', 7, 'flower', 118),
    ('Look1', 7, 'jam', 119),
    ('Look1', 7, 'map', 120),
    # Unit 8
    ('Look1', 8, 'bee', 121),
    ('Look1', 8, 'bird', 122),
    ('Look1', 8, 'chicken', 123),
    ('Look1', 8, 'cow', 124),
    ('Look1', 8, 'dog', 125),
    ('Look1', 8, 'donkey', 126),
    ('Look1', 8, 'duck', 127),
    ('Look1', 8, 'sheep', 128),
    ('Look1', 8, 'pen', 129),
    ('Look1', 8, 'farmer', 130),
    ('Look1', 8, 'food', 131),
    ('Look1', 8, 'eleven', 132),
    ('Look1', 8, 'twelve', 133),
    ('Look1', 8, 'thirteen', 134),
    ('Look1', 8, 'fourteen', 135),
    ('Look1', 8, 'fifteen', 136),
    ('Look1', 8, 'sixteen', 137),
    ('Look1', 8, 'seventeen', 138),
    ('Look1', 8, 'eighteen', 139),
    ('Look1', 8, 'nineteen', 140),
    ('Look1', 8, 'twenty', 141),
    ('Look1', 8, 'bed', 95),
    ('Look1', 8, 'leg', 80),
    ('Look1', 8, 'pen', 24),
    ('Look1', 8, 'pet', 142),
    ('Look1', 8, 'yes', 143),
    ('Look1', 9, 'dress', 144),
    ('Look1', 9, 'jeans', 145),
    ('Look1', 9, 'pants', 146),
    ('Look1', 9, 'shirt', 147),
    ('Look1', 9, 'shoes', 148),
    ('Look1', 9, 'skirt', 149),
    ('Look1', 9, 'socks', 150),
    ('Look1', 9, 'T-shirt', 151),
    ('Look1', 9, 'scarecrow', 152),
    ('Look1', 9, 'happy', 153),
    ('Look1', 9, 'boots', 154),
    ('Look1', 9, 'hat', 155),
    ('Look1', 9, 'gloves', 156),
    ('Look1', 9, 'big', 157),
    ('Look1', 9, 'bin', 158),
    ('Look1', 9, 'lip', 159),
    ('Look1', 9, 'sit', 160),
    ('Look1', 9, 'six', 6),
    ('Look1', 10, 'banana', 161),
    ('Look1', 10, 'bread', 162),
    ('Look1', 10, 'candy', 163),
    ('Look1', 10, 'lemon', 164),
    ('Look1', 10, 'milk', 165),
    ('Look1', 10, 'potato', 166),
    ('Look1', 10, 'rice', 167),
    ('Look1', 10, 'tomato', 168),
    ('Look1', 10, 'water', 101),
    ('Look1', 10, 'lunch', 169),
    ('Look1', 10, 'tray', 170),
    ('Look1', 10, 'terrible', 171),
    ('Look1', 10, 'great', 172),
    ('Look1', 10, 'dog', 125),
    ('Look1', 10, 'dot', 173),
    ('Look1', 10, 'fox', 174),
    ('Look1', 10, 'mop', 175),
    ('Look1', 10, 'nod', 176),
    ('Look1', 11, 'beach', 177),
    ('Look1', 11, 'beach ball', 178),
    ('Look1', 11, 'boat', 179),
    ('Look1', 11, 'ice cream', 180),
    ('Look1', 11, 'ocean', 181),
    ('Look1', 11, 'sand', 182),
    ('Look1', 11, 'sandcastle', 183),
    ('Look1', 11, 'shell', 184),
    ('Look1', 11, 'sun hat', 185),
    ('Look1', 11, 'mask', 186),
    ('Look1', 11, 'breathe', 187),
    ('Look1', 11, 'snorkel', 188),
    ('Look1', 11, 'flippers', 189),
    ('Look1', 11, 'bug', 190),
    ('Look1', 11, 'bus', 191),
    ('Look1', 11, 'cup', 192),
    ('Look1', 11, 'jug', 193),
    ('Look1', 11, 'run', 194),
    ('Look1', 12, 'fly a kite', 195),
    ('Look1', 12, 'make a cake', 196),
    ('Look1', 12, 'paint a picture', 197),
    ('Look1', 12, 'play a game', 198),
    ('Look1', 12, 'play soccer', 199),
    ('Look1', 12, 'read a book', 200),
    ('Look1', 12, 'sing a song', 201),
    ('Look1', 12, 'write a story', 202),
    ('Look1', 12, 'hot', 203),
    ('Look1', 12, 'paper', 204),
    ('Look1', 12, 'swing', 205),
    ('Look1', 12, 'hat', 155),
    ('Look1', 12, 'red', 17),
    ('Look1', 12, 'kid', 206),
    ('Look1', 12, 'sun', 207)
    ]

list101 = []
for v in vocab_entries:
    list101.append(v[:3])




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

    print(list1)
    print(title)
    return title, list1

# get_vocab('Look1', 2)

if __name__ == '__main__':
    create_db()  # Create the database and tables
    insert_vocab(list101)  # Insert initial vocabulary entries
    remove_duplicates()  # Optionally remove duplicates if needed