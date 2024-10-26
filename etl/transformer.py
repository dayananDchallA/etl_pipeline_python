# etl/transformer.py

import pandas as pd

class DataTransformer:
    @staticmethod
    def convert_pace(speed_m_per_s: float) -> str:
        speed_km_per_min = speed_m_per_s * 60 / 1000
        minutes_per_km = 1 / speed_km_per_min
        minutes = int(minutes_per_km)
        seconds = round((minutes_per_km - minutes) * 60)
        if seconds == 60:
            minutes += 1
            seconds = 0
        return f"{minutes}:{seconds:02d}/km"

    def transform(self, df: pd.DataFrame, athlete_id: str) -> pd.DataFrame:
        df['Moving Time'] = df['Moving Time'] / 60
        df['Elapsed time'] = df['Elapsed time'] / 60
        df['Distance'] = df['Distance'] / 1000
        df['Pace'] = df['Pace'].apply(self.convert_pace)
        
        # Rounding
        rounding_columns = ['Intensity', 'Avg Altitude', 'Avg HR%', 'Max HR%', 'Max Altitude', 'Distance', 'Moving Time', 'Elapsed time']
        df[rounding_columns] = df[rounding_columns].round(2)
        
        df['athlete_id'] = athlete_id

        # Rename columns to match SQL schema
        df.rename(columns={
            'athlete_id': 'AthleteId',
            'id': 'ActivityId',
            'Intensity': 'IntensityPercent',
            'Moving Time': 'MovingTime',
            'Elapsed time': 'ElapsedTime',
            'Avg Altitude': 'AvgAltitude',
            'Avg HR%': 'AvgHRPercent',
            'Max HR%': 'MaxHRPercent',
            'Max Altitude': 'MaxAltitude',
            'Max HR': 'MaxHR',
            'HRRc': 'HRRc',
            'Avg HR': 'AvgHR'
        }, inplace=True)
        
        print(f"Transformed data for athlete {athlete_id}.")
        return df
