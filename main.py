# main.py

from config.config import SERVER_NAME, DATABASE_NAME, DATA_FOLDER
from db.connection import DatabaseConnection
from etl.extractor import CSVDataExtractor
from etl.transformer import DataTransformer
from etl.loader import DataLoader
from etl.pipeline import ETLPipeline

def main():
    db_connection = DatabaseConnection(SERVER_NAME, DATABASE_NAME)
    engine = db_connection.connect()
    
    extractor = CSVDataExtractor()
    transformer = DataTransformer()
    loader = DataLoader(engine)
    
    etl_pipeline = ETLPipeline(extractor, transformer, loader, DATA_FOLDER)
    etl_pipeline.run()

if __name__ == "__main__":
    main()
