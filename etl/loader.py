# etl/loader.py

from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

class DataLoader:
    def __init__(self, engine):
        self.engine = engine

    def load(self, df: pd.DataFrame):
        try:
            df.to_sql('FitnessData', con=self.engine, if_exists='append', index=False)
            print(f"Loaded data for activities with IDs: {df['ActivityId'].tolist()}")
        except SQLAlchemyError as e:
            print(f"Error while inserting data: {e}")
