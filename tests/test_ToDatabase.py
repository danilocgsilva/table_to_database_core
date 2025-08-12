import unittest
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
from table_to_database.ToDatabaseCore import ToDatabaseCore
from table_to_database.Utils import Utils
from table_to_database.MySqlConfiguration import MySqlConfiguration
from table_to_database.Exceptions.DatabaseNotAvailableException import DatabaseNotAvailableException
from table_to_database.MySqlDriver import MySqlDriver
from .TestUtils import TestUtils
from .TestTrait import TestTrait
from .TearDownMethods import TearDownMethods

class test_ToDatabase(unittest.TestCase, TestTrait, TearDownMethods):
    def setUp(self):
        self.toDatabase = ToDatabase(ToDatabaseCore())
        self.generatedOds = None
        self.generatedDatabase = None
        mySqlDriver = MySqlDriver()
        mySqlDriver.set_database_configuration(TestUtils.get_test_db_configuration())
        self.mySqlDriver = mySqlDriver
        
    def tearDown(self):
        self._tearDown()
        
    def test_set_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.toDatabase.to_database("not_existing_file.ods")
            
    def test_excepts_if_database_configuration_not_setted(self):
        ods_file_name = TestUtils.create_empty_odf_file()
        self.generatedOds = ods_file_name
        with self.assertRaises(MissingDatabaseConfigurationException):
            self.toDatabase.to_database(ods_file_name)
            
    def test_create_database(self):
        database_configuration = TestUtils.get_test_db_configuration()
        
        data_create_table_one_row = [['column1', 'column2', 'column3'], [1, 2, 3]]
        ods_file_name = self._create_ods_with_data(data_create_table_one_row)
        self.generatedOds = ods_file_name
        self.toDatabase.set_database_configuration(database_configuration)
        database_name = Utils.generate_friendly_date_string()
        results = self.toDatabase.to_database(ods_file_name, database_name)
        self.generatedDatabase = database_name
        self.assertTrue(Utils.databaseExists(results.database_created, TestUtils.get_test_db_configuration()), f"Database {database_name} should exist after creation.")
        
    def test_create_one_row(self):
        database_configuration = TestUtils.get_test_db_configuration()
        self._database_connection(database_configuration)
        data_create_table_one_row = [['column1', 'column2', 'column3'], [1, 2, 3]]
        table_file_name = self._create_ods_with_data(data_create_table_one_row)
        self.toDatabase.set_database_configuration(database_configuration)
        database_name = "database_" + Utils.generate_friendly_date_string()
        results = self.toDatabase.to_database(table_file_name, database_name)
        self.generatedDatabase = database_name
        self.generatedOds = table_file_name
        registers_count = self._count_registers(database_name, results.tables_created[0])
        self.assertEqual(1, registers_count, f"Database {database_name} should contain exactly one row after adding one row.")
        
    def _database_connection(self, database_configuration):
        try:
            database_configuration.test_connection()
        except DatabaseNotAvailableException:
            raise Exception("Tests can't proceed. Please, have a test database available...")


