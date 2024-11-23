import sys
import os
import pandas as pd
import streamlit as st
import numpy as np
import csv 

# Add the src folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import functions from data_processing
from data_processing import calculate_custom_bayesian, find_game_position

# Define paths relative to the visualization folder
reviews_path = "../data/cleaned_review_of_games.csv"
comments_path = "../game_dataset/cleaned_comments_on_games.csv"

# Load datasets
reviews_df = pd.read_csv(reviews_path)
comments_df = pd.read_csv(comments_path)
print(reviews_df.head())
print(comments_df.head())

# Define global average and minimum votes threshold
global_avg = reviews_df['Average'].mean()
min_votes = int(reviews_df['Users rated'].mean())

# Calculate Custom Bayesian Average
reviews_df['Custom Bayesian Average'] = calculate_custom_bayesian(
    reviews_df['Average'], reviews_df['Users rated'], global_avg, min_votes
)

# Streamlit App
st.title("Board Game Analysis App")
st.sidebar.header("Navigation")

# Sidebar Navigation
menu = st.sidebar.radio("Select a Page:", ["Overview", "Find Game Ranking", "Compare Rankings"])

if menu == "Overview":
    st.subheader("Overview of Data")
    st.write("This app analyzes board game data using a custom Bayesian ranking system.")
    st.dataframe(reviews_df.head())

if menu == "Find Game Ranking":
    st.subheader("Find Your Favorite Game's Ranking")
    game_name = st.text_input("Enter the name of your favorite board game:")
    if game_name:
        try:
            position_average, position_custom = find_game_position(game_name, reviews_df)
            st.write(f"**Game**: {game_name}")
            st.write(f"**Rank by Average**: {position_average}")
            st.write(f"**Rank by Custom Bayesian Average**: {position_custom}")
        except IndexError:
            st.error(f"The game '{game_name}' was not found.")

if menu == "Compare Rankings":
    st.subheader("Top 10 Games: Average vs Custom Bayesian")
    top_10_average = reviews_df.sort_values(by='Average', ascending=False).head(10)
    top_10_bayesian = reviews_df.sort_values(by='Custom Bayesian Average', ascending=False).head(10)

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Top 10 by Average")
        st.table(top_10_average[['Name', 'Average', 'Users rated']])

    with col2:
        st.write("### Top 10 by Custom Bayesian Average")
        st.table(top_10_bayesian[['Name', 'Custom Bayesian Average', 'Users rated']])

# Footer
st.sidebar.text("Streamlit App | Board Game Analysis")
