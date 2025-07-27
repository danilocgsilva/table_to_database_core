from .MySqlConfiguration import MySqlConfiguration
import mysql.connector

class MySqlDriver:
    def __init__(self):
        self.mysql_configuration = None
    
    def set_database_configuration(self, mysql_configuration: MySqlConfiguration):
        """Set the MySQL database configuration."""
        self.mysql_configuration = mysql_configuration
        
    def exec(self, query: str):
        """Execute a SQL query on the MySQL database."""
        self._check_mysql_configuration()
        
        connection = mysql.connector.connect(
            host=self.mysql_configuration.host,
            user=self.mysql_configuration.user,
            password=self.mysql_configuration.password
        )
        myresult = self._run_query(query, connection)
        connection.close()
        return myresult
    
    def exec_with_connection(self, query: str, connection):
        """Execute a SQL query with an existing connection."""
        myresult = self._run_query(query, connection)
        return myresult
    
    def _run_query(self, query: str, connection):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            return result
        finally:
            cursor.close()
        
    def _check_mysql_configuration(self) -> None:
        if not self.mysql_configuration:
            raise ValueError("Database configuration is not set.")
        