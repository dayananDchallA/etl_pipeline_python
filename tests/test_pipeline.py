# tests/test_pipeline.py

import unittest
from unittest.mock import MagicMock
from etl.extractor import CSVDataExtractor
from etl.transformer import DataTransformer
from etl.loader import DataLoader
from etl.pipeline import ETLPipeline

class TestETLPipeline(unittest.TestCase):
    def setUp(self):
        self.extractor = MagicMock(spec=CSVDataExtractor)
        self.transformer = MagicMock(spec=DataTransformer)
        self.loader = MagicMock(spec=DataLoader)
        self.pipeline = ETLPipeline(self.extractor, self.transformer, self.loader, "data/")

    def test_pipeline_run(self):
        # Mock data
        mock_df = MagicMock()
        self.extractor.extract.return_value = mock_df
        self.transformer.transform.return_value = mock_df

        # Run the pipeline
        self.pipeline.run()

        # Verify calls
        self.extractor.extract.assert_called()
        self.transformer.transform.assert_called()
        self.loader.load.assert_called_with(mock_df)

if __name__ == "__main__":
    unittest.main()
