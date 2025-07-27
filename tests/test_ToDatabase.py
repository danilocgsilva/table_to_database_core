import unittest
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
from table_to_database.ToDatabaseCore import ToDatabaseCore
from table_to_database.Utils import Utils
from table_to_database.MySqlConfiguration import MySqlConfiguration
from table_to_database.Exceptions.DatabaseNotAvailableException import DatabaseNotAvailableException
import os
from table_to_database.MySqlDriver import MySqlDriver

class test_ToDatabase(unittest.TestCase):
    def setUp(self):
        self.toDatabase = ToDatabase(ToDatabaseCore())
        
    def test_set_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.toDatabase.set_excel_file("path/to/non_existent_file.txt")
            self.toDatabase.to_database()
            
    def test_excepts_if_database_configuration_not_setted(self):
        ods_file_name = Utils.create_empty_odf_file()
        with self.assertRaises(MissingDatabaseConfigurationException):
            self.toDatabase.set_excel_file(ods_file_name)
            self.toDatabase.to_database()
            
    def test_create_database(self):
        database_configuration = MySqlConfiguration()
        database_configuration.user = os.environ.get("TEST_DB_USER")
        database_configuration.password = os.environ.get("TEST_DB_PASSWORD")
        database_configuration.host = os.environ.get("TEST_DB_HOST")
        
        try:
            database_configuration.test_connection()
        except DatabaseNotAvailableException:
            raise Exception("Tests can't proceed. Please, have a test database available...")
        
        ods_file_name = Utils.create_empty_odf_file()
        
        self.toDatabase.set_excel_file(ods_file_name)
        self.toDatabase.set_database_configuration(database_configuration)
        
        database_name = Utils.generate_friendly_date_string()
        self.toDatabase.to_database(database_name)
        
        self.assertTrue(self._databaseExists(database_name), f"Database {database_name} should exist after creation.")
        
    def _databaseExists(self, database_name: str) -> bool:
        """Check if the database exists."""
        mysql_driver = MySqlDriver()
        mysql_driver.set_database_configuration(self._getDatabaseConfiguration())
        
        try:
            result = mysql_driver.exec(f"SHOW DATABASES LIKE '%{database_name}%'")
            return result.__len__() > 0
        except Exception as e:
            print(f"Error checking database existence: {e}")
            return False    

    def _getDatabaseConfiguration(self) -> MySqlConfiguration:
        """Get the database configuration."""
        database_configuration = MySqlConfiguration()
        database_configuration.user = os.environ.get("TEST_DB_USER")
        database_configuration.password = os.environ.get("TEST_DB_PASSWORD")
        database_configuration.host = os.environ.get("TEST_DB_HOST")
        return database_configuration
