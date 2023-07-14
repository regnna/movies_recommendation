import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=35c792859e362716fb80d3ee5bab24b2&language=en-US&&append_to_response=images")
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    j = list(enumerate(distances))
    i = 0
    m = []
    while i < 4806:
        t =[]
        t.append(i)
        k = movies.iloc[i].movie_id
        t.append(k)
        t.append(j[i][1])
        t = tuple(t)
        m.append(t)
        i += 1
    movies_list=sorted(m, reverse=True, key=lambda x: x[2])[1:7]
    # print(movies_list)
    # print(m)
    # movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for l in movies_list:
        recommended_movies.append(movies.iloc[l[0]].title)
        recommended_movies_poster.append(fetch_poster(l[1]))
    return recommended_movies,recommended_movies_poster


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movies Recommendation System')
# st.header("Honolulu header")
st.markdown("MArkdown header")
selected_movie_name= st.selectbox("movies List",movies['title'].values)
if st.button('Rcommend'):
    recommended_movies,posters = recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(posters[0])
        st.write(recommended_movies[0])

    with col2:
        st.image(posters[1])
        st.write(recommended_movies[1])

    with col3:
        st.image(posters[2])
        st.write(recommended_movies[2])

    with col1:
        st.image(posters[3])
        st.write(recommended_movies[3])

    with col2:
        st.image(posters[4])
        st.write(recommended_movies[4])
    with col3:
        st.image(posters[5])
        st.write(recommended_movies[5])
