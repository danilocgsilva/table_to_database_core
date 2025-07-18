import unittest
from table_to_database.ToDatabase import ToDatabase

class test_ToDatabase(unittest.TestCase):
    def setUp(self):
        self.toDatabase = ToDatabase()
        
    def test_set_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.toDatabase.set_file("path/to/non_existent_file.txt")
            self.toDatabase.to_database()
        # self.toDatabase.set_file("path/to/non_existent_file.txt")

    # def test_set_file(self):
    #     self.converter.set_file("path/to/file")
    #     self.assertEqual(self.converter.file_path, "path/to/file")

    # def test_to_database_without_file(self):
    #     with self.assertRaises(ValueError):
    #         self.converter.to_database()

    # def test_to_database_with_non_existent_file(self):
    #     self.converter.set_file("path/to/non_existent_file")
    #     with self.assertRaises(FileNotFoundError):
    #         self.converter.to_database()


    # def test_example(self):
    #     # Example test case
    #     self.assertTrue(True)
    
    # def touch_empty_file(self, file_path):
    #     """Create an empty file at the specified path."""
    #     with open("here.txt", 'w') as f:
    #         f.write("dummy content")
