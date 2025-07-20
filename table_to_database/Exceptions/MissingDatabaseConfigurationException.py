class MissingDatabaseConfigurationException(Exception):
    """Exception raised when the database configuration is missing."""
    
    def __init__(self, message="Database configuration is missing."):
        self.message = message
        super().__init__(self.message)