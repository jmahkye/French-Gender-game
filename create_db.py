import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param connection: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def create_row_entry(connection, data):
    """
    Create a new task
    :param connection:
    :param data:
    :return:
    """

    sql = ''' INSERT INTO nouns(id, name, gender, grammatical_no)
              VALUES(?,?,?,?) '''
    cur = connection.cursor()
    cur.execute(sql, data)
    connection.commit()

    return cur.lastrowid


if __name__ == '__main__':
    database = "resources/nouns.db"

    sql_create_nouns_table = """ CREATE TABLE IF NOT EXISTS nouns (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            gender text NOT NULL,
                                            grammatical_no NOT NULL
                                        ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_nouns_table)

    else:
        print("Error! cannot create the database connection.")

    fileName = 'resources\\dictionary\\nouns.txt'
    cursor = conn.execute('select * from nouns')
    length = len([description[0] for description in cursor.description])
    with open(fileName, 'r', encoding='utf-8') as f:
        rows = list(f.read().split('\n'))
        for i, row in enumerate(rows):
            row = row.split(';')
            row.insert(0, i)
            if len(row) == length:
                create_row_entry(conn, row)
