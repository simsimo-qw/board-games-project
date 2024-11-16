#interactive game 
import pandas as pd

# Load the dataset
df = pd.read_csv("data/cleaned_review_of_games.csv")

# Function to calculate Custom Bayesian Average
def calculate_custom_bayesian(df, global_avg, min_votes):
    df['Custom Bayesian Average'] = (
        (df['Average'] * df['Users rated'] + global_avg * min_votes) /
        (df['Users rated'] + min_votes)
    )
    return df

# Define global average and minimum votes threshold
global_avg = df['Average'].mean()
min_votes = int(df['Users rated'].mean())

# Apply the function to calculate Custom Bayesian Average
df = calculate_custom_bayesian(df, global_avg, min_votes)

# Function to find the position of a game
def find_game_position(game_name, df):
    # Sort by Normal Average
    df_sorted_average = df.sort_values(by='Average', ascending=False).reset_index(drop=True)
    # Sort by Custom Bayesian Average
    df_sorted_custom = df.sort_values(by='Custom Bayesian Average', ascending=False).reset_index(drop=True)
    
    try:
        # Find the position of the game in both rankings
        position_average = df_sorted_average[df_sorted_average['Name'].str.contains(game_name, case=False)].index[0] + 1
        position_custom = df_sorted_custom[df_sorted_custom['Name'].str.contains(game_name, case=False)].index[0] + 1

        # Display the positions
        print(f"\nGame: {game_name}")
        print(f"Position by Normal Average: {position_average}")
        print(f"Position by Custom Bayesian Average: {position_custom}")
    except IndexError:
        print(f"\nSorry, the game '{game_name}' was not found in the dataset.")

# Interactive game loop
while True:
    print("\n--- Board Game Ranking Finder ---")
    game_name = input("Enter the name of a game (or type 'exit' to quit): ").strip()
    
    if game_name.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    
    find_game_position(game_name, df)
