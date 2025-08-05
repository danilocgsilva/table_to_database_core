class CreationResult:
    def __init__(self, success: bool, tables_created: list, database_created: str):
        self._success = success
        self._tables_created = tables_created
        self._database_created = database_created
    
    @property
    def success(self) -> bool:
        return self._success
    
    @success.setter
    def success(self, value):
        self._success = value

    @property
    def tables_created(self) -> list:
        return self._tables_created
    
    @tables_created.setter
    def tables_created(self, value):
        self._tables_created = value

    @property
    def database_created(self) -> str:
        return self._database_created

    @database_created.setter
    def database_created(self, value):
        self._database_created = value
