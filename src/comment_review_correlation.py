import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load reviews dataset
reviews_df = pd.read_csv("data/cleaned_review_of_games.csv")

# Load cleaned comments dataset
comments_df = pd.read_csv("game_dataset/cleaned_comments_on_games.csv")

# Preview the datasets
print(reviews_df.head())
print(comments_df.head())

# Count comments using NumPy
comments_count = comments_df.groupby('name').size()
comments_count = comments_count.reset_index()
comments_count.columns = ['name', 'Number of Comments']

# Standardize column names to avoid unmatching name
reviews_df = reviews_df.rename(columns={'Name': 'name'})
comments_count = comments_count.rename(columns={'Name': 'name'})

# Convert to NumPy arrays for optimized operations
game_names = comments_count['name'].to_numpy()
number_of_comments = comments_count['Number of Comments'].to_numpy()

# Group the comments dataset by 'name' and count the number of comments for each game
comments_count = comments_df.groupby('name').size().reset_index(name='Number of Comments')

# Display the results
print(comments_count.head(60))  # Show the first 60 games and their comment counts

# Optionally, save the results to a CSV file for further analysis
comments_count.to_csv("game_dataset/comments_count.csv", index=False)
print("Comments count saved to game_dataset/comments_count.csv")

# Merge reviews with comments count
merged_df = pd.merge(reviews_df, comments_count, on='name', how='inner')

# Convert relevant columns to NumPy arrays
users_rated = merged_df['Users rated'].to_numpy()
comments_count = merged_df['Number of Comments'].to_numpy()


# Calculate the difference using NumPy
votes_comments_diff = np.subtract(users_rated, comments_count)

# Add the result back to the DataFrame
merged_df['Votes - Comments'] = votes_comments_diff

# Preview the differences
print(merged_df[['name', 'Users rated', 'Number of Comments', 'Votes - Comments']].head())


# Create a matrix of relevant columns
correlation_data = merged_df[['Users rated', 'Number of Comments', 'Average', 'Bayes average']].to_numpy()

# Compute the correlation matrix using NumPy
correlation_matrix = np.corrcoef(correlation_data, rowvar=False)

print("Correlation Matrix (NumPy):")
print(correlation_matrix)

import matplotlib.pyplot as plt


# Correlation matrix (replace this with your actual matrix)
correlation_matrix = np.array([
    [1.0, 0.96338753, 0.1687244, 0.63208549],
    [0.96338753, 1.0, 0.16347594, 0.61274807],
    [0.1687244, 0.16347594, 1.0, 0.46955278],
    [0.63208549, 0.61274807, 0.46955278, 1.0]
])

# Labels for the variables
labels = ['Users rated', 'Number of Comments', 'Average', 'Bayes average']

# Plot the heatmap
fig, ax = plt.subplots(figsize=(8, 6))
heatmap = ax.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest")

# Add labels for rows and columns
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

# Rotate the x-axis labels for better readability
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add the correlation values inside the heatmap
for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(j, i, f"{correlation_matrix[i, j]:.2f}", ha="center", va="center", color="black")

# Add a title and color bar
plt.title("Correlation Matrix")
plt.colorbar(heatmap)
plt.show()

