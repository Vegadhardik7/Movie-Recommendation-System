import streamlit as st
import pandas as pd
import requests
import pickle

def fetchposter(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=91c5f1cb21304bb73a3bd7344c912e6f&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        poster.append(fetchposter(movie_id))
    return recommended_movies, poster

movies_lst = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_lst)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommendation System")

option = st.selectbox("Select Your Favourite Movie & We Will Recommend You Accordingly",movies['title'].values)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




#if st.button('Recommend'):
#    rec = recommend(option)
#    for i in rec:
#        st.write(i)
