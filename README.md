🎬 Movie Recommender System

A Machine Learning based Movie Recommendation System that suggests similar movies using Content-Based Filtering and Cosine Similarity.

Built with Python and deployed using Streamlit.

📌 About The Project

This project recommends movies based on similarity of features such as:

Genres

Keywords

Cast

Crew

Movie Overview

The system processes movie metadata, converts text data into vectors, and calculates similarity scores to recommend the most relevant movies.

🚀 Features

🔎 Search any movie from dataset

🎯 Get Top 5 Similar Movie Recommendations

🧠 Content-Based Recommendation System

📊 Cosine Similarity Algorithm

🌐 Streamlit Web App Interface

⚡ Fast response using precomputed similarity matrix

🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Pickle

📂 Project Structure

movie-recommender-system
│── app.py
│── movie_recommender.ipynb
│── movies.pkl
│── similarity.pkl
│── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
│── requirements.txt
│── README.md

⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/your-username/movie-recommender-system.git

cd movie-recommender-system

2️⃣ Install dependencies

pip install -r requirements.txt

(If requirements.txt not available)

pip install pandas numpy scikit-learn streamlit

3️⃣ Run the application

streamlit run app.py

📊 How It Works

Data Cleaning and Preprocessing

Feature Engineering (Combine genres, keywords, cast, crew)

Text Vectorization using CountVectorizer

Cosine Similarity Calculation

Top 5 Similar Movies Recommendation

🌍 Deployment

The project can be deployed on:

Streamlit Cloud

Render

Vercel

🎯 Future Improvements

Add collaborative filtering

Add movie posters using TMDB API

Improve UI/UX

Add user authentication

Deploy with database integration

📜 License

This project is open-source and available under the MIT License.

LIVE URL :- https://movie-recommendation-system-bdfgjzasahhlqqtqmjt43s.streamlit.app/

👨‍💻 Author

Vansh
