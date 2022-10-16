import datetime
import Scraper
import SqlModule
import obj
        
        
ScraperInstance = Scraper.Main_Module
for item in ScraperInstance.groceryList:
    print(item.Name, item.Price, item.Store)
Sql = SqlModule.Sql_Connect.run()
conn = Sql[1]
crsr = Sql[0]
table = """ CREATE TABLE IF NOT EXISTS Groceries(
            Name TEXT,
            Store TEXT,
            Price REAL,
            Date INTEGER 
        ); """
crsr.execute(table)
conn.commit()
time = datetime.datetime.now()
time = str(time)
for objects in ScraperInstance.groceryList:
    sqlInsert = """INSERT INTO Groceries 
    (Name, Store, Price, Date)
    VALUES (?,?,?,?)"""
    crsr.execute(sqlInsert, (str(objects.Name),str(objects.Store), str(objects.Price), time))
    conn.commit()
conn.close()