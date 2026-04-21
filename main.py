import pandas as pd
import numpy as np
import logging
import os

# Professional Logging Setup (Standard in UK/US firms)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FraudDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Loads dataset with error handling."""
        if not os.path.exists(self.file_path):
            logging.error(f"File not found at {self.file_path}")
            return None
        
        try:
            self.df = pd.read_csv(self.file_path)
            logging.info(f"Dataset loaded successfully. Shape: {self.df.shape}")
            return self.df
        except Exception as e:
            logging.error(f"Unexpected error during loading: {e}")
            return None

    def perform_initial_audit(self):
        """Professional data integrity check."""
        if self.df is None:
            return
        
        print("\n" + "="*30)
        print(" DATA INTEGRITY AUDIT")
        print("="*30)
        
        # 1. Missing Values Check
        null_count = self.df.isnull().sum().sum()
        logging.info(f"Total Missing Values: {null_count}")

        # 2. Class Imbalance (The Fraud Detection Challenge)
        fraud_share = (self.df['Class'].value_counts(normalize=True) * 100).to_dict()
        print(f"\n Class Distribution:")
        print(f"   - Legit Transactions (0): {fraud_share[0]:.4f}%")
        print(f"   - Fraud Transactions (1): {fraud_share[1]:.4f}%")

        # 3. Financial Metrics Audit (Amount column)
        print(f"\n Financial Summary (Amount):")
        stats = self.df['Amount'].describe()
        print(f"   - Mean: ${stats['mean']:.2f}")
        print(f"   - Max:  ${stats['max']:.2f}")
        
        print("="*30 + "\n")

# --- Execution ---
if __name__ == "__main__":
    # Path ko apne environment ke mutabiq set karein
    DATA_PATH = 'creditcard.csv' 
    
    processor = FraudDataProcessor(DATA_PATH)
    data = processor.load_data()
    
    if data is not None:
        processor.perform_initial_audit()