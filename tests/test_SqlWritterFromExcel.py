import unittest
from .TestUtils import TestUtils
from table_to_database.SqlWritterFromExcel import SqlWritterFromExcel
from table_to_database.MySqlDriver import MySqlDriver
from table_to_database.Utils import Utils
from collections import OrderedDict
from pyexcel_ods import save_data

class test_SqlWritterFromExcel(unittest.TestCase):
    def test_write_one_line(self):
        mySqlConfiguration = TestUtils.get_test_db_configuration()
        sqlWritterFromExcel = SqlWritterFromExcel(mySqlConfiguration)
        odsFilePathString = TestUtils.create_empty_odf_file()
        database_name = "database_" + Utils.generate_friendly_date_string()
        sqlWritterFromExcel.write(database_name, odsFilePathString)
        self._dropDatabase(database_name)
        
    def test_write_three_line(self):
        mySqlConfiguration = TestUtils.get_test_db_configuration()
        
        mySqlDriver = MySqlDriver()
        mySqlDriver.set_database_configuration(mySqlConfiguration)
        
        sqlWritterFromExcel = SqlWritterFromExcel(mySqlConfiguration)
        
        odsFilePathString = self._create_ods()
        database_name = "database_" + Utils.generate_friendly_date_string()
        Utils.create_database(database_name, mySqlDriver)
        sqlWritterFromExcel.write(database_name, odsFilePathString)
        
    def _create_ods(self):
        ods_file_name_path = Utils.generate_friendly_date_string() + ".ods"
        ordered_dict = OrderedDict()
        ordered_dict.update({"Sheet 1": [[1,2,3],[4,5,6],[7,8,9]]})
        save_data(ods_file_name_path, ordered_dict)
        return ods_file_name_path
        
    # def _dropDatabase(self, database_name):
        