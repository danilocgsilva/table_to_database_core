from .TestUtils import TestUtils
from table_to_database.SqlWritterFromExcel import SqlWritterFromExcel
import unittest
from table_to_database.Utils import Utils

class test_SqlWritterFromExcel(unittest.TestCase):
    def test_write_one_line(self):
        mySqlConfiguration = TestUtils.get_test_db_configuration()
        sqlWritterFromExcel = SqlWritterFromExcel(mySqlConfiguration)
        odsFilePathString = TestUtils.create_empty_odf_file()
        database_name = "database_" + Utils.generate_friendly_date_string()
        sqlWritterFromExcel.write(database_name, odsFilePathString)
        
    def test_write_three_line(self):
        mySqlConfiguration = TestUtils.get_test_db_configuration()
        sqlWritterFromExcel = SqlWritterFromExcel(mySqlConfiguration)
        odsFilePathString = TestUtils.create_empty_odf_file()
        database_name = "database_" + Utils.generate_friendly_date_string()
        sqlWritterFromExcel.write(database_name, odsFilePathString)
        