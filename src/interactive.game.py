import pandas as pd
import numpy as np
from data_processing import load_datasets, calculate_custom_bayesian, find_game_position

# Define file paths
reviews_path = "data/cleaned_review_of_games.csv"
comments_path = "game_dataset/cleaned_comments_on_games.csv"

# Load datasets using the `load_datasets` function
reviews_df, comments_df = load_datasets(reviews_path, comments_path)

global_avg = round((np.mean(reviews_df['Average'])),2)  # Global average rating
min_votes = int(np.mean(reviews_df['Users rated']))  # Mean
print(f"Global Average: {global_avg}, Minimum Votes: {min_votes}")

# Calculate Custom Bayesian Average
reviews_df['Custom Bayesian Average'] = calculate_custom_bayesian (reviews_df['Average'], reviews_df['Users rated'], global_avg, min_votes) 

# Interactive game loop
while True:
    print("\n--- Board Game Ranking Finder ---")
    game_name = input("Enter the name of your favorite board game (or type 'exit' to quit): ").strip()
    
    if game_name.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    
    position_average, position_custom = find_game_position(game_name, reviews_df)
    
    if position_average and position_custom:
        print(f"\nGame: {game_name}")
        print(f"Position by Normal Average: {position_average}")
        print(f"Position by Custom Bayesian Average: {position_custom}")
    else:
        print(f"\nSorry, the game '{game_name}' was not found in the dataset.")
