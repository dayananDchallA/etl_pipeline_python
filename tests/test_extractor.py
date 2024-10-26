# tests/test_extractor.py

import unittest
import pandas as pd
from etl.extractor import CSVDataExtractor

class TestCSVDataExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = CSVDataExtractor()

    def test_extract_valid_file(self):
        # Assuming 'data/test_activities.csv' exists and is a valid CSV file
        df = self.extractor.extract("data/test_activities.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_extract_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            self.extractor.extract("data/non_existing_file.csv")

if __name__ == "__main__":
    unittest.main()
