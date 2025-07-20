from .MySqlConfiguration import MySqlConfiguration

class MySqlDriver:
    def __init__(self):
        self.mysql_configuration = None
    
    def set_database_configuration(self, mysql_configuration: MySqlConfiguration):
        """Set the MySQL database configuration."""
        self.mysql_configuration = mysql_configuration