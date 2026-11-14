import pandas as pd
import streamlit as st
from recommendation import recommend_movie

# Page configuration
st.set_page_config(
    page_title="IMDb Movie Recommendation System",
        layout="wide")

st.title('IMDb Movie Recommendation System')
st.write("Discover movies based on storyline similarity", 
            "Using TF-IDF and Cosine Similarity.")


st.divider()

# Sidebar
st.sidebar.title("Movie Recommendation")

st.sidebar.write(
    "This application recommends movies "
    "based on the similarity of their storylines."
)
# User input
st.subheader("Enter Your Movie Storyline")

user_storyline = st.text_area(
    "Enter the movie story:",
    height=180
)
# Number of recommendations
top_n = st.selectbox(
    "Number of Recommendations",
    [5,6,7,8,9,10]
)
# Recommendation button
if st.button("Recommend Movies", type="primary"):

    if not user_storyline.strip():

        st.warning("Please enter a movie storyline.")

    else:
        result = recommend_movie(
        user_storyline,
        k=top_n)

        
        if result.empty:

            st.warning(
                "No similar movies found. "
                "Try entering more storyline details."
            )
        else:

            st.success("Recommendations generated!")

            st.subheader("Recommended Movies")

            for index, value in result.iterrows():

                st.markdown(
                    f"### {index + 1}. {value['Movie Name']}")

                st.write(
                    f"**Storyline:** {value['Storyline']}")
