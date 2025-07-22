import unittest
from table_to_database.MySqlConfiguration import MySqlConfiguration
from table_to_database.Exceptions.DatabaseNotAvailableException import DatabaseNotAvailableException
from table_to_database.Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException

class test_MySqlConfiguration(unittest.TestCase):
    def setUp(self):
        self.mysql_configuration = MySqlConfiguration()

    def test_missing_configuration(self):
        with self.assertRaises(ValueError):
            self.mysql_configuration.ready()
            
    def test_non_existing_database_configuration_exceltion(self):
        self.mysql_configuration.user = "test_user"
        self.mysql_configuration.password = "test_password"
        self.mysql_configuration.host = "localhost"
        self.mysql_configuration.port = 3306
        
        with self.assertRaises(DatabaseNotAvailableException):
            self.mysql_configuration.test_connection()

