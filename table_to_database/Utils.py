from pyexcel_ods import save_data
from datetime import datetime
from collections import OrderedDict 

class Utils:    
    def create_ods_file_with_order_dict(self, order_dict: OrderedDict) -> str:
        """
        Creates an ODS file with the provided order dictionary.
        """
        filename = "/tmp/" + Utils.generate_friendly_date_string() + ".ods"
        save_data(filename, order_dict)
        return filename
        
    @staticmethod
    def generate_friendly_date_string():
        """
        Generates a friendly date string for testing purposes.
        """
        return datetime.now().strftime("%Y_%m_%d_%H%M%S")
    
    @staticmethod
    def create_database(database_name, database_driver):
        """Create the database if it does not exist."""
        database_driver.exec(f"CREATE DATABASE IF NOT EXISTS {database_name};")