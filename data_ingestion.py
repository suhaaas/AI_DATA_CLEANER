import os
import pandas as pd
import requests
from sqlalchemy import create_engine

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')

class DataIngestion:
    def __init__(self, db_url=None):
        self.engine = create_engine(db_url) if db_url else None

    def load_csv(self, file_path):
        """Load data from a CSV file."""
        file_path = os.path.join(DATA_DIR, file_path)
        try:
            df = pd.read_csv(file_path)
            print(f"Loaded data from {file_path}")
            return df
        except Exception as e:
            print(f"Error loading CSV file {file_path}: {e}")
            return None
        
    def load_excel(self, file_path):
        """Load data from an Excel file."""
        file_path = os.path.join(DATA_DIR, file_path)
        try:
            df = pd.read_excel(file_path,sheet_name=None)
            print(f"Loaded data from {file_path}")
            return df
        except Exception as e:
            print(f"Error loading Excel file {file_path}: {e}")
            return None
        
    def connect_database(self,db_url):
        """Connect to a database using SQLAlchemy."""
        try:
            self.engine = create_engine(db_url)
            #connection = self.engine.connect()
            print("Database connection is successful.")
            #connection.close()
        except Exception as e:
            print(f"Error connecting to database: {e}")
            #self.engine = None

    def load_from_database(self, query):
        """Load data from a database using a SQL query."""
        if not self.engine:
            print("Database engine is not initialized.")
            return None
        try:
            df = pd.read_sql_query(query, self.engine)
            print("Data loaded from database.")
            return df
        except Exception as e:
            print(f"Error loading data from database: {e}")
            return None
        

    def fetch_from_api(self, api_url,params=None):  
        """Fetch data from a REST API."""
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                df = pd.json_normalize(data)
                print(f"Data fetched from API: {api_url}")
                return df
            else:
                print(f"Error fetching data from API: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching data from API: {e}")
            return None