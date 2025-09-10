import pandas as pd
from sqlalchemy import create_engine, text
from .MySqlConfiguration import MySqlConfiguration
from .CreationResult import CreationResult
from .Exceptions.DatabaseNotExistsException import DatabaseNotExistsException
from .Utils import Utils
from table_to_database.MySqlDriver import MySqlDriver

class SqlWritterFromExcel:
    mysql_connection: MySqlConfiguration
    def __init__(self, mysql_connection: MySqlConfiguration):
        if mysql_connection is None:
            raise ValueError("You must assign a mysql configuration to the SqlWritterFromExcel.")
        self.mysql_connection = mysql_connection

    def write(self, database_name: str, table_file_path: str):
        """Write data to the database."""
        
        if Utils.databaseExists(database_name, self.mysql_connection) == False:
            raise DatabaseNotExistsException()
        
        sheets_names = self._getSheetsNames(table_file_path)
        
        for sheet_name in sheets_names:
            df = pd.read_excel(table_file_path, sheet_name=sheet_name, engine='odf')
            df.to_sql(
                sheet_name,
                con=self.get_engine(database_name),
                if_exists='replace',
                index=False
            )
        return CreationResult(True, sheets_names, database_name, True)
        
        
    def get_engine(self, database_name: str):
        string_for_connection = (
            f"mysql+mysqlconnector://{self.mysql_connection.user}:"
            f"{self.mysql_connection.password}@"
            f"{self.mysql_connection.host}:3306/{database_name}"
        )
        
        return create_engine(string_for_connection)
    
    def _getSheetsNames(self, excel_file_path):
        excel_file_data = pd.ExcelFile(excel_file_path)
        excel_file_data.close()
        return excel_file_data.sheet_names
            

