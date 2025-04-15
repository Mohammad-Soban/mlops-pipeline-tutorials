import pandas as pd
import os
from utils.logger import log_exception, logger
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data(file_path):
    """
    Load the data from the given file path.
    """
    try:
        data = pd.read_csv(file_path)
        data.fillna("", inplace=True)
        logger.info("Data loaded successfully")
        return data
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()

def applying_Tf_Idf(train_data, test_data, max_features):
    """
    Apply Tf-Idf on the train and test data.
    """
    try:
        ti = TfidfVectorizer(max_features=max_features)

        x_train = train_data['text'].values
        x_test = test_data['text'].values

        y_train = train_data['label'].values
        y_test = test_data['label'].values

        x_train_tfidf = ti.fit_transform(x_train)
        x_test_tfidf = ti.transform(x_test)

        train_df = pd.DataFrame(x_train_tfidf.toarray())
        train_df['label'] = y_train

        test_df = pd.DataFrame(x_test_tfidf.toarray())
        test_df['label'] = y_test

        logger.info("Tf-Idf applied successfully")
        return train_df, test_df
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()

def save_data(df, path):
    """
    Save the data to the given path.
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path, index=False)
    
    except Exception as e:
        log_exception()
        logger.warning("Unable to save data....")
        exit()

def main():
    try:
        max_features = 50

        train_data = load_data("./data/processed_data/train_processed.csv")
        test_data = load_data("./data/processed_data/test_processed.csv")

        train_data_tfidf, test_data_tfidf = applying_Tf_Idf(train_data, test_data, max_features)

        save_data(train_data_tfidf, os.path.join("./data", "transformed", "train_tfidf.csv"))
        save_data(test_data_tfidf, os.path.join("./data", "transformed", "test_tfidf.csv"))

    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


if __name__ == "__main__":
    main()
