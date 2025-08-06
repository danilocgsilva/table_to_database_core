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
        
        table_name = "datasheet"
        df = pd.read_excel(table_file_path, engine='odf')
        df.to_sql(
            table_name,
            con=self.get_engine(database_name),
            if_exists='replace',
            index=False
        )

        return CreationResult(True, [table_name], database_name)
        
    def get_engine(self, database_name: str):
        string_for_connection = (
            f"mysql+mysqlconnector://{self.mysql_connection.user}:"
            f"{self.mysql_connection.password}@"
            f"{self.mysql_connection.host}:3306/{database_name}"
        )
        
        return create_engine(string_for_connection)
