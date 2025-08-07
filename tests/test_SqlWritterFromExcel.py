import unittest
from .TestUtils import TestUtils
from table_to_database.SqlWritterFromExcel import SqlWritterFromExcel
from table_to_database.MySqlDriver import MySqlDriver
from table_to_database.Utils import Utils
from collections import OrderedDict
from pyexcel_ods import save_data
from .TestTrait import TestTrait
from table_to_database.Exceptions.DatabaseNotExistsException import DatabaseNotExistsException

class test_SqlWritterFromExcel(unittest.TestCase, TestTrait):
    def setUp(self):
        self.mySqlDriver = MySqlDriver()
        self.mySqlDriver.set_database_configuration(TestUtils.get_test_db_configuration())
    
    def test_raise_database_not_exists(self):
        mySqlConfiguration = TestUtils.get_test_db_configuration()
        sqlWritterFromExcel = SqlWritterFromExcel(mySqlConfiguration)
        data_table = [
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ]
        odsFilePathString = TestUtils.create_ods_with_data(data_table, "ods_")
        with self.assertRaises(DatabaseNotExistsException):
            sqlWritterFromExcel.write("some_database", odsFilePathString)
    
    def test_write_one_line(self):
        mySqlConfiguration = TestUtils.get_test_db_configuration()
        sqlWritterFromExcel = SqlWritterFromExcel(mySqlConfiguration)
        data_table = [
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ]
        odsFilePathString = TestUtils.create_ods_with_data(data_table, "ods_")
        database_name = "database_" + Utils.generate_friendly_date_string()
        
        Utils.create_database(database_name, self.mySqlDriver)
        results = sqlWritterFromExcel.write(database_name, odsFilePathString)
        created_rows = self._count_registers(results.database_created, results.tables_created[0])
        self.assertEqual(created_rows, 1)
        
    def test_write_three_line(self):
        mySqlConfiguration = TestUtils.get_test_db_configuration()
        
        sqlWritterFromExcel = SqlWritterFromExcel(mySqlConfiguration)
        
        odsFilePathString = self._create_ods()
        database_name = "database_" + Utils.generate_friendly_date_string()
        Utils.create_database(database_name, self.mySqlDriver)
        sqlWritterFromExcel.write(database_name, odsFilePathString)
        
    def _create_ods(self):
        ods_file_name_path = Utils.generate_friendly_date_string() + ".ods"
        ordered_dict = OrderedDict()
        ordered_dict.update({"Sheet 1": [[1,2,3],[4,5,6],[7,8,9]]})
        save_data(ods_file_name_path, ordered_dict)
        return ods_file_name_path
        
        