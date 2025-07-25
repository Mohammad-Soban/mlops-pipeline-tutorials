import os
import numpy as np
import pandas as pd
import pickle
import json
import yaml
from dvclive import Live
from sklearn.metrics import accuracy_score, precision_score, roc_auc_score, recall_score
from utils.logger import log_exception, logger
from utils.loader import load_params


def load_model(path):
    try:
        with open(path, 'rb') as file:
            model = pickle.load(file)

        logger.info("Model loaded successfully")
        
        return model
    
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()

def load_data(path):
    """
    Load data from a CSV file.
    """
    try:
        data = pd.read_csv(path)
        return data
    
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


def evaluate_model(rf, X_test, y_test):
    """
    Evaluate the model using various metrics by getting predictions.
    """
    try:
        y_pred = rf.predict(X_test)
        y_pred_proba = rf.predict_proba(X_test)[:, 1]

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)

        metrics_dict = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'roc_auc': roc_auc
        }

        logger.info('Model evaluation metrics calculated successfully')

        return metrics_dict

    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


def save_metrics(metrics, file_path):
    """
    Save the metrics to a JSON file.
    """ 
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            json.dump(metrics, file, indent=4)

    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()
    

def main():
    try:
        params = load_params('params.yaml')

        rf = load_model('models/rf_model.pkl')
        test_data = load_data('./data/transformed/test_tfidf.csv')

        X_test = test_data.iloc[:, :-1].values
        y_test = test_data.iloc[:, -1].values

        metrics = evaluate_model(rf, X_test, y_test)

        with Live(save_dvc_exp=True) as live:
            live.log_metric('accuracy', metrics['accuracy'])
            live.log_metric('precision', metrics['precision'])
            live.log_metric('recall', metrics['recall'])
            live.log_metric('roc_auc', metrics['roc_auc'])
                
            live.log_params(params)

        save_metrics(metrics, 'reports/model_metrics.json')

    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


if __name__ == "__main__":
    main()