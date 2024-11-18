import matplotlib.pyplot as plt
import numpy as np 
def plot_low_vote_games_comparison(data, title="Low-Vote Games with High Averages: Average vs Custom Bayesian Average"):
    """
    Plots a comparison of Average vs Custom Bayesian Average for low-vote games.
    """
    # Prepare x-axis
    x = range(len(data))

    # Bar chart for Average and Custom Bayesian Average
    plt.figure(figsize=(12, 6))
    plt.bar(x, data['Average'], width=0.4, label='Average', color='orange', align='center')
    plt.bar([i + 0.4 for i in x], data['Custom Bayesian Average'], width=0.4, label='Custom Bayesian Average', color='blue', align='center')

    # Add game names to the x-axis
    plt.xticks([i + 0.2 for i in x], data['Name'], rotation=45, ha='right')
    plt.ylabel("Ratings")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def scatter_plot_votes_vs_ratings(reviews_df, low_votes_high_average, global_avg, sample_all=2000, sample_low=250):
    """
    Creates a scatter plot to show the relationship between votes and ratings.
    Highlights low-vote games with high averages.
    """
    plt.figure(figsize=(10, 6))

    # Plot all games
    plt.scatter(
        reviews_df.sample(n=sample_all)['Users rated'], 
        reviews_df.sample(n=sample_all)['Average'], 
        alpha=0.6, 
        label='All Games', 
        color='blue'
    )

    # Highlight low-vote games with high averages
    plt.scatter(
        low_votes_high_average.sample(n=sample_low)['Users rated'], 
        low_votes_high_average.sample(n=sample_low)['Average'], 
        color='red', 
        label='Low Votes & High Average'
    )

    # Global average line
    plt.axhline(global_avg, color='green', linestyle='--', label=f"Global Average = {global_avg:.2f}")

    plt.xlim([0, 800])
    plt.xlabel("Number of Votes (Users rated)")
    plt.ylabel("Average Rating")
    plt.title("Impact of Few Votes on Average Ratings")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(correlation_matrix, labels, title="Correlation Matrix"):
    """
    Plots a heatmap for the given correlation matrix.

    Parameters:
    - correlation_matrix (ndarray): The correlation matrix to visualize.
    - labels (list): The labels for the rows and columns of the matrix.
    - title (str): Title of the heatmap (default is "Correlation Matrix").
    """
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
    plt.title(title)
    plt.colorbar(heatmap)
    plt.tight_layout()
    plt.show()
