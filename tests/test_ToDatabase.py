import unittest
from table_to_database.Facade.ToDatabase import ToDatabase

class test_ToDatabase(unittest.TestCase):
    def setUp(self):
        self.toDatabase = ToDatabase()
        
    def test_set_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.toDatabase.set_file("path/to/non_existent_file.txt")
            self.toDatabase.to_database()
            
    def test_excepts_if_database_configuration_not_setted(self):

