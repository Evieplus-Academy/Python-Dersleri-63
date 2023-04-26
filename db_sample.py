import sqlite3


class Database:
    connection = None

    @classmethod
    def connect(cls, database_file):
        if cls.connection is None:
            cls.connection = sqlite3.connect(database_file)
            print("Database connection established.")
        else:
            print("Database connection already established.")

    @classmethod
    def close(cls):
        if cls.connection is not None:
            cls.connection.close()
            cls.connection = None
            print("Database connection closed.")


db1 = Database()
db1.connect("sample.db")
db1.connect("sample.db")
db1.close()
db1.connect("sample.db")
db1.connect("sample.db")
print()
db2 = Database()
db2.connect("sample.db")
db2.connect("sample.db")
db2.close()
db2.connect("sample.db")
db2.connect("sample.db")

