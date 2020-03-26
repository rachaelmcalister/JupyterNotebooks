from sys import path

path.append("/Users/rachaelmcalister/warehouse-script/python/ab_weekly_tests/")

from db_connection import DBConnection
from db_connector_user import DBConnectorUser

class DBConnectionUser(DBConnection):
    connection = None
    db_settings = None
    
    @classmethod
    def get_connection(cls, new=False):
        if new or not cls.connection:
            cls.connection = DBConnectorUser(cls.db_settings).create_connection()

        return cls.connection