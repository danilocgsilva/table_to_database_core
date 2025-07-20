import unittest
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
from .TestUtils import TestUtils

class test_ToDatabase(unittest.TestCase):
    def setUp(self):
        self.toDatabase = ToDatabase()
        
    def test_set_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.toDatabase.set_file("path/to/non_existent_file.txt")
            self.toDatabase.to_database()
            
    def test_excepts_if_database_configuration_not_setted(self):
        ods_file_name = TestUtils.create_empty_odf_file()
        with self.assertRaises(MissingDatabaseConfigurationException):
            self.toDatabase.set_file(ods_file_name)
            self.toDatabase.to_database()
