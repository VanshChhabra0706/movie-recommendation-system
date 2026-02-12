import streamlit as st
import pandas as pd
import pickle
import requests

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Movie Recommender System", layout="wide")

TMDB_API_KEY = "bac645078e9a3c0f648c04bfcdf37a67"
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# ------------------ LOAD DATA ------------------
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ------------------ POSTER FETCH (TITLE BASED) ------------------
@st.cache_data(show_spinner=False, ttl=3600)
def fetch_poster_by_title(title):
    try:
        params = {
            "api_key": TMDB_API_KEY,
            "query": title
        }

        response = requests.get(TMDB_SEARCH_URL, params=params, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        if data.get("results"):
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return TMDB_IMAGE_URL + poster_path

        return None

    except Exception:
        return None

# ------------------ RECOMMENDER ------------------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        title = movies.iloc[i[0]]["title"]
        names.append(title)
        posters.append(fetch_poster_by_title(title))

    return names, posters

# ------------------ UI ------------------
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

if st.button("Recommend"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.subheader(names[i])
            if posters[i]:
                st.image(posters[i], use_container_width=True)
            else:
                st.caption("Poster not available")
