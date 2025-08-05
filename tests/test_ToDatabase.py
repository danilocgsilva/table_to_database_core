import unittest
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
from table_to_database.ToDatabaseCore import ToDatabaseCore
from table_to_database.Utils import Utils
from table_to_database.MySqlConfiguration import MySqlConfiguration
from table_to_database.Exceptions.DatabaseNotAvailableException import DatabaseNotAvailableException
from table_to_database.MySqlDriver import MySqlDriver
from collections import OrderedDict
from .TestUtils import TestUtils
from pyexcel_ods import save_data

class test_ToDatabase(unittest.TestCase):
    def setUp(self):
        self.toDatabase = ToDatabase(ToDatabaseCore())
        
    def test_set_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.toDatabase.to_database("not_existing_file.ods")
            
    def test_excepts_if_database_configuration_not_setted(self):
        ods_file_name = TestUtils.create_empty_odf_file()
        with self.assertRaises(MissingDatabaseConfigurationException):
            self.toDatabase.to_database(ods_file_name)
            
    def test_create_database(self):
        database_configuration = TestUtils.get_test_db_configuration()
        self._test_database_connection(database_configuration)
        ods_file_name = TestUtils.create_empty_odf_file()
        self.toDatabase.set_database_configuration(database_configuration)
        database_name = Utils.generate_friendly_date_string()
        self.toDatabase.to_database(database_name, ods_file_name)
        self.assertTrue(self._databaseExists(database_name), f"Database {database_name} should exist after creation.")
        
    def test_create_one_row(self):
        database_configuration = TestUtils.get_test_db_configuration()
        self._database_connection(database_configuration)
        data_create_table_one_row = [['column1', 'column2', 'column3'], [1, 2, 3]]
        table_file_name = self._create_ods(data_create_table_one_row)
        self.toDatabase.set_database_configuration(database_configuration)
        database_name = "database_" + Utils.generate_friendly_date_string()
        results = self.toDatabase.to_database(table_file_name, database_name)
        table_name = "Sheet1"
        registers_count = self._count_registers(database_name, table_name)
        self.assertCountEqual(1, registers_count, f"Database {database_name} should contain exactly one row after adding one row.")
        
    def _database_connection(self, database_configuration):
        try:
            database_configuration.test_connection()
        except DatabaseNotAvailableException:
            raise Exception("Tests can't proceed. Please, have a test database available...")
        
    def _databaseExists(self, database_name: str) -> bool:
        """Check if the database exists."""
        mysql_driver = MySqlDriver()
        # mysql_driver.set_database_configuration(self._getDatabaseConfiguration())
        mysql_driver.set_database_configuration(TestUtils.get_test_db_configuration())
        try:
            result = mysql_driver.exec(f"SHOW DATABASES LIKE '%{database_name}%'")
            return result.__len__() > 0
        except Exception as e:
            print(f"Error checking database existence: {e}")
            return False
    
    def _count_registers(self, database_name: str, table_name):
        """Count the number of registers in the database."""
        mysql_driver = MySqlDriver()
        # mysql_driver.set_database_configuration(self._getDatabaseConfiguration())
        mysql_driver.set_database_configuration(TestUtils.get_test_db_configuration())
        
        try:
            result = mysql_driver.exec(f"SELECT COUNT(*) FROM {table_name};")
            result = result[0][0]
            return result
        except Exception as e:
            print(f"Error counting registers: {e}")
    
    def _create_ods(self, data_from_list):
        file_name_path = "generic_table_file_" + Utils.generate_friendly_date_string() + ".ods"
        order_dict = OrderedDict()
        order_dict.update({"Sheet 1": data_from_list})
        save_data(file_name_path, order_dict)
        return file_name_path

