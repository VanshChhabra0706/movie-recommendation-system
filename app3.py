import streamlit as st
import pandas as pd
import pickle
import requests

st.set_page_config(page_title="Movie Recommender System", layout="wide")

# ---------- LOAD DATA ----------
movies_dict = pickle.load(open('movie_dict.pkl1', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl1', 'rb'))

API_KEY = "bac645078e9a3c0f648c04bfcdf37a67"

# ---------- POSTER FETCH ----------
@st.cache_data(show_spinner=False)
def fetch_poster(tmdb_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}&language=en-US"
        res = requests.get(url, timeout=5)

        if res.status_code != 200:
            return None

        data = res.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

        return None
    except:
        return None


# ---------- RECOMMENDER ----------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        row = movies.iloc[i[0]]

        tmdb_id = row['id']   # ✅ correct TMDB ID
        names.append(row['title'])
        posters.append(fetch_poster(tmdb_id))

    return names, posters


# ---------- UI ----------
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)

    cols = st.columns(5)

