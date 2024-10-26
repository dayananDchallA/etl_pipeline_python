# etl/pipeline.py

import os
from etl.extractor import DataExtractor
from etl.transformer import DataTransformer
from etl.loader import DataLoader

class ETLPipeline:
    def __init__(self, extractor: DataExtractor, transformer: DataTransformer, loader: DataLoader, data_folder: str):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.data_folder = data_folder

    def run(self):
        for file_name in os.listdir(self.data_folder):
            if file_name.endswith("_activities.csv") and len(file_name) == 22:
                athlete_id = file_name.split("_activities")[0]
                file_path = os.path.join(self.data_folder, file_name)
                
                # Extract
                df = self.extractor.extract(file_path)
                
                # Transform
                df_transformed = self.transformer.transform(df, athlete_id)
                
                # Load
                self.loader.load(df_transformed)
