from pyexcel_ods import save_data
from datetime import datetime

class Utils:    
    @staticmethod
    def create_empty_odf_file() -> str:
        # Create an empty dictionary (represents empty sheets)
        data = {}
        filename = "/tmp/" + Utils.generate_friendly_date_string() + ".ods"
        save_data(filename, data)
        return filename
        
    @staticmethod
    def generate_friendly_date_string():
        """
        Generates a friendly date string for testing purposes.
        """
        return datetime.now().strftime("%Y_%m_%d_%H%M%S")