import pandas as pd
import numpy as np


class DataCleaning:
    def handle_missing_values(self, df, strategy='mean'):
        """Handle missing values in the DataFrame."""
        if strategy == 'mean':
            df.fillna(df.mean(numeric_only=True), inplace=True)
        elif strategy == 'median':
            df.fillna(df.median(numeric_only=True), inplace=True)
        elif strategy == 'mode':
            df.fillna(df.mode().iloc[0], inplace=True)
        elif strategy == 'drop':
             df.dropna(inplace=True)
        return df
        

    def remove_duplicates(self, df):
        """Remove duplicate rows from the DataFrame."""
        return df.drop_duplicates() 

    def fix_data_types(self, df):
        """Fix data types of specified columns in the DataFrame."""
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                pass
        return df

    def clean_data(self,df): 
        """Perform a series of cleaning steps on the DataFrame."""
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.fix_data_types(df)
        return df


