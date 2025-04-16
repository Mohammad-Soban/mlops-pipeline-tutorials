import os
import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
from utils.logger import log_exception, logger

def load_params(path):
    """
    Load parameters from the given YAML file.
    """
    try:
        with open(path, 'r') as file:
            params = yaml.safe_load(file)
        return params
    except Exception as e:
        log_exception()
        logger.warning("Unable to load params.yaml file")
        exit()


def load_data(data_url):
    """
    Load the data from the given URL.
    """
    try:
        data = pd.read_csv(data_url)
        logger.info("Data loaded successfully")
        return data
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()

def clean_data(data):
    """
    Preprocess the data by removing duplicates and null values.
    """
    try:
        # Drop all the columns having str unnamed in their name
        data = data.loc[:, ~data.columns.str.contains('^Unnamed')] 
        data = data.rename(columns={'v1': 'label', 'v2': 'text'})
        data = data.drop_duplicates(keep = 'first')
        data = data.dropna()
        logger.info("Data preprocessed successfully")
        return data
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()

def save_data(train_data, test_data, data_path):
    """
    Saves the train and test data into a new directory named raw inside the data_path.
    """
    try:
        raw_data_path = os.path.join(data_path, 'raw')
        os.makedirs(raw_data_path, exist_ok=True)
        
        train_data_path = os.path.join(raw_data_path, 'train.csv')
        train_data.to_csv(train_data_path, index=False)
        logger.info(f"Train data saved to {train_data_path}")

        test_data_path = os.path.join(raw_data_path, 'test.csv')
        test_data.to_csv(test_data_path, index=False)
        logger.info(f"Test data saved to {test_data_path}")

    except Exception as e:
        log_exception()
        logger.warning("Unable to save train and test data....")

def main():
    """
    Main function to load, preprocess, split and save the data.    
    """
    try:
        params = load_params('params.yaml')
        test_size = params['data_ingestion']['test_size']
        random_state = params['data_ingestion']['random_state']
        data_url = "https://raw.githubusercontent.com/Mohammad-Soban/mlops-pipeline-tutorials/refs/heads/main/experiments/spam.csv"

        data = load_data(data_url)
        data = clean_data(data)
        
        train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
        
        save_data(train_data, test_data, './data')
    
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit() 

if __name__ == '__main__':
    main()