import pandas as pd

class OdsToDataset:
    ods_file_path: str
    def __init__(self, ods_file_path: str):
        self.ods_file_path = ods_file_path

    def to_dataset(self):
        return pd.read_excel(self.ods_file_path, engine='odf')
    