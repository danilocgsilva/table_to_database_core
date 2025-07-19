from ..ToDatabaseCore import ToDatabaseCore
import os

class ToDatabase:
    def __init__(self):
        self.to_database_core = ToDatabaseCore()

    def to_database(self):
        self.to_database_core.to_database()

    def set_file(self, file_path: str):
        self.to_database_core.set_file(file_path)
        