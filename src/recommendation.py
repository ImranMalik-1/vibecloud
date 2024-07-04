# src/recommendation.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_preprocessing import load_data, preprocess_data

def get_recommendations(input_song, data, num_recommendations=5):
    """
    Get song recommendations based on a given input song.
    :param input_song: The name of the song to base recommendations on.
    :param data: DataFrame containing the dataset.
    :param num_recommendations: Number of recommended songs to return.
    :return: List of recommended songs.
    """
    # TF-IDF Vectorizer to convert text data into numerical features
    tfidf_vectorizer = TfidfVectorizer()
    data['track_genre'] = data['track_genre'].fillna('')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['track_genre'])
    
    # Get the TF-IDF vector for the input song
    input_song_genre = data[data['track_name'].str.lower() == input_song.lower()]['track_genre'].values[0]
    input_vector = tfidf_vectorizer.transform([input_song_genre])
    
    # Compute cosine similarity between the input song and all other songs
    cosine_sim = cosine_similarity(input_vector, tfidf_matrix)
    
    # Get indices of most similar songs
    similar_indices = cosine_sim[0].argsort()[-num_recommendations-1:-1][::-1]
    
    # Get recommended songs
    recommended_songs = data.iloc[similar_indices]
    
    return recommended_songs[['track_name', 'track_artist', 'track_album', 'track_popularity']]

if __name__ == "__main__":
    # Load and preprocess data
    data = load_data('data/playlist_data.csv')
    processed_data = preprocess_data(data)
    
    # Get recommendations for a sample song
    input_song = 'Blinding Lights'
    recommendations = get_recommendations(input_song, processed_data)
    
    print(f"Recommendations for '{input_song}':")
    print(recommendations)
