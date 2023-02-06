import mysql.connector

class Connection:
    def get_connection():
        connection=mysql.connector.connect(
            host="localhost",
            database="test",
            port=3307,
            username="root",
            password="")

        return connection

    def close_connection(connection):
        if connection:
            connection.close()