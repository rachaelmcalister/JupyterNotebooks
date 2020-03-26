from sys import path
from boto3 import client

path.append("/Users/rachaelmcalister/warehouse-script/python/ab_weekly_tests/")

from db_connector import DBConnector

class DBConnectorUser(DBConnector):
    
    def __init__(self, db_settings = None):
        self.db_settings = db_settings
        self.db_connection = None
    
    def setup_redshift_credentials(self,
                                   user='rachael',
                                   cluster='redshift-warehouse-production'):
        """
        Sets up redshift connection authenticating and generating temporary
        credentials for further db connections.
        Returns:
            Dict: Credentials required to establish db connections.
        """
        redshift_client = client('redshift')
        credentials = redshift_client.get_cluster_credentials(
            DbUser=user,
            ClusterIdentifier=cluster
        )
        return credentials

