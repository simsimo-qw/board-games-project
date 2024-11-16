import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("data/cleaned_review_of_games.csv")

# Calculate the global average and minimum votes using NumPy
global_avg = np.mean(df['Average'])  # Global average rating
min_votes = int(np.round(np.mean(df['Users rated'])))  # Minimum votes threshold
print(f"Global Average: {global_avg}, Minimum Votes: {min_votes}")

# Calculate Custom Bayesian Average using NumPy
def calculate_custom_bayesian_numpy(average, votes, global_avg, min_votes):
    return (average * votes + global_avg * min_votes) / (votes + min_votes)

# Apply the function using NumPy
df['Custom Bayesian Average'] = calculate_custom_bayesian_numpy(
    df['Average'], df['Users rated'], global_avg, min_votes
)

# Calculate differences using NumPy
df['Difference'] = np.subtract(df['Custom Bayesian Average'], df['Average'])

# Preview the results
print(df[['Name', 'Average', 'Custom Bayesian Average', 'Difference']].head())

# Statistics on differences
mean_diff = np.mean(df['Difference'])
max_diff = np.max(df['Difference'])
min_diff = np.min(df['Difference'])
print(f"Mean Difference: {mean_diff}")
print(f"Maximum Difference: {max_diff}")
print(f"Minimum Difference: {min_diff}")

# Calculate difference with BGG's Bayesian Average
df['Difference to BGG'] = np.subtract(df['Custom Bayesian Average'], df['Bayes average'])

# Preview the differences with BGG's Bayesian Average
print(df[['Name', 'Bayes average', 'Custom Bayesian Average', 'Difference to BGG']].head())

# Find top positive and negative differences with BGG's Bayesian Average
high_diff_bgg = df.sort_values(by='Difference to BGG', ascending=False).head(10)
low_diff_bgg = df.sort_values(by='Difference to BGG').head(10)

print("Top 10 games where Custom Bayesian is higher than BGG:")
print(high_diff_bgg[['Name', 'Bayes average', 'Custom Bayesian Average', 'Difference to BGG', 'Users rated']])

print("Top 10 games where Custom Bayesian is lower than BGG:")
print(low_diff_bgg[['Name', 'Bayes average', 'Custom Bayesian Average', 'Difference to BGG', 'Users rated']])

top_30_average = df.sort_values(by='Average', ascending=False).head(30)[['Name', 'Average', 'Users rated']]
top_30_custom_bayesian = df.sort_values(by='Custom Bayesian Average', ascending=False).head(30)[
    ['Name', 'Custom Bayesian Average', 'Users rated']]

print("Top 30 Games by Normal Average:") 
print (top_30_average)

print("Top 30 Games by custom Bayesian Average:")
print(top_30_custom_bayesian)
