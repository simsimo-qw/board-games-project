#model for cleaning data 

import pandas as pd

# Load the dataset
df = pd.read_csv("data/review_of_games.csv")
print("Original columns:", df.columns)

# Clean the dataset by dropping unnecessary columns
columns_to_drop = ['Unnamed: 0', 'URL', 'Thumbnail']
for column in columns_to_drop:
    if column in df.columns:
        df = df.drop(columns=[column])

print("Cleaned columns:", df.columns)
# Save the cleaned dataset
df.to_csv("board-games-project/data/cleaned_review_of_games.csv", index=False)
print("Cleaned dataset saved!")

#need to clean the comments one.
# Load the comments dataset

comments_df = pd.read_csv("game_dataset/comments_on_games.csv")
print(comments_df.head())


columns_to_drop = ['Unnamed: 0', 'comment']
for column in columns_to_drop:
    if column in comments_df.columns:
        comments_df = comments_df.drop(columns=[column])

# Preview the DataFrame after dropping columns
print(comments_df.head())

# Save the cleaned DataFrame to a CSV file
comments_df.to_csv("game_dataset/cleaned_comments_on_games.csv", index=False)

# Confirm it was saved
print("cleaned_comments_on_games.csv")

