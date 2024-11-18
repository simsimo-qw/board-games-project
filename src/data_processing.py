import pandas as pd
import numpy as np

#Loads the reviews and comments datasets from the provided paths.
def load_datasets(reviews_path,comments_path):
    reviews_df = pd.read_csv("data\cleaned_review_of_games.csv")
    comments_df = pd.read_csv("game_dataset\cleaned_comments_on_games.csv")
    return reviews_df, comments_df

# Calculate Custom Bayesian Average 
def calculate_custom_bayesian(average, votes, global_avg, min_votes):
    return (average * votes + global_avg * min_votes) / (votes + min_votes)
