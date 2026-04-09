<<<<<<< HEAD
import streamlit as st
import pandas as pd
import pickle
import requests
import requests
import os

file_id = "1g5XrsneVPGWsxFzYMz6oRZwNqUMxuxla"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

if not os.path.exists("similarity.pkl"):
    with open("similarity.pkl", "wb") as f:
        response = requests.get(url)
        f.write(response.content)

st.set_page_config(page_title="Movie Recommender System", layout="wide")

# ---------- LOAD DATA ----------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "bac645078e9a3c0f648c04bfcdf37a67"

# ---------- POSTER FETCH ----------
@st.cache_data(show_spinner=False)
def fetch_poster(tmdb_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}&language=en-US"
        res = requests.get(url, timeout=3)

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

        # 🔑 IMPORTANT: choose correct ID column
        tmdb_id = row['id'] if 'id' in movies.columns else row['movie_id']

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
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i], width=250)
            else:
                st.caption("Poster not available")
=======
import streamlit as st
import pandas as pd
import pickle
import requests

st.set_page_config(page_title="Movie Recommender System", layout="wide")

# ---------- LOAD DATA ----------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "bac645078e9a3c0f648c04bfcdf37a67"

# ---------- POSTER FETCH ----------
@st.cache_data(show_spinner=False)
def fetch_poster(tmdb_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}&language=en-US"
        res = requests.get(url, timeout=3)

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

        # 🔑 IMPORTANT: choose correct ID column
        tmdb_id = row['id'] if 'id' in movies.columns else row['movie_id']

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
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i], width=250)
            else:
                st.caption("Poster not available")
>>>>>>> f0286d86b4343160ba1e6623209eadd40490fb2e
