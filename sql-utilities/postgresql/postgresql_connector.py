import psycopg2
from psycopg2 import OperationalError


class DatabaseConnector:
    def __init__(self, dbname, host, port, user, password):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            print(f"Attempting to connect to {self.dbname} at {self.host}:{self.port}")
            self.connection = psycopg2.connect(
                database = self.dbname,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
            )
            self.cursor = self.connection.cursor()
            print(f"Connected to {self.dbname}")
        except OperationalError as e:
            print(f"Error: Unable to connect to the database: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print(f"Connection closed")
