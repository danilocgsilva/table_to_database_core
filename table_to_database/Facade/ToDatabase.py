from ..ToDatabaseCore import ToDatabaseCore
from ..MySqlConfiguration import MySqlConfiguration
from ..MySqlDriver import MySqlDriver
from ..Exceptions.DriverNotSettedException import DriverNotSettedException
from ..Exceptions.MissingDatabaseConfigurationException import MissingDatabaseConfigurationException
from ..SqlWritterFromExcel import SqlWritterFromExcel

class ToDatabase:
    to_database_core: ToDatabaseCore
    database_configuration: MySqlConfiguration
    def __init__(self, to_database_core: ToDatabaseCore):
        self.to_database_core = to_database_core
        self.database_configuration = None
        
    def set_database_configuration(self, database_configuration: MySqlConfiguration):
        self.database_configuration = database_configuration
        return self

    def to_database(self, database_name: str = None):
        self.to_database_core.set_database_configuration(self.database_configuration)
        try:
            self.to_database_core.to_database(database_name)
        except DriverNotSettedException as e:
            raise MissingDatabaseConfigurationException()
        self.to_database_core.to_database()

    def set_excel_file(self, file_path: str):
        self.to_database_core.set_file(file_path)
        
    def set_database_host(self, host: str):
        """Set the database host."""
        if not host:
            raise ValueError("Database host cannot be empty.")
        self.database_configuration.host = host
        
    def set_database_user(self, user: str):
        """Set the database user."""
        if not user:
            raise ValueError("Database user cannot be empty.")
        self.database_configuration.user = user
        
    def set_database_password(self, password: str):
        """Set the database password."""
        if not password:
            raise ValueError("Database password cannot be empty.")
        self.database_configuration.password = password
        