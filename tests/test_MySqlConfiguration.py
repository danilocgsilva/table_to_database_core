import unittest
from table_to_database.MySqlConfiguration import MySqlConfiguration

class test_MySqlConfiguration(unittest.TestCase):
    def setUp(self):
        self.mysql_configuration = MySqlConfiguration()

    def test_missing_configuration(self):
        with self.assertRaises(ValueError):
            self.mysql_configuration.ready()

