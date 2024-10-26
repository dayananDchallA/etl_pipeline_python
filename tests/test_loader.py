# tests/test_loader.py

import unittest
import pandas as pd
from unittest.mock import MagicMock
from etl.loader import DataLoader
from sqlalchemy import create_engine

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.mock_engine = create_engine('sqlite:///:memory:')  # Use in-memory SQLite for testing
        self.loader = DataLoader(self.mock_engine)

    def test_load_data(self):
        df = pd.DataFrame({
            "ActivityId": [1, 2],
            "AthleteId": ["athlete123", "athlete123"]
        })
        self.loader.load(df)
        # Verify data in SQL (e.g., count rows or query data in SQLite)
        with self.mock_engine.connect() as conn:
            result = conn.execute("SELECT COUNT(*) FROM FitnessData").fetchone()[0]
            self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
