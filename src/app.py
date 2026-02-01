# Streamlit application entry point
import streamlit as st
from recommender import recommend_learning_path
from compression import compress_context

st.title("📚 Learning Path Recommender")

st.write("This app recommends what you should learn next based on your skills.")

current_skills = st.multiselect(
    "Select your current skills:",
    ["Basics", "Data Types", "Loops", "Functions", "HTML", "CSS", "JavaScript"]
)

target_skill = st.selectbox(
    "Select your target skill:",
    ["Python", "Data Science", "Web Development"]
)

if st.button("Recommend Learning Path"):
    path = recommend_learning_path(current_skills, target_skill)
    compressed_path = compress_context(path)

    st.subheader("Recommended Learning Path:")
    st.write(compressed_path)
