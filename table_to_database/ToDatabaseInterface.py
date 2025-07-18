import abc

class ToDatabaseInterface(abc.ABC):

    @abc.abstractmethod
    def to_database(self):
        pass

    @abc.abstractmethod
    def set_file(self, file_path: str):
        """Set the file path for the table to be converted."""
        pass

