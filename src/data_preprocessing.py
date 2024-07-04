# src/data_preprocessing.py

import pandas as pd

def load_data(file_path):
    """
    Load the Spotify Million Playlist Dataset.
    :param file_path: Path to the dataset file.
    :return: DataFrame containing the dataset.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """
    Preprocess the dataset to extract relevant information.
    :param data: Raw DataFrame containing the dataset.
    :return: Processed DataFrame.
    """
    # Extract relevant columns
    data = data[['track_uri', 'track_name', 'track_artist', 'track_album', 'track_popularity', 'track_genre']]
    
    # Drop rows with missing values
    data = data.dropna()
    
    return data
