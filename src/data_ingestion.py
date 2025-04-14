import os
import pandas as pd
from sklearn.model_selection import train_test_split
from utils.logger import logging, logger

def load_data(data_url):
    """
    Load the data from the given URL.
    """
    try:
        data = pd.read_csv(data_url)
        logger.info("Data loaded successfully")
        return data
    except Exception as e:
        logging()
        logger.warning("Exitting the program ....")
        exit()

def preprocess_data(data):
    """
    Preprocess the data by removing duplicates and null values.
    """
    try:
        # Drop all the columns having str unnamed in their name
        data = data.loc[:, ~data.columns.str.contains('^Unnamed')] 
        data.rename(columns={'v1': 'label', 'v2': 'text'}, inplace=True)
        data = data.drop_duplicates()
        data = data.dropna()
        logger.info("Data preprocessed successfully")
        return data
    except Exception as e:
        logging()
        logger.warning("Exitting the program ....")
        exit()

