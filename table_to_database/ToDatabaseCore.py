from .ToDatabaseInterface import ToDatabaseInterface
from .Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
import os
import pandas as pd
from .Utils import Utils
from .MySqlConfiguration import MySqlConfiguration
from .MySqlDriver import MySqlDriver
from .SqlWritterFromExcel import SqlWritterFromExcel
from .CreationResult import CreationResult

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

    def to_database(self, database_name: str = None) -> CreationResult:
        self._check_for_errors()
        if database_name:
            database_name = "database_" + Utils.generate_friendly_date_string()
            self.database_name = database_name
        Utils.create_database(database_name, self.database_driver)
        table_name = "Sheet1"
        return self._write_to_database(database_name, table_name)

    def set_file(self, file_path: str) -> CreationResult:
        """Set the file path for the table to be converted."""
        self.file_path = file_path
        
    def _write_to_database(self, database_name: str, table_name: str):
        """Write the data from the file to the database."""
        if not self.file_path or not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        sql_writer = SqlWritterFromExcel(self.database_configuration)
        return sql_writer.write(database_name, self.file_path)
        
    def _check_for_errors(self):
        if not self.file_path:
            raise ValueError("File path is not set.")
        
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        if self.database_configuration is None:
            raise MissingDatabaseConfigurationException()
        
    # def _create_database(self, database_name):
    #     """Create the database if it does not exist."""
    #     self.database_driver.exec(f"CREATE DATABASE IF NOT EXISTS {database_name};")
        
