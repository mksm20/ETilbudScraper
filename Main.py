import datetime
import Scraper
import SqlModule
import obj
        
        
ScraperInstance = Scraper.Main_Module
for item in ScraperInstance.groceryList:
    print(item.Name, item.Price, item.Extra, item.Store)
Sql = SqlModule.Sql_Connect.run()
conn = Sql[1]
crsr = Sql[0]
table = """ CREATE TABLE IF NOT EXISTS Groceries(
            Name TEXT,
            Store TEXT,
            Extra TEXT,
            Price REAL,
            Date INTEGER 
        ); """
crsr.execute(table)
conn.commit()
time = str(datetime.datetime.now())
for objects in ScraperInstance.groceryList:
    sqlInsert = """INSERT INTO Groceries 
    (Name, Store, Extra ,Price, Date)
    VALUES (?,?,?,?,?)"""
    extra = ""
    if(objects.Extra is not None):
        extra = str(objects.Extra)
    crsr.execute(sqlInsert, (str(objects.Name),str(objects.Store),extra,str(objects.Price), time))
    conn.commit()
conn.close()