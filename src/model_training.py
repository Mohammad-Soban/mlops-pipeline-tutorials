import pandas as pd
import numpy as np
import pickle
import yaml
import os
from sklearn.ensemble import RandomForestClassifier
from utils.logger import log_exception, logger
from utils.loader import load_params


def load_data(file_path):
    """
    Load the data from the given file path.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


def train_model(X_train, y_train, params):
    """
    Train the model based on the parameters
    """

    try:
        if X_train is None or y_train is None or (X_train.shape[0] != y_train.shape[0]):
            raise ValueError("X_train and y_train should be equal in lenght and should not be None")
        
        rf = RandomForestClassifier(n_estimators=params['n_estimators'], random_state=params['random_state'])
        rf.fit(X_train, y_train)

        logger.info("Model trained successfully")

        return rf
    
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


def save_model(model, path):
    """
    Save the model to the given path.
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'wb') as file:
            pickle.dump(model, file)
        
        logger.info('Model Saved to path: %s', path)

    except Exception as e:
        log_exception()
        logger.warning("Could not save the model")
        exit()


def main():
    try:
        params = load_params('params.yaml')['model_training']
        
        train_data = load_data('./data/transformed/train_tfidf.csv')
        X_train = train_data.iloc[:, :-1].values
        y_train = train_data.iloc[:, -1].values

        rf = train_model(X_train, y_train, params)
        model_path = 'models/rf_model.pkl'
        save_model(rf, model_path)

    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


if __name__ == "__main__":
    main() 