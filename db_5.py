import sqlite3


def create_db():
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


def recreate_kindergarten_table():
    conn = sqlite3.connect("vocabulary.db2")
    cursor = conn.cursor()

    # Drop the existing table if it exists
    drop_table_query = "DROP TABLE IF EXISTS kindergarten;"
    cursor.execute(drop_table_query)

    # Create the new kindergarten table
    create_table_query = '''
    CREATE TABLE kindergarten (
        id INTEGER PRIMARY KEY,
        level TEXT NOT NULL,
        title TEXT NOT NULL,
        vocab TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()



vocab_words = [
    ("Look 3", 1, "the US"),
    ("Look 3", 1, "Brazil"),
    ("Look 3", 1, "Argentina"),
    ("Look 3", 1, "the UK"),
    ("Look 3", 1, "Spain"),
    ("Look 3", 1, "Poland"),
    ("Look 3", 1, "Italy"),
    ("Look 3", 1, "Japan"),
    ("Look 3", 1, "South Africa"),
    ("Look 3", 1, "Australia"),
    ("Look 3", 1, "son"),
    ("Look 3", 1, "daughter"),
    ("Look 3", 1, "parent"),
    ("Look 3", 1, "grandparent"),
    ("Look 3", 1, "plane"),
    ("Look 3", 1, "game"),
    ("Look 3", 1, "train"),
    ("Look 3", 1, "paint"),
    ("Look 3", 1, "play"),
    ("Look 3", 1, "Friday"),
    ("Look 3", 2, "farm"),
    ("Look 3", 2, "field"),
    ("Look 3", 2, "forest"),
    ("Look 3", 2, "lake"),
    ("Look 3", 2, "mountain"),
    ("Look 3", 2, "path"),
    ("Look 3", 2, "river"),
    ("Look 3", 2, "town"),
    ("Look 3", 2, "village"),
    ("Look 3", 2, "waterfall"),
    ("Look 3", 2, "cable car"),
    ("Look 3", 2, "subway"),
    ("Look 3", 2, "exercise"),
    ("Look 3", 2, "tree"),
    ("Look 3", 2, "beach"),
    ("Look 3", 2, "country"),
    ("Look 3", 2, "week"),
    ("Look 3", 2, "please"),
    ("Look 3", 2, "story"),
    ("Look 3", 3, "clean up my"),
    ("Look 3", 3, "bedroom"),
    ("Look 3", 3, "cook"),
    ("Look 3", 3, "feed the dog"),
    ("Look 3", 3, "fix my bike"),
    ("Look 3", 3, "go shopping"),
    ("Look 3", 3, "make my bed"),
    ("Look 3", 3, "practice the piano"),
    ("Look 3", 3, "take out the"),
    ("Look 3", 3, "garbage"),
    ("Look 3", 3, "wash the dishes"),
    ("Look 3", 3, "water the plants"),
    ("Look 3", 3, "pick (fruit)"),
    ("Look 3", 3, "recycling"),
    ("Look 3", 3, "put away"),
    ("Look 3", 3, "night"),
    ("Look 3", 3, "right"),
    ("Look 3", 3, "my kite"),
    ("Look 3", 3, "fly"),
    ("Look 3", 3, "ride"),
    ("Look 3", 4, "bake"),
    ("Look 3", 4, "collect stickers"),
    ("Look 3", 4, "do puzzles"),
    ("Look 3", 4, "dress up"),
    ("Look 3", 4, "make things"),
    ("Look 3", 4, "play video games"),
    ("Look 3", 4, "play hide-and-seek"),
    ("Look 3", 4, "read comic books"),
    ("Look 3", 4, "roller-skate"),
    ("Look 3", 4, "watch movies"),
    ("Look 3", 4, "stick"),
    ("Look 3", 4, "teenagers"),
    ("Look 3", 4, "interested in"),
    ("Look 3", 4, "real"),
    ("Look 3", 4, "window"),
    ("Look 3", 4, "know"),
    ("Look 3", 4, "coat"),
    ("Look 3", 4, "home"),
    ("Look 3", 4, "closed"),
    ("Look 3", 5, "ketchup"),
    ("Look 3", 5, "milkshakes"),
    ("Look 3", 5, "noodles"),
    ("Look 3", 5, "pancakes"),
    ("Look 3", 5, "pasta"),
    ("Look 3", 5, "salad"),
    ("Look 3", 5, "sandwiches"),
    ("Look 3", 5, "soup"),
    ("Look 3", 5, "vegetables"),
    ("Look 3", 5, "cup"),
    ("Look 3", 5, "plate"),
    ("Look 3", 5, "bowl"),
    ("Look 3", 5, "straw"),
    ("Look 3", 5, "bottle"),
    ("Look 3", 5, "glass"),
    ("Look 3", 5, "choose"),
    ("Look 3", 5, "blue"),
    ("Look 3", 5, "Tuesday"),
    ("Look 3", 5, "ruler"),
    ("Look 3", 5, "huge"),
    ("Look 3", 6, "ant"),
    ("Look 3", 6, "bat"),
    ("Look 3", 6, "dolphin"),
    ("Look 3", 6, "kangaroo"),
    ("Look 3", 6, "panda"),
    ("Look 3", 6, "parrot"),
    ("Look 3", 6, "penguin"),
    ("Look 3", 6, "shark"),
    ("Look 3", 6, "whale"),
    ("Look 3", 6, "waking up"),
    ("Look 3", 6, "busy"),
    ("Look 3", 6, "lizard"),
    ("Look 3", 6, "hungry"),
    ("Look 3", 6, "safe"),
    ("Look 3", 6, "elephant"),
    ("Look 3", 6, "photo"),
    ("Look 3", 6, "fish"),
    ("Look 3", 6, "fruit"),
    ("Look 3", 6, "breakfast"),
    ("Look 3", 7, "a beard"),
    ("Look 3", 7, "a moustache"),
    ("Look 3", 7, "dark hair"),
    ("Look 3", 7, "light hair"),
    ("Look 3", 7, "curly hair"),
    ("Look 3", 7, "straight hair"),
    ("Look 3", 7, "fat"),
    ("Look 3", 7, "thin"),
    ("Look 3", 7, "tall"),
    ("Look 3", 7, "round face"),
    ("Look 3", 7, "meter"),
    ("Look 3", 7, "take (two hours)"),
    ("Look 3", 7, "die"),
    ("Look 3", 7, "almost"),
    ("Look 3", 7, "birthday"),
    ("Look 3", 7, "dirty"),
    ("Look 3", 7, "short"),
    ("Look 3", 7, "morning"),
    ("Look 3", 7, "dark"),
    ("Look 3", 7, "car"),
    ("Look 3", 8, "back"),
    ("Look 3", 8, "shoulder"),
    ("Look 3", 8, "stomach"),
    ("Look 3", 8, "tooth (teeth)"),
    ("Look 3", 8, "a cold"),
    ("Look 3", 8, "a cough"),
    ("Look 3", 8, "a sore neck"),
    ("Look 3", 8, "sick"),
    ("Look 3", 8, "toothache"),
    ("Look 3", 8, "medicine"),
    ("Look 3", 8, "calm"),
    ("Look 3", 8, "worry"),
    ("Look 3", 8, "grade"),
    ("Look 3", 8, "now"),
    ("Look 3", 8, "down"),
    ("Look 3", 8, "bounce"),
    ("Look 3", 8, "playground"),
    ("Look 3", 9, "building"),
    ("Look 3", 9, "bus stop"),
    ("Look 3", 9, "café"),
    ("Look 3", 9, "hospital"),
    ("Look 3", 9, "market"),
    ("Look 3", 9, "movie theater"),
    ("Look 3", 9, "parking lot"),
    ("Look 3", 9, "sports center"),
    ("Look 3", 9, "supermarket"),
    ("Look 3", 9, "skyscraper"),
    ("Look 3", 9, "factory"),
    ("Look 3", 9, "shopping center"),
    ("Look 3", 9, "birthday"),
    ("Look 3", 9, "burger"),
    ("Look 3", 9, "world"),
    ("Look 3", 9, "person"),
    ("Look 3", 10, "bike to school"),
    ("Look 3", 10, "climb trees"),
    ("Look 3", 10, "cry"),
    ("Look 3", 10, "laugh"),
    ("Look 3", 10, "need water"),
    ("Look 3", 10, "sail"),
    ("Look 3", 10, "stay home"),
    ("Look 3", 10, "wait for the bus"),
    ("Look 3", 10, "walk to school"),
    ("Look 3", 10, "archaeologist"),
    ("Look 3", 10, "machine"),
    ("Look 3", 10, "remains"),
    ("Look 3", 10, "change"),
    ("Look 3", 10, "air"),
    ("Look 3", 10, "hair"),
    ("Look 3", 10, "square"),
    ("Look 3", 10, "parent"),
    ("Look 3", 10, "bear"),
    ("Look 3", 10, "wear"),
    ("Look 3", 11, "eat outside"),
    ("Look 3", 11, "get lost"),
    ("Look 3", 11, "go canoeing"),
    ("Look 3", 11, "go on a roller coaster"),
    ("Look 3", 11, "have a picnic"),
    ("Look 3", 11, "make friends"),
    ("Look 3", 11, "ride on a motorcycle"),
    ("Look 3", 11, "see a shooting star"),
    ("Look 3", 11, "sleep in a tent"),
    ("Look 3", 11, "swim in a lake"),
    ("Look 3", 11, "ski"),
    ("Look 3", 11, "sled"),
    ("Look 3", 11, "explorer"),
    ("Look 3", 11, "face"),
    ("Look 3", 11, "pencil"),
    ("Look 3", 11, "huge"),
    ("Look 3", 11, "giraffe"),
    ("Look 3", 12, "art gallery"),
    ("Look 3", 12, "dinosaur"),
    ("Look 3", 12, "fair"),
    ("Look 3", 12, "museum"),
    ("Look 3", 12, "ride"),
    ("Look 3", 12, "sculpture"),
    ("Look 3", 12, "summer camp"),
    ("Look 3", 12, "theme park"),
    ("Look 3", 12, "water park"),
    ("Look 3", 12, "wildlife park"),
    ("Look 3", 12, "chef"),
    ("Look 3", 12, "star"),
    ("Look 3", 12, "circus"),
    ("Look 3", 12, "juggle"),
    ("Look 3", 12, "skill"),
    ("Look 3", 12, "unicycle"),
    ("Look 3", 12, "summer"),
    ("Look 3", 12, "kangaroo"),
    ("Look 3", 12, "holiday"),
    ("Look 3", 12, "banana"),
    ("Look 3", 12, "waterfall"),
    ("Look 3", 12, "travel")
]


kg_vocab = vocab_entries2 = [
    # Adjectives
    ('KG', 'Adjectives', 'Big'),
    ('KG', 'Adjectives', 'Fast'),
    ('KG', 'Adjectives', 'Short'),
    ('KG', 'Adjectives', 'Small'),
    ('KG', 'Adjectives', 'Slow'),
    ('KG', 'Adjectives', 'Strong'),
    ('KG', 'Adjectives', 'Tall'),
    ('KG', 'Adjectives', 'Weak'),
    # Animals
    ('KG', 'Animals', 'Deer'),
    ('KG', 'Animals', 'Goat'),
    ('KG', 'Animals', 'Hen'),
    ('KG', 'Animals', 'Kitten'),
    ('KG', 'Animals', 'Lizard'),
    ('KG', 'Animals', 'Owl'),
    ('KG', 'Animals', 'Puppy'),
    ('KG', 'Animals', 'Rooster'),
    # Animals 1
    ('KG', 'Animals 1', 'Duck'),
    ('KG', 'Animals 1', 'Elephant'),
    ('KG', 'Animals 1', 'Fish'),
    ('KG', 'Animals 1', 'Gorilla'),
    ('KG', 'Animals 1', 'Lion'),
    ('KG', 'Animals 1', 'Penguin'),
    ('KG', 'Animals 1', 'Rabbit'),
    ('KG', 'Animals 1', 'Turtle'),
    # Animals 2
    ('KG', 'Animals 2', 'Fox'),
    ('KG', 'Animals 2', 'Giraffe'),
    ('KG', 'Animals 2', 'Monkey'),
    ('KG', 'Animals 2', 'Mouse'),
    ('KG', 'Animals 2', 'Pig'),
    ('KG', 'Animals 2', 'Snake'),
    ('KG', 'Animals 2', 'Zebra'),
    ('KG', 'Animals 2', 'Kangaroo'),
    # Bedroom
    ('KG', 'Bedroom', 'Bed'),
    ('KG', 'Bedroom', 'Blanket'),
    ('KG', 'Bedroom', 'Curtain'),
    ('KG', 'Bedroom', 'Lamp'),
    ('KG', 'Bedroom', 'Mirror'),
    ('KG', 'Bedroom', 'Pillow'),
    ('KG', 'Bedroom', 'Table'),
    ('KG', 'Bedroom', 'Toys'),
    # Body Parts 1
    ('KG', 'Body Parts 1', 'Ears'),
    ('KG', 'Body Parts 1', 'Eyes'),
    ('KG', 'Body Parts 1', 'Head'),
    ('KG', 'Body Parts 1', 'Knees'),
    ('KG', 'Body Parts 1', 'Mouth'),
    ('KG', 'Body Parts 1', 'Nose'),
    ('KG', 'Body Parts 1', 'Shoulders'),
    ('KG', 'Body Parts 1', 'Toes'),
    # Body Parts 2
    ('KG', 'Body Parts 2', 'Arm'),
    ('KG', 'Body Parts 2', 'Back'),
    ('KG', 'Body Parts 2', 'Finger'),
    ('KG', 'Body Parts 2', 'Foot'),
    ('KG', 'Body Parts 2', 'Hair'),
    ('KG', 'Body Parts 2', 'Hand'),
    ('KG', 'Body Parts 2', 'Neck'),
    ('KG', 'Body Parts 2', 'Teeth'),
    # Buildings
    ('KG', 'Buildings', 'Castle'),
    ('KG', 'Buildings', 'Farm'),
    ('KG', 'Buildings', 'House'),
    ('KG', 'Buildings', 'Hut'),
    ('KG', 'Buildings', 'Igloo'),
    ('KG', 'Buildings', 'Skyscraper'),
    ('KG', 'Buildings', 'Temple'),
    ('KG', 'Buildings', 'Teepee'),
    # Christmas
    ('KG', 'Christmas', 'Angel'),
    ('KG', 'Christmas', 'Bell'),
    ('KG', 'Christmas', 'Candy Cane'),
    ('KG', 'Christmas', 'Christmas Tree'),
    ('KG', 'Christmas', 'Presents'),
    ('KG', 'Christmas', 'Reindeer'),
    ('KG', 'Christmas', 'Santa'),
    ('KG', 'Christmas', 'Snowman'),
    # Classroom Objects
    ('KG', 'Classroom Objects', 'Book'),
    ('KG', 'Classroom Objects', 'Chair'),
    ('KG', 'Classroom Objects', 'Computer'),
    ('KG', 'Classroom Objects', 'Crayon'),
    ('KG', 'Classroom Objects', 'Pencil'),
    ('KG', 'Classroom Objects', 'Ruler'),
    ('KG', 'Classroom Objects', 'Scissors'),
    ('KG', 'Classroom Objects', 'Paper'),
    # Clothes1
    ('KG', 'Clothes1', 'Coat'),
    ('KG', 'Clothes1', 'Hat'),
    ('KG', 'Clothes1', 'Shoes'),
    ('KG', 'Clothes1', 'Shorts'),
    ('KG', 'Clothes1', 'Skirt'),
    ('KG', 'Clothes1', 'Socks'),
    ('KG', 'Clothes1', 'T-shirt'),
    ('KG', 'Clothes1', 'Trousers'),
    # Clothes2
    ('KG', 'Clothes2', 'Jeans'),
    ('KG', 'Clothes2', 'Mittens'),
    ('KG', 'Clothes2', 'Rainboots'),
    ('KG', 'Clothes2', 'Raincoat'),
    ('KG', 'Clothes2', 'Sandals'),
    ('KG', 'Clothes2', 'Scarf'),
    ('KG', 'Clothes2', 'Sneakers'),
    ('KG', 'Clothes2', 'Sweater'),
    # Colours
    ('KG', 'Colours', 'Black'),
    ('KG', 'Colours', 'Blue'),
    ('KG', 'Colours', 'Green'),
    ('KG', 'Colours', 'Orange'),
    ('KG', 'Colours', 'Pink'),
    ('KG', 'Colours', 'Red'),
    ('KG', 'Colours', 'White'),
    ('KG', 'Colours', 'Yellow'),
    # Cook
    ('KG', 'Cook', 'Bake'),
    ('KG', 'Cook', 'Boil'),
    ('KG', 'Cook', 'Fry'),
    ('KG', 'Cook', 'Grill'),
    ('KG', 'Cook', 'Mix'),
    ('KG', 'Cook', 'Roast'),
    ('KG', 'Cook', 'Slice'),
    ('KG', 'Cook', 'Stir'),
    # Desserts
    ('KG', 'Desserts', 'Cake'),
    ('KG', 'Desserts', 'Chocolate'),
    ('KG', 'Desserts', 'Cookies'),
    ('KG', 'Desserts', 'Crisps'),
    ('KG', 'Desserts', 'Donut'),
    ('KG', 'Desserts', 'Ice Cream'),
    ('KG', 'Desserts', 'Ice Lolly'),
    ('KG', 'Desserts', 'Popcorn'),
    # Drinks
    ('KG', 'Drinks', 'Coffee'),
    ('KG', 'Drinks', 'Hot Chocolate'),
    ('KG', 'Drinks', 'Lemonade'),
    ('KG', 'Drinks', 'Milk'),
    ('KG', 'Drinks', 'Orange Juice'),
    ('KG', 'Drinks', 'Soda'),
    ('KG', 'Drinks', 'Tea'),
    ('KG', 'Drinks', 'Water'),
    # Family
    ('KG', 'Family', 'Brother'),
    ('KG', 'Family', 'Father'),
    ('KG', 'Family', 'Grandfather'),
    ('KG', 'Family', 'Grandmother'),
    ('KG', 'Family', 'Mother'),
    ('KG', 'Family', 'Parents'),
    ('KG', 'Family', 'Sister'),
    ('KG', 'Family', 'Family'),
    # Fantasy
    ('KG', 'Fantasy', 'Castle'),
    ('KG', 'Fantasy', 'Dragon'),
    ('KG', 'Fantasy', 'King'),
    ('KG', 'Fantasy', 'Queen'),
    # Feelings
    ('KG', 'Feelings', 'Happy'),
    ('KG', 'Feelings', 'Hungry'),
    ('KG', 'Feelings', 'Sad'),
    ('KG', 'Feelings', 'Sick'),
    ('KG', 'Feelings', 'Thirsty'),
    ('KG', 'Feelings', 'Tired'),
    # Food
    ('KG', 'Food', 'Chicken'),
    ('KG', 'Food', 'Eggs'),
    ('KG', 'Food', 'Hamburger'),
    ('KG', 'Food', 'Pizza'),
    ('KG', 'Food', 'Rice'),
    ('KG', 'Food', 'Salad'),
    ('KG', 'Food', 'Sandwich'),
    ('KG', 'Food', 'Steak'),
    # Fruit
    ('KG', 'Fruit', 'Apple'),
    ('KG', 'Fruit', 'Banana'),
    ('KG', 'Fruit', 'Cherry'),
    ('KG', 'Fruit', 'Grapes'),
    ('KG', 'Fruit', 'Lemon'),
    ('KG', 'Fruit', 'Orange'),
    ('KG', 'Fruit', 'Pineapple'),
    ('KG', 'Fruit', 'Strawberry'),
    # Garden
    ('KG', 'Garden', 'Flower'),
    ('KG', 'Garden', 'Grass'),
    ('KG', 'Garden', 'Tree'),
    # Hair
    ('KG', 'Hair', 'Curly Hair'),
    ('KG', 'Hair', 'Long Hair'),
    ('KG', 'Hair', 'Moustache'),
    ('KG', 'Hair', 'Pigtails'),
    ('KG', 'Hair', 'Short Hair'),
    ('KG', 'Hair', 'Straight Hair'),
    # Hospital
    ('KG', 'Hospital', 'Bed'),
    ('KG', 'Hospital', 'Curtain'),
    ('KG', 'Hospital', 'Doctor'),
    ('KG', 'Hospital', 'Hospital'),
    ('KG', 'Hospital', 'Medicine'),
    ('KG', 'Hospital', 'Nurse'),
    ('KG', 'Hospital', 'Patient'),
    ('KG', 'Hospital', 'Stretcher'),
    # Insects
    ('KG', 'Insects', 'Ant'),
    ('KG', 'Insects', 'Bee'),
    ('KG', 'Insects', 'Butterfly'),
    ('KG', 'Insects', 'Fly'),
    ('KG', 'Insects', 'Ladybug'),
    ('KG', 'Insects', 'Mosquito'),
    ('KG', 'Insects', 'Spider'),
    ('KG', 'Insects', 'Worm'),
    # Jobs
    ('KG', 'Jobs', 'Cook'),
    ('KG', 'Jobs', 'Doctor'),
    ('KG', 'Jobs', 'Fireman'),
    ('KG', 'Jobs', 'Nurse'),
    ('KG', 'Jobs', 'Policeman'),
    ('KG', 'Jobs', 'Postman'),
    ('KG', 'Jobs', 'Teacher'),
    ('KG', 'Jobs', 'Student'),
    # Kitchen
    ('KG', 'Kitchen', 'Bowl'),
    ('KG', 'Kitchen', 'Fork'),
    ('KG', 'Kitchen', 'Knife'),
    ('KG', 'Kitchen', 'Plate'),
    ('KG', 'Kitchen', 'Pot'),
    ('KG', 'Kitchen', 'Spoon'),
    ('KG', 'Kitchen', 'Cup'),
    ('KG', 'Kitchen', 'Glass'),
    # Nature
    ('KG', 'Nature', 'Flower'),
    ('KG', 'Nature', 'Grass'),
    ('KG', 'Nature', 'Mountain'),
    ('KG', 'Nature', 'Rainbow'),
    ('KG', 'Nature', 'Stars'),
    ('KG', 'Nature', 'Sun'),
    ('KG', 'Nature', 'Tree'),
    ('KG', 'Nature', 'Moon'),
    # Nature2
    ('KG', 'Nature2', 'Bridge'),
    ('KG', 'Nature2', 'Cave'),
    ('KG', 'Nature2', 'Hill'),
    ('KG', 'Nature2', 'Mud'),
    ('KG', 'Nature2', 'Path'),
    ('KG', 'Nature2', 'Sand'),
    ('KG', 'Nature2', 'Volcano'),
    ('KG', 'Nature2', 'Waterfall'),
    # Places
    ('KG', 'Places', 'Airport'),
    ('KG', 'Places', 'Bus Stop'),
    ('KG', 'Places', 'Hospital'),
    ('KG', 'Places', 'Park'),
    ('KG', 'Places', 'Restaurant'),
    ('KG', 'Places', 'School'),
    ('KG', 'Places', 'Supermarket'),
    ('KG', 'Places', 'Zoo'),
    # Prepositions
    ('KG', 'Prepositions', 'Above'),
    ('KG', 'Prepositions', 'Behind'),
    ('KG', 'Prepositions', 'Between'),
    ('KG', 'Prepositions', 'In'),
    ('KG', 'Prepositions', 'In front of'),
    ('KG', 'Prepositions', 'Next to'),
    ('KG', 'Prepositions', 'On'),
    ('KG', 'Prepositions', 'Under'),
    # Shapes
    ('KG', 'Shapes', 'Circle'),
    ('KG', 'Shapes', 'Diamond'),
    ('KG', 'Shapes', 'Heart'),
    ('KG', 'Shapes', 'Oval'),
    ('KG', 'Shapes', 'Rectangle'),
    ('KG', 'Shapes', 'Square'),
    ('KG', 'Shapes', 'Star'),
    ('KG', 'Shapes', 'Triangle'),
    # Sports
    ('KG', 'Sports', 'Badminton'),
    ('KG', 'Sports', 'Baseball'),
    ('KG', 'Sports', 'Basketball'),
    ('KG', 'Sports', 'Golf'),
    ('KG', 'Sports', 'Hockey'),
    ('KG', 'Sports', 'Soccer'),
    ('KG', 'Sports', 'Tennis'),
    ('KG', 'Sports', 'Volleyball'),
    # Transport
    ('KG', 'Transport', 'Airplane'),
    ('KG', 'Transport', 'Bicycle'),
    ('KG', 'Transport', 'Boat'),
    ('KG', 'Transport', 'Bus'),
    ('KG', 'Transport', 'Car'),
    ('KG', 'Transport', 'Helicopter'),
    ('KG', 'Transport', 'Motorbike'),
    ('KG', 'Transport', 'Train'),
    # Vegetables
    ('KG', 'Vegetables', 'Beans'),
    ('KG', 'Vegetables', 'Carrot'),
    ('KG', 'Vegetables', 'Corn'),
    ('KG', 'Vegetables', 'Cucumber'),
    ('KG', 'Vegetables', 'Mushroom'),
    ('KG', 'Vegetables', 'Onion'),
    ('KG', 'Vegetables', 'Potato'),
    ('KG', 'Vegetables', 'Tomato'),
    # Verbs
    ('KG', 'Verbs', 'Drink'),
    ('KG', 'Verbs', 'Eat'),
    ('KG', 'Verbs', 'Listen'),
    ('KG', 'Verbs', 'Read'),
    ('KG', 'Verbs', 'Run'),
    ('KG', 'Verbs', 'Sleep'),
    ('KG', 'Verbs', 'Walk'),
    ('KG', 'Verbs', 'Write'),
    # Verbs2
    ('KG', 'Verbs2', 'Count'),
    ('KG', 'Verbs2', 'Cry'),
    ('KG', 'Verbs2', 'Dance'),
    ('KG', 'Verbs2', 'Laugh'),
    ('KG', 'Verbs2', 'Play'),
    ('KG', 'Verbs2', 'Sing'),
    ('KG', 'Verbs2', 'Swim'),
    ('KG', 'Verbs2', 'Watch'),
    # Weather
    ('KG', 'Weather', 'Cloudy'),
    ('KG', 'Weather', 'Cold'),
    ('KG', 'Weather', 'Fine'),
    ('KG', 'Weather', 'Hot'),
    ('KG', 'Weather', 'Rainy'),
    ('KG', 'Weather', 'Snowy'),
    ('KG', 'Weather', 'Sunny'),
    ('KG', 'Weather', 'Windy')
]
def enter_vocab_to_database(vocab_words):
    with sqlite3.connect('vocabulary.db2') as conn:
        cursor = conn.cursor()
        insert_query = 'INSERT INTO vocab (book, unit, word) Values (?, ?, ?)'
        cursor.executemany(insert_query, (vocab_words))
        conn.commit()


def enter_kg_vocab_to_database(kg_vocab):
    try:
        with sqlite3.connect('vocabulary.db2') as conn:
            cursor = conn.cursor()
            insert_query = 'INSERT INTO kindergarten (level, title, vocab) Values (?, ?, ?)'
            cursor.executemany(insert_query, kg_vocab)
            conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")





# 2 db created
# create_db()
# create_db2()

#entered look 2 and 1 and 3
# enter_vocab_to_database(vocab_words)

# recreate_kindergarten_table()
# enter_kg_vocab_to_database(kg_vocab)

def query_kindergarten_db(level, title):
    with sqlite3.connect("vocabulary.db2") as conn:
        cursor = conn.cursor()
        query = 'SELECT vocab From kindergarten WHERE level=? AND title=?'
        cursor.execute(query, (level, title))
        results = cursor.fetchall()


        conn.commit()
        return results


def remove_duplicates():
    with sqlite3.connect('vocabulary.db2') as conn:
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



def get_vocab(book, unit):
    conn = sqlite3.connect('vocabulary.db2')
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
    conn = sqlite3.connect('vocabulary.db2')
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
    conn = sqlite3.connect('vocabulary.db2')
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
    conn = sqlite3.connect('vocabulary.db2')
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
    conn = sqlite3.connect('vocabulary.db2')
    cur = conn.cursor()

    # Fetch distinct book names
    cur.execute("SELECT DISTINCT book FROM vocab")
    books = [book[0] for book in cur.fetchall()]
    books.sort()

    conn.close()
    return books


if __name__ == '__main__':
    # create_db2()  # Create the database and tables
    # insert_vocab(vocab_entries)  # Insert initial vocabulary entries
    # remove_duplicates()  # Optionally remove duplicates if needed
    # get_vocab('Look1', 11)
    # get_kg_vocab('KG', 'Bedroom')
    make_kg_dict()
    # insert_vocabs2(vocab_entries2)




# remove_duplicates()
# print(query_kindergarten_db('KG', 'Bedroom'))



