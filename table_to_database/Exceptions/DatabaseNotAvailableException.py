class DatabaseNotAvailableException(Exception):
    """Exception raised when the database is not available."""
    
    def __init__(self, message="Database is not available. Check your connection settings."):
        self.message = message
        super().__init__(self.message)
