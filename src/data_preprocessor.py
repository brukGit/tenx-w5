# src/data_preprocessor.py

import pandas as pd

class DataPreprocessor:
    @staticmethod
    def preprocess_data(input_file, output_file):
        df = pd.read_csv(input_file)
        
        # Convert date to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Basic text cleaning
        df['Message'] = df['Message'].fillna('').str.lower().str.strip()
        
        # Save preprocessed data
        df.to_csv(output_file, index=False)
        print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    input_file = 'data/raw/telegram_data.csv'
    output_file = 'data/processed/preprocessed_data.csv'
    DataPreprocessor.preprocess_data(input_file, output_file)