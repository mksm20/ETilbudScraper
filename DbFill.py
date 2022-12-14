import datetime
import Scraper
import SqlModule
import obj
import csv
import re


class DbFiller:  
    
    def dbFill(self):        
        ScraperInstance = Scraper.Main_Module
        groceryList = ScraperInstance.run()
        Sql = SqlModule.Sql_Connect.run()
        conn = Sql[1]
        crsr = Sql[0]

        table = """ CREATE TABLE IF NOT EXISTS GroceriesRand(
                    Name TEXT,
                    Store TEXT,
                    Extra TEXT,
                    Price REAL,
                    Date INTEGER 
                ); """
        table2 = """ CREATE TABLE IF NOT EXISTS GroceriesEat(
                    Name TEXT,
                    Store TEXT,
                    Extra TEXT,
                    Price REAL,
                    Date INTEGER 
                ); """
                
        tables = (table, table2)
        for table in tables:
            crsr.execute(table)
            conn.commit()

        time = str(datetime.datetime.now())

        for object in groceryList:
            inputStr = "GroceriesEat"
            if self.__isGrocery(object):
                inputStr = "GroceriesRand"
            extra = ""
            if(object.Extra is not None):
                extra = str(object.Extra)
            sqlInsert = f"""INSERT INTO {inputStr} 
            (Name, Store, Extra ,Price, Date)
            VALUES (?,?,?,?,?)"""    
            crsr.execute(sqlInsert, (str(object.Name),str(object.Store),extra,str(object.Price), time))
            conn.commit()
        conn.close()
        
    @classmethod          
    def __isGrocery(self, grocery):
        with open("groceryStoreList.csv", "r") as file:
            data = csv.reader(file)
            for field in data:
                for fields in field:
                    if re.match("K-bmandsg*rden", fields):
                        re.sub("-", "ø", str(fields))
                        re.sub("*", "å", str(fields))
                    print(str(fields))
                    if grocery.Store == fields:
                        return False
            if float(grocery.Price) < 500:
                    return False 
            return True
