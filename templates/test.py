import sqlite3
def create_db():
    conn = sqlite3.connect('dboys')
    cursor =conn.cursor()
    db_info = '''
    CREATE TABLE IF NOT EXISTS boys (
    id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL,
    name TEXT NOT NULL,
    job TEXT NOT NULL
    );
    
    '''
    cursor.execute(db_info)
    conn.commit()


def enter_info_db(entries):
    with sqlite3.connect('dboys') as conn:
        cursor = conn.cursor()
        insert_query = 'INSERT INTO boys (age, name, job) Values (?, ?, ?)'
        cursor.executemany(insert_query, (entries))

        conn.commit()


entries = [(30, 'John', 'Engineer'),
            (25, 'Sarah', 'Teacher'),
            (40, 'Michael', 'Engineer'),
            (28, 'Emily', 'Teacher'),
            (35, 'David', 'Teacher'),
            (22, 'Jessica', 'Student'),
            (45, 'Jennifer', 'Teacher'),
            (32, 'Robert', 'Student'),
            (27, 'Amanda', 'Engineer'),
            (38, 'William', 'Architect')]

def dict_of_jobs():
    with sqlite3.connect('dboys') as conn:
        cursor = conn.cursor()
        query = 'SELECT * from boys'
        cursor.execute(query)
        rows = cursor.fetchall()

        dict0 = {}
        for row in rows:
            if row[3] not in dict0:
                dict0[row[3]] = [row[1:3]]

            else:
                dict0[row[3]].append(row[1:3])

        print(dict0)




dict_of_jobs()


def remove_duplicates():
    with sqlite3.connect('dboys') as conn:
        cursor = conn.cursor()
        delete_query = '''
                DELETE FROM boys
                WHERE id NOT IN (
                    SELECT MIN(id)
                    FROM boys
                    GROUP BY age, name, job
                )
                '''
        cursor.execute(delete_query)
        conn.commit()


def query_db(age, job):
    conn = sqlite3.connect('dboys')
    cursor = conn.cursor()
    query_request = 'SELECT name from boys WHERE age=? AND job=?'
    cursor.execute(query_request, (age, job))
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


# remove_duplicates()


def get_everything():
    with sqlite3.connect('dboys') as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM boys'
        cursor.execute(query)
        rows = cursor.fetchall()




        return rows


def add_more_to_db(entries5):
    with sqlite3.connect('dboys') as conn:
        cursor = conn.cursor()
        input_query = 'INSERT into boys (age, name, job) VALUES (?, ?, ?)'
        cursor.executemany(input_query, (entries5))
        conn.commit()

entries5 = [(35, 'Jonnnnnny', 'Engineeeeeeer'),
            (25, 'Sssssarah', 'Teattttcher')]


def get_dict_of_database():
    with sqlite3.connect('dboys') as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM boys'
        cursor.execute(query)

        rows = cursor.fetchall()
        print(rows)
        print()

        columns = [column[0] for column in cursor.description]
        print(columns)
        print()

        dict7 = [dict(zip(columns, row)) for row in rows]
        print(dict7)

        for row in dict7:
            print(row)




# get_dict_of_database()
# add_more_to_db(entries5)
# create_db()
# enter_info_db(entries)
#tuples to string
# print(get_everything())

# Python3 code to demonstrate working of
# List of tuples to String
# using str() + strip()

# # initialize list
# test_list = [(1, 4), (5, 6), (8, 9), (3, 6)]
#
# # printing original list
# print("The original list is : " + str(test_list))

# List of tuples to String
# using str() + strip()
# res = str(test_list).strip('[]')
#
# # printing result
# print("Resultant string from list of tuple : " + res)