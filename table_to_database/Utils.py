from pyexcel_ods import save_data
from datetime import datetime
from collections import OrderedDict 

class Utils:    
    @staticmethod
    def create_empty_odf_file(prefix = "") -> str:
        data = {}
        filename = prefix + Utils.generate_friendly_date_string() + ".ods"
        save_data(filename, data)
        return filename
    
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