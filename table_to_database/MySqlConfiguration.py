from typing import Optional

class MySqlConfiguration:
    def __init__(self):
        self._host: Optional[str] = None
        self._user: Optional[str] = None
        self._password: Optional[str] = None
        self._database: Optional[str] = None
        
    @property
    def host(self) -> Optional[str]:
        return self._host
    
    @host.setter
    def host(self, value: str):
        self._host = value
        
    @property
    def user(self) -> Optional[str]:
        return self._user
    
    @user.setter
    def user(self, value: str):
        self._user = value
        
    @property
    def password(self) -> Optional[str]:
        return self._password
    
    @password.setter
    def password(self, value: str):
        self._password = value
        
    @property
    def database(self) -> Optional[str]:
        return self._database

    @database.setter
    def database(self, value: str):
        self._database = value
        
    def is_ready(self) -> bool:
        """Gently check if the MySQL configuration is complete without breaking the application."""
        if not self._host or not self._user or not self._password:
            return False
        return True
        
    def ready(self):
        """Halts the application if the MySQL configuration is not complete."""
        if not self.is_ready():
            raise ValueError("MySQL configuration is not complete. Please set host, user, and password.")
        
