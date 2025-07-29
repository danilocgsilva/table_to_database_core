import os
from table_to_database.MySqlConfiguration import MySqlConfiguration
from pyexcel_ods import save_data
from table_to_database.Utils import Utils

class TestUtils:
    @staticmethod
    def get_test_db_configuration():
        """Get the test database configuration from environment variables."""
        database_configuration = MySqlConfiguration()
        database_configuration.database = os.environ.get("TEST_DB_NAME")
        database_configuration.user = os.environ.get("TEST_DB_USER")
        database_configuration.password = os.environ.get("TEST_DB_PASSWORD")
        database_configuration.host = os.environ.get("TEST_DB_HOST")
        return database_configuration
        
        
    @staticmethod
    def create_empty_odf_file(prefix = "") -> str:
        data = {}
        filename = prefix + Utils.generate_friendly_date_string() + ".ods"
        save_data(filename, data)
        return filename