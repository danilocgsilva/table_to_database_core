from table_to_database.ToDatabaseInterface import ToDatabaseInterface
import os

class ToDatabase(ToDatabaseInterface):
    def __init__(self):
        self.file_path = None

    def to_database(self):
        if not self.file_path:
            raise ValueError("File path is not set.")
        
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        print(f"Converting {self.file_path} to database...")

    def set_file(self, file_path: str):
        """Set the file path for the table to be converted."""
        self.file_path = file_path