import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_processing import calculate_custom_bayesian , load_datasets
from graph_visualization import plot_correlation_heatmap


reviews_path = "data/cleaned_review_of_games.csv"
comments_path = "game_dataset/cleaned_comments_on_games.csv"

# Load datasets
reviews_df, comments_df = load_datasets(reviews_path, comments_path)

# Standardize column names
reviews_df = reviews_df.rename(columns={'Name': 'name'})
comments_count = comments_df.groupby('name').size().reset_index(name='Number of Comments')

# Merge reviews and comments data
merged_df = pd.merge(reviews_df, comments_count, on='name', how='inner')

# Calculate global average and minimum votes
global_avg = round((np.mean(reviews_df['Average'])),2)  # Global average rating
min_votes = int(np.mean(reviews_df['Users rated']))  # Mean

# Calculate Custom Bayesian Average
merged_df['Custom Bayesian Average'] = calculate_custom_bayesian(
    merged_df['Average'], merged_df['Users rated'], global_avg, min_votes
)

# Calculate the difference between votes and comments
merged_df['Votes - Comments'] = np.subtract(merged_df['Users rated'], merged_df['Number of Comments'])

# Compute correlation matrix dynamically 
correlation_matrix = merged_df[['Users rated', 'Number of Comments', 'Average', 'Custom Bayesian Average']].corr().to_numpy()
labels = ['Users rated', 'Number of Comments', 'Average', 'Custom Bayesian Average']

#plot the heatmap 
plot_correlation_heatmap(correlation_matrix, labels, title="Custom Bayesian Average Correlation")

