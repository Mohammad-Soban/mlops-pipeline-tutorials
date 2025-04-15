import pandas as pd
import string
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from utils.logger import log_exception, logger

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')


def text_transformation(text):
    """
    Perform text preprocessing including tokenization, stopword removal, punctuation removal and stemming.
    """
    try:
        text = text.lower()

        # Tokenize the text
        text = word_tokenize(text)

        # Remove non-alphabetic tokens
        text = [word for word in text if word.isalnum()]

        # Remove stopwords
        text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]

        # Stemming
        ps = PorterStemmer()
        text = [ps.stem(word) for word in text]
        
        return ' '.join(text)
    
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


def data_preprocess(data, target='label', text='text'):
    """
    Preprocess the data by applying label encoding and transforming the text column
    """
    try:
        le = LabelEncoder()
        data[target] = le.fit_transform(data[target])
        
        data.loc[:, text] = data[text].apply(text_transformation)
        logger.info("Data Proecessed Successfully")

        return data
    
    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


def main(text = 'text', target = 'label'):
    """
    Main function to load raw data and apply transformation and preprocessing.
    """
    try:
        train_data = pd.read_csv("./data/raw/train.csv")
        test_data  = pd.read_csv("./data/raw/test.csv")

        logger.info("Train and Test Data read successfully")

        train_data_preprocessed = data_preprocess(train_data, target, text)
        test_data_preprocessed = data_preprocess(test_data, target, text)

        # Storing the preprocessed data in a new directory named processed inside the data_path
        processed_data_path = os.path.join('./data', 'processed_data')
        os.makedirs(processed_data_path, exist_ok=True)

        train_data_path = os.path.join(processed_data_path, 'train_processed.csv')
        train_data_preprocessed.to_csv(train_data_path, index=False)

        test_data_path = os.path.join(processed_data_path, 'test_processed.csv')
        test_data_preprocessed.to_csv(test_data_path, index=False)

        logger.info(f"Train and Test data preprocessed and saved to {processed_data_path}")

    except Exception as e:
        log_exception()
        logger.warning("Exitting the program ....")
        exit()


if __name__ == "__main__":
    main()
