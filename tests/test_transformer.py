# tests/test_transformer.py

import unittest
import pandas as pd
from etl.transformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    def setUp(self):
        self.transformer = DataTransformer()

    def test_convert_pace(self):
        pace = self.transformer.convert_pace(2.78)  # Approx 6:00 min/km
        self.assertEqual(pace, "6:00/km")

    def test_transform(self):
        df = pd.DataFrame({
            "Moving Time": [300, 600],
            "Elapsed time": [400, 700],
            "Distance": [1000, 2000],
            "Pace": [2.78, 3.33]
        })
        transformed_df = self.transformer.transform(df, "athlete123")
        self.assertIn("AthleteId", transformed_df.columns)
        self.assertEqual(transformed_df.iloc[0]["AthleteId"], "athlete123")

if __name__ == "__main__":
    unittest.main()
