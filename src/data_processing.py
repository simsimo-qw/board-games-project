import pandas as pd
import numpy as np

#Loads the reviews and comments datasets from the provided paths.
def load_datasets(reviews_path, comments_path):
    reviews_df = pd.read_csv(reviews_path)
    comments_df = pd.read_csv(comments_path)
    return reviews_df, comments_df


def count_comments(comments_df):
    comments_count = comments_df.groupby('name').size().reset_index(name='Number of Comments')
    return comments_count

def merge_datasets(reviews_df, comments_count):
    reviews_df = reviews_df.rename(columns={'Name': 'name'})
    merged_df = pd.merge(reviews_df, comments_count, on='name', how='inner')
    return merged_df


def calculate_differences(merged_df):
    users_rated = merged_df['Users rated'].to_numpy()
    comments_count = merged_df['Number of Comments'].to_numpy()
    votes_comments_diff = np.subtract(users_rated, comments_count)
    merged_df['Votes - Comments'] = votes_comments_diff
    return merged_df

def compute_correlation(merged_df):
    correlation_data = merged_df[['Users rated', 'Number of Comments', 'Average', 'Bayes average']].to_numpy()
    correlation_matrix = np.corrcoef(correlation_data, rowvar=False)
    return correlation_matrix

def calculate_custom_bayesian(df, global_avg, min_votes):
    df['Custom Bayesian Average'] = (
        (df['Average'] * df['Users rated'] + global_avg * min_votes) /
        (df['Users rated'] + min_votes)
    )
    return df