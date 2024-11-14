#model for cleaning data 

import pandas as pd

# Load the dataset
df = pd.read_csv("board-games-project/data/review_of_games.csv")
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

print("funziona")



