import unittest
from .TestUtils import TestUtils
from table_to_database.SqlWritterFromExcel import SqlWritterFromExcel
from table_to_database.MySqlDriver import MySqlDriver
from table_to_database.Utils import Utils
from collections import OrderedDict
from pyexcel_ods import save_data
from .TestTrait import TestTrait
from table_to_database.Exceptions.DatabaseNotExistsException import DatabaseNotExistsException
import os
from .TearDownMethods import TearDownMethods

class test_SqlWritterFromExcel(unittest.TestCase, TestTrait, TearDownMethods):
    def setUp(self):
        self.mySqlDriver = MySqlDriver()
        self.mySqlDriver.set_database_configuration(TestUtils.get_test_db_configuration())
        self.generatedOds = None
        self.generatedDatabase = None
        self.mysqlConfiguration = TestUtils.get_test_db_configuration()

    def tearDown(self):
        self._tearDown()

    def test_raise_exception_if_database_not_exists(self):
        sqlWritterFromExcel = SqlWritterFromExcel(self.mysqlConfiguration)
        data_table = [
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ]
        odsFilePathString = TestUtils.create_ods_with_data(data_table, "ods_")
        self.generatedOds = odsFilePathString
        with self.assertRaises(DatabaseNotExistsException):
            sqlWritterFromExcel.write("some_database", odsFilePathString)

    def test_write_one_line(self):
        sqlWritterFromExcel = SqlWritterFromExcel(self.mysqlConfiguration)
        data_table = [
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ]
        odsFilePathString = TestUtils.create_ods_with_data(data_table, "ods_")
        database_name = "database_" + Utils.generate_friendly_date_string()
        Utils.create_database(database_name, self.mySqlDriver)
        self.generatedDatabase = database_name
        results = sqlWritterFromExcel.write(database_name, odsFilePathString)
        os.remove(odsFilePathString)
        created_rows = self._count_registers(results.database_created, results.tables_created[0])
        self.assertEqual(created_rows, 1)

    def test_write_three_line(self):
        sqlWritterFromExcel = SqlWritterFromExcel(self.mysqlConfiguration)
        odsFilePathString = self._create_ods()
        database_name = "database_" + Utils.generate_friendly_date_string()
        Utils.create_database(database_name, self.mySqlDriver)
        self.generatedDatabase = database_name
        sqlWritterFromExcel.write(database_name, odsFilePathString)
        os.remove(odsFilePathString)

    def test_check_tables_based_on_spreadsheet(self):
        table1_name = "first_spreadsheet"
        self.generatedDatabase = "database_" + Utils.generate_friendly_date_string()

        Utils.create_database(self.generatedDatabase, self.mySqlDriver)
        print("@" + self.generatedDatabase + "@")

        data_to_create_table = [[1,2,3],[4,5,6],[7,8,9]]
        created_ods = self._create_ods_with_data(data_to_create_table, table1_name)
        print(created_ods)

        sqlWritterFromExcel = SqlWritterFromExcel(self.mysqlConfiguration)
        sqlWritterFromExcel.write(self.generatedDatabase, created_ods)

        self.assertTrue(self._check_table_exists(table1_name, self.generatedDatabase))

    def _create_ods(self):
        data_to_create_table = [[1,2,3],[4,5,6],[7,8,9]]
        return self._create_ods_with_data(data_to_create_table)

    def _check_table_exists(self, table_name, database_name):
        mysql_driver = MySqlDriver()
        mysql_driver.exec(f"USE {database_name}")
        query_list_tables = f"SHOW TABLES LIKE 'table_name';"

        return False

