#model for cleaning data 

import pandas as pd
from data_processing import drop_columns, load_datasets

#Define file paths 
reviews_path = "data/review_of_games.csv"
comments_path = "game_dataset/comments_on_games.csv"

# Load datasets
reviews_df, comments_df = load_datasets(reviews_path, comments_path)

# Clean the dataset by dropping unnecessary columns
columns_to_drop_reviews = ['Unnamed: 0', 'URL', 'Thumbnail']
reviews_df = drop_columns(reviews_df, columns_to_drop_reviews)

# Save the cleaned review dataset
reviews_df.to_csv("./data/cleaned_review_of_games.csv", index=False)
print("Cleaned reviews dataset saved!")

#Need to clean the comments one.
columns_to_drop_comments = ['Unnamed: 0', 'comment']
comments_df = drop_columns(comments_df, columns_to_drop_comments)

#save the cleaned comments datset
comments_df.to_csv("./game_dataset/cleaned_comments_on_games.csv", index=False)
print("Cleaned comments dataset saved!")

#Both dataset after dropping columns
print((comments_df.head()),(reviews_df.head()))

