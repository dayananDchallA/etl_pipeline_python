# db/connection.py

from sqlalchemy import create_engine

class DatabaseConnection:
    def __init__(self, server_name: str, database_name: str):
        self.server_name = server_name
        self.database_name = database_name
        self.engine = None

    def connect(self):
        conn_string = f'mssql+pyodbc://{self.server_name}/{self.database_name}?driver=ODBC+Driver+17+for+SQL+Server'
        self.engine = create_engine(conn_string)
        return self.engine
