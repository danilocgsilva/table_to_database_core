from table_to_database.MySqlDriver import MySqlDriver
from .TestUtils import TestUtils
from collections import OrderedDict
from pyexcel_ods import save_data
from table_to_database.Utils import Utils

class TestTrait:
    def _count_registers(self, database_name: str, table_name) -> int:
        """Count the number of registers in the database."""
        mysql_driver = MySqlDriver()
        mysql_driver.set_database_configuration(TestUtils.get_test_db_configuration())

        mysql_driver.exec(f"USE {database_name};")
        
        try:
            result = mysql_driver.exec(f"SELECT COUNT(*) FROM {table_name};")
            counting = result[0][0]
            return int(counting)
        except Exception as e:
            print(f"Error counting registers: {e}")

    def _create_ods_with_data(self, data_from_list, sheet_name = None):
        file_name_path = "generic_table_file_" + Utils.generate_friendly_date_string() + ".ods"
        order_dict = OrderedDict()
        print(sheet_name)
        if sheet_name is None:
            sheet_name = "Sheet 1"
        order_dict.update({sheet_name: data_from_list})
        save_data(file_name_path, order_dict)
        return file_name_path
