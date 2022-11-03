from DbFill import DbFiller
import django


def fillDB():
    CreateDatabase = DbFiller
    CreateDatabase.dbFill(CreateDatabase)

fillDB()