import streamlit as st
import pandas as pd
from recommender import recom, df  # using df from recommender

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")
st.markdown("Select a movie from the dropdown to get top 5 similar recommendations!")

selected_movie = st.selectbox(
    "Choose a movie to get recommendations:",
    df['title'].values
)

if st.button("Get Recommendations"):
    recommendations_name, recommendations_posters = recom(selected_movie)
    
    st.subheader("Recommended Movies:")
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(recommendations_posters[i], use_container_width=True)
            st.markdown(f"<p style='font-size:18px; font-weight:500; text-align:center'>{recommendations_name[i]}</p>", unsafe_allow_html=True)
