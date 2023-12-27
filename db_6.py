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



def create_db2():
    conn = sqlite3.connect('vocabulary.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS kindergarten (
    id INTEGER PRIMARY KEY,
    level TEXT NOT NULL,
    title TEXT NOT NULL,
    vocab TEXT NOT NULL);
    '''

    cursor.execute(create_table_query)
    conn.commit()


def insert_vocab(entries):
    with sqlite3.connect('vocabulary.db') as conn:
        cursor = conn.cursor()
        insert_query = 'INSERT INTO vocab (book, unit, word) Values (?, ?, ?)'
        cursor.executemany(insert_query, (entries))
        conn.commit()


def insert_vocabs2(vocab_entries2):
    with sqlite3.connect('vocabulary.db') as conn:
        cursor = conn.cursor()
        insert_query = 'INSERT INTO kindergarten (level, title, vocab) Values (?, ?, ?)'
        cursor.executemany(insert_query, (vocab_entries2))
        conn.commit()



vocab_entries2 = [
    # Weather
    ('KG', 'Weather', 'Sunny'),
    ('KG', 'Weather', 'Fine'),
    ('KG', 'Weather', 'Cloudy'),
    ('KG', 'Weather', 'Hot'),
    ('KG', 'Weather', 'Cold'),
    ('KG', 'Weather', 'Rainy'),
    ('KG', 'Weather', 'Windy'),
    ('KG', 'Weather', 'Snowy'),
    # Verbs
    ('KG', 'Verbs', 'Eat'),
    ('KG', 'Verbs', 'Write'),
    ('KG', 'Verbs', 'Run'),
    ('KG', 'Verbs', 'Sleep'),
    ('KG', 'Verbs', 'Drink'),
    ('KG', 'Verbs', 'Listen'),
    ('KG', 'Verbs', 'Walk'),
    ('KG', 'Verbs', 'Read'),
    # Verbs2
    ('KG', 'Verbs2', 'Cry'),
    ('KG', 'Verbs2', 'Watch'),
    ('KG', 'Verbs2', 'Swim'),
    ('KG', 'Verbs2', 'Play'),
    ('KG', 'Verbs2', 'Sing'),
    ('KG', 'Verbs2', 'Laugh'),
    ('KG', 'Verbs2', 'Dance'),
    ('KG', 'Verbs2', 'Count'),
    # Vegetables
    ('KG', 'Vegetables', 'Onion'),
    ('KG', 'Vegetables', 'Potato'),
    ('KG', 'Vegetables', 'Mushroom'),
    ('KG', 'Vegetables', 'Tomato'),
    ('KG', 'Vegetables', 'Carrot'),
    ('KG', 'Vegetables', 'Corn'),
    ('KG', 'Vegetables', 'Beans'),
    ('KG', 'Vegetables', 'Cucumber'),
    # Transport
    ('KG', 'Transport', 'Helicopter'),
    ('KG', 'Transport', 'Car'),
    ('KG', 'Transport', 'Bicycle'),
    ('KG', 'Transport', 'Train'),
    ('KG', 'Transport', 'Airplane'),
    ('KG', 'Transport', 'Boat'),
    ('KG', 'Transport', 'Bus'),
    ('KG', 'Transport', 'Motorbike'),
    # Sports
    ('KG', 'Sports', 'Soccer'),
    ('KG', 'Sports', 'Baseball'),
    ('KG', 'Sports', 'Basketball'),
    ('KG', 'Sports', 'Volleyball'),
    ('KG', 'Sports', 'Badminton'),
    ('KG', 'Sports', 'Tennis'),
    ('KG', 'Sports', 'Hockey'),
    ('KG', 'Sports', 'Golf'),
    # Shapes
    ('KG', 'Shapes', 'Triangle'),
    ('KG', 'Shapes', 'Star'),
    ('KG', 'Shapes', 'Circle'),
    ('KG', 'Shapes', 'Oval'),
    ('KG', 'Shapes', 'Diamond'),
    ('KG', 'Shapes', 'Heart'),
    ('KG', 'Shapes', 'Square'),
    ('KG', 'Shapes', 'Rectangle'),
    # Prepositions
    ('KG', 'Prepositions', 'Behind'),
    ('KG', 'Prepositions', 'Next to'),
    ('KG', 'Prepositions', 'Between'),
    ('KG', 'Prepositions', 'In'),
    ('KG', 'Prepositions', 'Above'),
    ('KG', 'Prepositions', 'On'),
    ('KG', 'Prepositions', 'Under'),
    ('KG', 'Prepositions', 'In front of'),
    # Places
    ('KG', 'Places', 'Hospital'),
    ('KG', 'Places', 'School'),
    ('KG', 'Places', 'Airport'),
    ('KG', 'Places', 'Park'),
    ('KG', 'Places', 'Supermarket'),
    ('KG', 'Places', 'Zoo'),
    ('KG', 'Places', 'Bus Stop'),
    ('KG', 'Places', 'Restaurant'),
    # Nature
    ('KG', 'Nature', 'Sun'),
    ('KG', 'Nature', 'Moon'),
    ('KG', 'Nature', 'Stars'),
    ('KG', 'Nature', 'Mountain'),
    ('KG', 'Nature', 'Rainbow'),
    ('KG', 'Nature', 'Flower'),
    ('KG', 'Nature', 'Grass'),
    ('KG', 'Nature', 'Tree'),
    # Nature2
    ('KG', 'Nature2', 'Waterfall'),
    ('KG', 'Nature2', 'Cave'),
    ('KG', 'Nature2', 'Mud'),
    ('KG', 'Nature2', 'Bridge'),
    ('KG', 'Nature2', 'Sand'),
    ('KG', 'Nature2', 'Volcano'),
    ('KG', 'Nature2', 'Hill'),
    ('KG', 'Nature2', 'Path'),
    # Jobs
    ('KG', 'Jobs', 'Teacher'),
    ('KG', 'Jobs', 'Nurse'),
    ('KG', 'Jobs', 'Postman'),
    ('KG', 'Jobs', 'Cook'),
    ('KG', 'Jobs', 'Doctor'),
    ('KG', 'Jobs', 'Student'),
    ('KG', 'Jobs', 'Policeman'),
    ('KG', 'Jobs', 'Fireman'),
    # Insects
    ('KG', 'Insects', 'Ant'),
    ('KG', 'Insects', 'Spider'),
    ('KG', 'Insects', 'Worm'),
    ('KG', 'Insects', 'Ladybug'),
    ('KG', 'Insects', 'Bee'),
    ('KG', 'Insects', 'Mosquito'),
    ('KG', 'Insects', 'Butterfly'),
    ('KG', 'Insects', 'Fly'),
    # House
    ('KG', 'House', 'Garden'),
    ('KG', 'House', 'Kitchen'),
    ('KG', 'House', 'House'),
    ('KG', 'House', 'Bedroom'),
    ('KG', 'House', 'Bathroom'),
    ('KG', 'House', 'Living Room'),
    ('KG', 'House', 'Study'),
    ('KG', 'House', 'Wardrobe'),
    # Fruit
    ('KG', 'Fruit', 'Apple'),
    ('KG', 'Fruit', 'Lemon'),
    ('KG', 'Fruit', 'Orange'),
    ('KG', 'Fruit', 'Strawberry'),
    ('KG', 'Fruit', 'Banana'),
    ('KG', 'Fruit', 'Cherry'),
    ('KG', 'Fruit', 'Pineapple'),
    ('KG', 'Fruit', 'Grapes'),
    # Food
    ('KG', 'Food', 'Salad'),
    ('KG', 'Food', 'Eggs'),
    ('KG', 'Food', 'Rice'),
    ('KG', 'Food', 'Pizza'),
    ('KG', 'Food', 'Chicken'),
    ('KG', 'Food', 'Sandwich'),
    ('KG', 'Food', 'Hamburger'),
    ('KG', 'Food', 'Steak'),
    # Feelings
    ('KG', 'Feelings', 'Hungry'),
    ('KG', 'Feelings', 'Thirsty'),
    ('KG', 'Feelings', 'Tired'),
    ('KG', 'Feelings', 'Sick'),
    ('KG', 'Feelings', 'Happy'),
    ('KG', 'Feelings', 'Sad'),
    # Fantasy
    ('KG', 'Fantasy', 'Dragon'),
    ('KG', 'Fantasy', 'Castle'),
    ('KG', 'Fantasy', 'King'),
    ('KG', 'Fantasy', 'Queen'),
    # Family
    ('KG', 'Family', 'Sister'),
    ('KG', 'Family', 'Family'),
    ('KG', 'Family', 'Grandmother'),
    ('KG', 'Family', 'Parents'),
    ('KG', 'Family', 'Mother'),
    ('KG', 'Family', 'Brother'),
    ('KG', 'Family', 'Father'),
    ('KG', 'Family', 'Grandfather'),
    # Drinks
    ('KG', 'Drinks', 'Water'),
    ('KG', 'Drinks', 'Hot Chocolate'),
    ('KG', 'Drinks', 'Lemonade'),
    ('KG', 'Drinks', 'Soda'),
    ('KG', 'Drinks', 'Milk'),
    ('KG', 'Drinks', 'Tea'),
    ('KG', 'Drinks', 'Orange Juice'),
    ('KG', 'Drinks', 'Coffee'),
    # Desserts
    ('KG', 'Desserts', 'Cookies'),
    ('KG', 'Desserts', 'Crisps'),
    ('KG', 'Desserts', 'Donut'),
    ('KG', 'Desserts', 'Chocolate'),
    ('KG', 'Desserts', 'Popcorn'),
    ('KG', 'Desserts', 'Ice Cream'),
    ('KG', 'Desserts', 'Ice Lolly'),
    ('KG', 'Desserts', 'Cake'),
    # Description
    ('KG', 'Description', 'Bald'),
    ('KG', 'Description', 'Long Hair'),
    ('KG', 'Description', 'Short Hair'),
    ('KG', 'Description', 'Curly Hair'),
    ('KG', 'Description', 'Straight Hair'),
    ('KG', 'Description', 'Beard'),
    ('KG', 'Description', 'Pigtails'),
    ('KG', 'Description', 'Moustache'),
    # Additional categories
    # Colours
    ('KG', 'Colours', 'Red'),
    ('KG', 'Colours', 'Yellow'),
    ('KG', 'Colours', 'Blue'),
    ('KG', 'Colours', 'Green'),
    ('KG', 'Colours', 'Orange'),
    ('KG', 'Colours', 'Pink'),
    ('KG', 'Colours', 'White'),
    ('KG', 'Colours', 'Black'),
    # Clothes
    ('KG', 'Clothes2', 'Scarf'),
    ('KG', 'Clothes2', 'Jeans'),
    ('KG', 'Clothes2', 'Sneakers'),
    ('KG', 'Clothes2', 'Sandals'),
    ('KG', 'Clothes2', 'Mittens'),
    ('KG', 'Clothes2', 'Sweater'),
    ('KG', 'Clothes2', 'Raincoat'),
    ('KG', 'Clothes2', 'Rainboots'),
    ('KG', 'Clothes1', 'Hat'),
    ('KG', 'Clothes1', 'Shoes'),
    ('KG', 'Clothes1', 'Coat'),
    ('KG', 'Clothes1', 'Skirt'),
    ('KG', 'Clothes1', 'Trousers'),
    ('KG', 'Clothes1', 'Socks'),
    ('KG', 'Clothes1', 'T-shirt'),
    ('KG', 'Clothes1', 'Shorts'),
    # Classroom Objects
    ('KG', 'Classroom Objects', 'Pencil'),
    ('KG', 'Classroom Objects', 'Ruler'),
    ('KG', 'Classroom Objects', 'Crayon'),
    ('KG', 'Classroom Objects', 'Scissors'),
    ('KG', 'Classroom Objects', 'Paper'),
    ('KG', 'Classroom Objects', 'Book'),
    ('KG', 'Classroom Objects', 'Chair'),
    ('KG', 'Classroom Objects', 'Computer'),
    # Christmas
    ('KG', 'Christmas', 'Presents'),
    ('KG', 'Christmas', 'Angel'),
    ('KG', 'Christmas', 'Candy Cane'),
    ('KG', 'Christmas', 'Bell'),
    ('KG', 'Christmas', 'Santa'),
    ('KG', 'Christmas', 'Reindeer'),
    ('KG', 'Christmas', 'Christmas Tree'),
    ('KG', 'Christmas', 'Snowman'),
    ('KG', 'Buildings', 'House'),
    ('KG', 'Buildings', 'Farm'),
    ('KG', 'Buildings', 'Igloo'),
    ('KG', 'Buildings', 'Temple'),
    ('KG', 'Buildings', 'Castle'),
    ('KG', 'Buildings', 'Skyscraper'),
    ('KG', 'Buildings', 'Hut'),
    ('KG', 'Buildings', 'Teepee'),
    ('KG', 'Body Parts 1', 'Head'),
    ('KG', 'Body Parts 1', 'Shoulders'),
    ('KG', 'Body Parts 1', 'Knees'),
    ('KG', 'Body Parts 1', 'Toes'),
    ('KG', 'Body Parts 1', 'Eyes'),
    ('KG', 'Body Parts 1', 'Ears'),
    ('KG', 'Body Parts 1', 'Mouth'),
    ('KG', 'Body Parts 1', 'Nose'),
    ('KG', 'Body Parts 2', 'Hair'),
    ('KG', 'Body Parts 2', 'Teeth'),
    ('KG', 'Body Parts 2', 'Foot'),
    ('KG', 'Body Parts 2', 'Neck'),
    ('KG', 'Body Parts 2', 'Hand'),
    ('KG', 'Body Parts 2', 'Arm'),
    ('KG', 'Body Parts 2', 'Back'),
    ('KG', 'Body Parts 2', 'Finger'),
    ('KG', 'Bedroom', 'Bed'),
    ('KG', 'Bedroom', 'Blanket'),
    ('KG', 'Bedroom', 'Pillow'),
    ('KG', 'Bedroom', 'Table'),
    ('KG', 'Bedroom', 'Lamp'),
    ('KG', 'Bedroom', 'Mirror'),
    ('KG', 'Bedroom', 'Toys'),
    ('KG', 'Bedroom', 'Curtain'),
    ('KG', 'Bathroom', 'Bathtub'),
    ('KG', 'Bathroom', 'Toilet'),
    ('KG', 'Bathroom', 'Brush'),
    ('KG', 'Bathroom', 'Sink'),
    ('KG', 'Bathroom', 'Soap'),
    ('KG', 'Bathroom', 'Hairdryer'),
    ('KG', 'Bathroom', 'Shower'),
    ('KG', 'Bathroom', 'Towel'),
    ('KG', 'Animals 1', 'Fish'),
    ('KG', 'Animals 1', 'Elephant'),
    ('KG', 'Animals 1', 'Penguin'),
    ('KG', 'Animals 1', 'Turtle'),
    ('KG', 'Animals 1', 'Rabbit'),
    ('KG', 'Animals 1', 'Lion'),
    ('KG', 'Animals 1', 'Gorilla'),
    ('KG', 'Animals 1', 'Duck'),
    ('KG', 'Animals 2', 'Kangaroo'),
    ('KG', 'Animals 2', 'Mouse'),
    ('KG', 'Animals 2', 'Pig'),
    ('KG', 'Animals 2', 'Zebra'),
    ('KG', 'Animals 2', 'Monkey'),
    ('KG', 'Animals 2', 'Fox'),
    ('KG', 'Animals 2', 'Snake'),
    ('KG', 'Animals 2', 'Giraffe'),
    ('KG', 'Animals', 'Kitten'),
    ('KG', 'Animals', 'Goat'),
    ('KG', 'Animals', 'Hen'),
    ('KG', 'Animals', 'Rooster'),
    ('KG', 'Animals', 'Deer'),
    ('KG', 'Animals', 'Owl'),
    ('KG', 'Animals', 'Puppy'),
    ('KG', 'Animals', 'Lizard'),
    ('KG', 'Adjectives', 'Short'),
    ('KG', 'Adjectives', 'Tall'),
    ('KG', 'Adjectives', 'Fast'),
    ('KG', 'Adjectives', 'Slow'),
    ('KG', 'Adjectives', 'Big'),
    ('KG', 'Adjectives', 'Small'),
    ('KG', 'Adjectives', 'Strong'),
    ('KG', 'Adjectives', 'Weak')
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




# create_db()
# insert_vocab(vocab_entries)
# remove_duplicates()
# #
def get_vocab(book, unit):
    conn = sqlite3.connect('vocabulary.db')
    cursor = conn.cursor()

    query = f"SELECT word FROM vocab WHERE book=? AND unit=?"
    cursor.execute(query, (book.capitalize(), unit))

    results = cursor.fetchall()
    if not results:
        return print('Not in Data Base')

    cursor.close()
    conn.close()

    # title = book.capitalize() + ' Unit ' + str(unit) + ' Vocab'
    list1 = []
    for word in results:
        list1.append(''.join(word))

    return list1

def get_kg_vocab(level, title):
    conn = sqlite3.connect('vocabulary.db')
    cursor = conn.cursor()

    query = 'SELECT vocab From kindergarten WHERE level=? AND title=?'
    cursor.execute(query, (level, title))
    results = cursor.fetchall()

    # Extract vocabulary words from the query results
    vocab_list = [item[0] for item in results]

    print(title + ': ', vocab_list)

    cursor.close()
    conn.commit()
    return vocab_list


def some_function():
    conn = sqlite3.connect('vocabulary.db')
    cur = conn.cursor()

    # Fetch distinct book names
    cur.execute("SELECT DISTINCT book, unit FROM vocab")
    results = cur.fetchall()

    books_units = {}
    for book, unit in results:
        if book not in books_units:
            books_units[book] = [unit]
        else:
            books_units[book].append(unit)

    conn.close()
    return books_units


def make_kg_dict():
    conn = sqlite3.connect('vocabulary.db')
    cursor = conn.cursor()

    query = 'SELECT DISTINCT title, vocab FROM kindergarten'
    cursor.execute(query)
    results = cursor.fetchall()

    dict = {}
    for title, vocab in results:
        if title not in dict:
            dict[title] = [vocab]
        else:
            dict[title].append(vocab)


    cursor.close()
    conn.commit()

    print(dict)
    return dict

def get_all_books():
    conn = sqlite3.connect('vocabulary.db')
    cur = conn.cursor()

    # Fetch distinct book names
    cur.execute("SELECT DISTINCT book FROM vocab")
    books = [book[0] for book in cur.fetchall()]
    books.sort()

    conn.close()
    return books

    # return render_template('your_template.html', books=books, units=units)
# print(some_function())
if __name__ == '__main__':
    # create_db2()  # Create the database and tables
    # insert_vocab(vocab_entries)  # Insert initial vocabulary entries
    # remove_duplicates()  # Optionally remove duplicates if needed
    # get_vocab('Look1', 11)
    # get_kg_vocab('KG', 'Bedroom')
    make_kg_dict()
    # insert_vocabs2(vocab_entries2)


