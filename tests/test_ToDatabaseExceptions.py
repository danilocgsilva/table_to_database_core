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
        
    def _configure_configuration(self):
        database_configuration = TestUtils.get_test_db_configuration()
        self._database_connection(database_configuration)
        return database_configuration
    
