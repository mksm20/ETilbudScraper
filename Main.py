import Scraper
import SqlModule
import obj
        
    
ScraperInstance = Scraper.Main_Module
list = ScraperInstance.run()
Sql = SqlModule.Sql_Connect.run()
SqlConnection = Sql[1]
crsr = Sql[2]

SqlDisconnect = SqlModule.Sql_Disconnect(SqlConnection)
SqlDisconnect.close