import psycopg2
from psycopg2 import OperationalError
import csv

class PostgresqlDatabaseConnector:
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

    def sql_stmt_to_execute(self, sql_stmt):
        try:
            print(f"Running query: {sql_stmt}")
            self.cursor.execute(sql_stmt)
            records = self.cursor.fetchall()
            return records
        except OperationalError as e:
            print(f"Error: Unable to execute query: {e}")
            return None
        
    def spool_stmt_to_csv(self, sql_stmt, csv_output):
        try:
            records = self.sql_stmt_to_execute(sql_stmt)
            record_count = self.cursor.rowcount
            header = [desc[0] for desc in self.cursor.description]
            with open(csv_output, mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
                writer.writerows(records)
            print(f"{record_count} records written to {csv_output}")
        except OperationalError as e:
            print(f"Error: Unable to spool records to csv: {e}")

    def sql_file_to_execute(self, sql_file,):
        try:
            with open(sql_file, mode='r') as file:
                sql_stmt = file.read()
            print(f"Running query: {sql_stmt}")
            self.cursor.execute(sql_stmt)
            records = self.cursor.fetchall()
            return records
        except OperationalError as e:
            print(f"Error: Unable to execute query: {e}")
            return None

    def spool_sql_file_to_csv(self, sql_stmt, csv_output):
        try:
            records = self.sql_stmt_to_execute(sql_stmt)
            record_count = self.cursor.rowcount
            header = [desc[0] for desc in self.cursor.description]
            with open(csv_output, mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
                writer.writerows(records)
            print(f"{record_count} records written to {csv_output}")
        except OperationalError as e:
            print(f"Error: Unable to spool records to csv: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print(f"Connection closed")