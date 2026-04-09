import streamlit as st
import pandas as pd
import pickle
import requests

st.set_page_config(page_title="Movie Recommender System", layout="wide")

# ---------- LOAD DATA ----------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# 🔐 Put your API key here
API_KEY = "YOUR_TMDB_API_KEY"

# ---------- POSTER FETCH ----------
@st.cache_data(show_spinner=False)
def fetch_poster(tmdb_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return None

    except Exception:
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

        # ✅ CORRECT TMDB ID HANDLING
        if 'tmdb_id' in movies.columns:
            tmdb_id = row['tmdb_id']
        elif 'id' in movies.columns:
            tmdb_id = row['id']
        else:
            tmdb_id = row['movie_id']

        names.append(row['title'])
        posters.append(fetch_poster(int(tmdb_id)))

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
            st.subheader(names[i])
            if posters[i]:
                st.image(posters[i], use_container_width=True)
            else:
                st.caption("Poster not available")