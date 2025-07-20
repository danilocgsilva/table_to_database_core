from pyexcel_ods import save_data
from datetime import datetime

class TestUtils:
    # @staticmethod
    # def get_test_data_path():
    #     """
    #     Returns the path to the test data directory.
    #     """
    #     import os
    #     return os.path.join(os.path.dirname(__file__), 'test_data')

    # @staticmethod
    # def get_test_file_path(filename):
    #     """
    #     Returns the full path to a test file given its filename.
    #     """
    #     import os
    #     return os.path.join(TestUtils.get_test_data_path(), filename)
    
    @staticmethod
    def create_empty_odf_file() -> str:
        # Create an empty dictionary (represents empty sheets)
        data = {}
        filename = "/tmp/" + TestUtils.generate_friendly_date_string() + ".ods"
        save_data(filename, data)
        return filename
        
    @staticmethod
    def generate_friendly_date_string():
        """
        Generates a friendly date string for testing purposes.
        """
        return datetime.now().strftime("%Y-%m-%d_%H%M%S")