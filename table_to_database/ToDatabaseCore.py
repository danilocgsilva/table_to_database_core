from .ToDatabaseInterface import ToDatabaseInterface
from .Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
import os
import pandas as pd
from .Utils import Utils
from .MySqlConfiguration import MySqlConfiguration
from .MySqlDriver import MySqlDriver
from .SqlWritterFromExcel import SqlWritterFromExcel

class ToDatabaseCore(ToDatabaseInterface):
    file_path: str
    database_configuration: MySqlConfiguration
    database_driver: MySqlDriver
    database_name: str
    def __init__(self):
        self.file_path = None
        self.database_configuration = None
        self.database_driver = None
        
    def set_database_configuration(self, database_configuration: MySqlConfiguration):
        self.database_configuration = database_configuration
        self.database_driver = MySqlDriver()
        self.database_driver.set_database_configuration(database_configuration)

    def to_database(self, database_name: str = None):
        self._check_for_errors()
        if database_name:
            database_name = "database_" + Utils.generate_friendly_date_string()
            self.database_name = database_name
        self._create_database(database_name)
        
    def set_file(self, file_path: str):
        """Set the file path for the table to be converted."""
        self.file_path = file_path
        
    # def write_to_database(self):
    #     sqlWritterFromExcel = SqlWritterFromExcel(self.database_configuration)
    #     # print("-------")
    #     # print(self.file_path)
    #     # print("-------")
    #     sqlWritterFromExcel.write(self.database_name, self.file_path)
        
    def _check_for_errors(self):
        if not self.file_path:
            raise ValueError("File path is not set.")
        
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        if self.database_configuration is None:
            raise MissingDatabaseConfigurationException()
        
    def _create_database(self, database_name):
        """Create the database if it does not exist."""
        self.database_driver.exec(f"CREATE DATABASE IF NOT EXISTS {database_name};")
        
