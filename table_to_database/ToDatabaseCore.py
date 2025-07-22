from .ToDatabaseInterface import ToDatabaseInterface
from .Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
import os
import pandas as pd
from .Utils import Utils
from sqlalchemy import create_engine

class ToDatabaseCore(ToDatabaseInterface):
    def __init__(self):
        self.file_path = None
        self.database_driver = None
        self.database_configuration = None
        
    def set_database_configuration(self, database_configuration):
        self.database_configuration = database_configuration

    def to_database(self):
        self._check_for_errors()
        
        database_name = "database_" + Utils.generate_friendly_date_string()
        
        self._create_database(database_name)
        
        # pd.read_excel(self.file_path, engine='openpyxl').to_sql(
        #     name=table_name,
        #     con=self.database_configuration.get_connection(),
        #     if_exists='replace',
        #     index=False
        # )
        
    def set_file(self, file_path: str):
        """Set the file path for the table to be converted."""
        self.file_path = file_path
        
    def _check_for_errors(self):
        if not self.file_path:
            raise ValueError("File path is not set.")
        
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        if self.database_configuration is None:
            raise MissingDatabaseConfigurationException()
        
    def _create_database(self, database_name):
        """Create the database if it does not exist."""
        engine = self.get_engine()
        with engine.connect() as connection:
            connection.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        
    def get_engine(self):
        """Get the SQLAlchemy engine for the database."""
        if self.database_configuration is None:
            raise MissingDatabaseConfigurationException()
        
        db_user = self.database_configuration.get_user()
        db_password = self.database_configuration.get_password()
        db_host = self.database_configuration.get_host()
        db_port = self.database_configuration.get_port()
        
        return create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/")
        
