# etl/extractor.py

import pandas as pd
from abc import ABC, abstractmethod

class DataExtractor(ABC):
    @abstractmethod
    def extract(self, file_path: str) -> pd.DataFrame:
        pass

class CSVDataExtractor(DataExtractor):
    def extract(self, file_path: str) -> pd.DataFrame:
        df = pd.read_csv(file_path)
        print(f"Data extracted successfully from {file_path}.")
        return df
