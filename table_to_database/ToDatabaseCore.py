from .ToDatabaseInterface import ToDatabaseInterface
from .Exceptions.DriverNotSettedException import DriverNotSettedException
import os

class ToDatabaseCore(ToDatabaseInterface):
    def __init__(self):
        self.file_path = None
        self.database_driver = None
        
    def set_database_driver(self, driver):
        self.database_driver = driver

    def to_database(self):
        if not self.file_path:
            raise ValueError("File path is not set.")
        
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        if self.database_driver is None:
            raise DriverNotSettedException()
        
    def set_file(self, file_path: str):
        """Set the file path for the table to be converted."""
        self.file_path = file_path
