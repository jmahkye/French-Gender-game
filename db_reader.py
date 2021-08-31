import sqlite3


class DataBaseReader:
    def __init__(self, db='nouns.db'):
        self.connection = sqlite3.connect(db)
        self._random_statement = """SELECT * FROM {} ORDER BY RANDOM() LIMIT 1;""".format("nouns")

    def get_random_row(self):
        """ Query a random row in the table and return the data
        :param None
        :return: cur.fetchall()[0]
        """
        cur = self.connection.cursor()
        cur.execute(self._random_statement)
        return cur.fetchall()[0]

    def change_table(self, table_name):
        """ Change table used in db
        :param table_name: name of table in db
        :return: None
        """
        self._random_statement = """SELECT * FROM {} ORDER BY RANDOM() LIMIT 1;""".format(table_name)


if __name__ == '__main__':
    reader = DataBaseReader()
    print(reader.get_random_row())

