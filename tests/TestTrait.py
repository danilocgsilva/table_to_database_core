from table_to_database.MySqlDriver import MySqlDriver
from .TestUtils import TestUtils

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
