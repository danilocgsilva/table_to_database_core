import unittest
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
from table_to_database.ToDatabaseCore import ToDatabaseCore
from table_to_database.Utils import Utils
from table_to_database.MySqlConfiguration import MySqlConfiguration
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
        self.toDatabase.set_database_configuration(
            TestUtils.get_test_db_configuration()
        )
        data_create_table_one_row = [['column1', 'column2', 'column3'], [1, 2, 3]]
        ods_file_name = self._create_ods_with_data(data_create_table_one_row)
        self.generatedOds = ods_file_name
        database_name = Utils.generate_friendly_date_string()
        results = self.toDatabase.to_database(ods_file_name, database_name)
        self.generatedDatabase = database_name
        self.assertTrue(Utils.databaseExists(results.database_created, TestUtils.get_test_db_configuration()), f"Database {database_name} should exist after creation.")
        
    def test_create_one_row(self):
        self.toDatabase.set_database_configuration(
            self._configure_configuration()
        )
        data_create_table_one_row = [['column1', 'column2', 'column3'], [1, 2, 3]]
        self.generatedOds = self._create_ods_with_data(data_create_table_one_row)
        self.generatedDatabase = "database_" + Utils.generate_friendly_date_string()
        results = self.toDatabase.to_database(self.generatedOds, self.generatedDatabase)
        registers_count = self._count_registers(self.generatedDatabase, results.tables_created[0])
        self.assertEqual(1, registers_count, f"Database {self.generatedDatabase} should contain exactly one row after adding one row.")
        
    def test_create_three_rows(self):
        database_configuration = self._configure_configuration()
        data_create_table_three_rows = [['column1', 'column2', 'column3'], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.generatedOds = self._create_ods_with_data(data_create_table_three_rows)
        self.toDatabase.set_database_configuration(database_configuration)
        self.generatedDatabase = "database_" + Utils.generate_friendly_date_string()
        results = self.toDatabase.to_database(self.generatedOds, self.generatedDatabase)
        registers_count = self._count_registers(self.generatedDatabase, results.tables_created[0])
        self.assertEqual(3, registers_count, f"Database {self.generatedDatabase} should contain exactly three rows after adding three rows.")
        
    def test_create_two_tables(self):
        self.toDatabase.set_database_configuration(
            self._configure_configuration()
        )
        data_create_table_one = [['column1', 'column2', 'column3'], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
        data_create_table_two = [['columnA', 'columnB', 'columnC'], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L']]
        self.generatedOds = self._create_ods_with_spreadsheets(
            {"Table_One": data_create_table_one},
            {"Table_Two": data_create_table_two}
        )
        self.generatedDatabase = "database_" + Utils.generate_friendly_date_string()
        results = self.toDatabase.to_database(self.generatedOds, self.generatedDatabase)
        registers_count_table_one = self._count_registers(self.generatedDatabase, results.tables_created[0])
        registers_count_table_two = self._count_registers(self.generatedDatabase, results.tables_created[1])
        self.assertEqual(3, registers_count_table_one, f"Database {self.generatedDatabase} should contain exactly three rows in table one after adding three rows.")
        self.assertEqual(4, registers_count_table_two, f"Database {self.generatedDatabase} should contain exactly three rows in table two after adding three rows.")
        
    def test_upload_data_twice_equal_data(self):
        self.toDatabase.set_database_configuration(
            self._configure_configuration()
        )
        data_create_table_one = [['column1', 'column2', 'column3'], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.generatedOds = self._create_ods_with_data(data_create_table_one)
        self.generatedDatabase = "database_" + Utils.generate_friendly_date_string()
        self.toDatabase.to_database(self.generatedOds, self.generatedDatabase)
        self.toDatabase.to_database(self.generatedOds, self.generatedDatabase)
        
    def _configure_configuration(self):
        database_configuration = TestUtils.get_test_db_configuration()
        self._database_connection(database_configuration)
        return database_configuration
        
    


