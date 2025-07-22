class DriverNotSettedException(Exception):
    """Exception raised when the database driver is not set."""
    
    def __init__(self, message="Database driver is not set."):
        self.message = message
        super().__init__(self.message)
