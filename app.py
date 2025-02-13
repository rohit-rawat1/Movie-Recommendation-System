import streamlit as st
import pickle
import base64

# Function to set background image
def set_bg_hack(main_bg):
    # Set image as background
    main_bg_ext = "jpg"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Specify your local image file
set_bg_hack('image/background.jpg')


def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(df.iloc[movie_id].title)
    return recommended_movies

df = pickle.load(open('movies.pkl','rb'))
movies= df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies
)

if st.button("Recommend"):
    names = recommend(selected_movie_name)

    st.text('1. ' + names[0])
    st.text('2. ' + names[1])
    st.text('3. ' + names[2])
    st.text('4. ' + names[3])
    st.text('5. ' + names[4])




