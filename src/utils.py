# src/utils.py

def print_recommendations(recommendations):
    """
    Print the recommended songs.
    :param recommendations: DataFrame containing recommended songs.
    """
    for index, row in recommendations.iterrows():
        print(f"Song: {row['track_name']}, Artist: {row['track_artist']}, Album: {row['track_album']}, Popularity: {row['track_popularity']}")
