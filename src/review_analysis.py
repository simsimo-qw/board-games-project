import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_processing import load_datasets, calculate_custom_bayesian
from graph_visualization import plot_low_vote_games_comparison, scatter_plot_votes_vs_ratings

# Define file paths
reviews_path = "data/cleaned_review_of_games.csv"
comments_path = "game_dataset/cleaned_comments_on_games.csv"

# Load datasets
reviews_df, comments_df = load_datasets(reviews_path, comments_path)

global_avg = round((np.mean(reviews_df['Average'])),2)  # Global average rating
min_votes = int(np.mean(reviews_df['Users rated']))  # Mean
print(f"Global Average: {global_avg}, Minimum Votes: {min_votes}")

# Calculate Custom Bayesian Average
reviews_df['Custom Bayesian Average'] = calculate_custom_bayesian (reviews_df['Average'], reviews_df['Users rated'], global_avg, min_votes) 

# Calculate the difference for each game
reviews_df['Difference (Bayesian - Average)'] = reviews_df['Custom Bayesian Average'] - reviews_df['Average']

# PART 1: Top 10 Rankings Comparison
top_10_average = reviews_df.sort_values(by='Average', ascending=False).head(10)
top_10_bayesian = reviews_df.sort_values(by='Custom Bayesian Average', ascending=False).head(10)

print("\nTop 10 Games by Average:")
print(top_10_average[['Name', 'Average', 'Users rated']])

print("\nTop 10 Games by Custom Bayesian Average:")
print(top_10_bayesian[['Name', 'Custom Bayesian Average', 'Users rated']])

# Prepare top 10 by Average
top_10_average = reviews_df.sort_values(by='Average', ascending=False).head(10)[['Name']]
top_10_average['Rank (Average)'] = range(1, 11)

# Prepare top 10 by Custom Bayesian Average
top_10_bayesian = reviews_df.sort_values(by='Custom Bayesian Average', ascending=False).head(10)[['Name']]
top_10_bayesian['Rank (Bayesian)'] = range(1, 11)

# Reset indices to ensure alignment for concatenation
top_10_average.reset_index(drop=True, inplace=True)
top_10_bayesian.reset_index(drop=True, inplace=True)

# Combine into a single table for side-by-side comparison
comparison_table = pd.concat([top_10_average, top_10_bayesian], axis=1)

# Update column names for clarity
comparison_table.columns = ['Name (Average)', 'Rank (Average)', 'Name (Bayesian)', 'Rank (Bayesian)']

# Display the comparison table
print("\nSide-by-Side Comparison with Rankings (Name and Rank)")
print(comparison_table)


# PART 2: Identify Low-Vote Games with High Averages
low_votes_threshold = 200  # Define low votes as less than 200
low_votes_high_average = reviews_df[
    (reviews_df['Users rated'] < low_votes_threshold) & (reviews_df['Average'] > 8.0)
].sort_values(by='Average', ascending=False)

print("\nGames with Few Votes and High Averages:")
print(low_votes_high_average[['Name', 'Average', 'Users rated', 'Custom Bayesian Average']])

#visualization part

# Limit to top 20 games for visualization
top_low_votes_high_average = low_votes_high_average.head(20)

# Plot comparison for low-vote games
plot_low_vote_games_comparison(top_low_votes_high_average)

# Create scatter plot showing the problem
scatter_plot_votes_vs_ratings(reviews_df, low_votes_high_average, global_avg)
