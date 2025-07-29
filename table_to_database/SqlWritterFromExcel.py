import pandas as pd
from sqlalchemy import create_engine, text
from .MySqlConfiguration import MySqlConfiguration

class SqlWritterFromExcel:
    mysql_connection: MySqlConfiguration
    def __init__(self, mysql_connection: MySqlConfiguration):
        if mysql_connection is None:
            raise ValueError("You must assign a mysql configuration to the SqlWritterFromExcel.")
        self.mysql_connection = mysql_connection

    def write(self, database_name: str, table_file_path: str):
        """Write data to the database."""
        table_name = "datasheet"
        
        df = pd.read_excel(table_file_path, engine='odf')
        
        df.to_sql(
            table_name,
            con=self.get_engine(database_name),
            if_exists='replace',
            index=False
        )
        
    def get_engine(self, database_name: str):
        
        string_for_connection = (
            f"mysql+mysqlconnector://{self.mysql_connection.user}:"
            f"{self.mysql_connection.password}@"
            f"{self.mysql_connection.host}:3306/{database_name}"
        )
        
        return create_engine(string_for_connection)
