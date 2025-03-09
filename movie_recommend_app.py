import streamlit as st
import pickle
import pandas as pd

# Load Data
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['Series_Title'].values.tolist()
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies['Series_Title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_indices:
        recommended_movies.append(movies.iloc[i[0]].Series_Title)
        recommended_movies_poster.append(movies.iloc[i[0]].Poster_Link)  # Fetch posters from dataset

    return recommended_movies, recommended_movies_poster

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox(
    'Select a Movie:',
    movies_list
)

if st.button("Recommend"):
    movie_names, movie_posters = recommend(selected_movie)

    # Display movies & posters in a grid
    cols = st.columns(5)  # Create 5 columns for posters
    for i in range(len(movie_names)):
        with cols[i]:  # Assign each movie to a column
            st.image(movie_posters[i], use_column_width=True)  # ✅ Fixed deprecation issue
            st.write(movie_names[i])
