class DatabaseNotExistsException(Exception):
    """Exception raised when the database does not exist."""
    
    def __init__(self, message="Database does not exist. Please create the database before proceeding."):
        self.message = message
        super().__init__(self.message)