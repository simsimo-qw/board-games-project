import pandas as pd
import numpy as np

#Drop specified column from a Dataset 
def drop_columns(df,columns_to_drop):
    for column in columns_to_drop:
        if column in df.columns:
            print(f"Dropping column: {column}")
            df = df.drop(columns=[column])
    return df

#Loads the reviews and comments datasets from the provided paths.
def load_datasets(reviews_path,comments_path):
    reviews_df = pd.read_csv(reviews_path)
    comments_df = pd.read_csv(comments_path)
    return reviews_df, comments_df

# Calculate Custom Bayesian Average 
def calculate_custom_bayesian(average, votes, global_avg, min_votes):
    return (average * votes + global_avg * min_votes) / (votes + min_votes)

def find_game_position(game_name, df):

    df_sorted_average = df.sort_values(by='Average', ascending=False).reset_index(drop=True)
    df_sorted_custom = df.sort_values(by='Custom Bayesian Average', ascending=False).reset_index(drop=True)
    
    try:
        # Find the position of the game in both rankings
        position_average = df_sorted_average[df_sorted_average['Name'].str.contains(game_name, case=False, na=False)].index[0] + 1
        position_custom = df_sorted_custom[df_sorted_custom['Name'].str.contains(game_name, case=False, na=False)].index[0] + 1

        # Return the positions
        return position_average, position_custom
    except IndexError:
        # Game not found
        return None, None
