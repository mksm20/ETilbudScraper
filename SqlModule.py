import sqlite3

class Sql_Connect:
    def run():
        connection = sqlite3.connect("price_grocery.db")
        crsr = connection.cursor()
        return (crsr, connection)
        

class Sql_Disconnect:
    def __init__(self, connection):
        self.connection = connection
    def close(self):
        self.connection.close()