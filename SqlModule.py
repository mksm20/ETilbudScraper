import sqlite3

class Sql_Connect:
    def run():
        connection = sqlite3.connect("price_grocery.db")
        crsr = connection.cursor()
        return (crsr, connection)
        
class Sql_Request:
    None