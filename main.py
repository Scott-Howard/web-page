# code a home page for the website
# code a contact me page for the website
#add a navigation bar to the website
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/sh_google.jpg", width=600)
    
with col2:
    st.title("Scott Howard")
    content = """
    Welcome to my website. I am a Data Scientist and Statistician. 
    I graduated in 2022 from the University of Newcastle with a Honours degree in Statistics.
    I have experience in Python, R, SQL, and machine learning. 
    I have a passion for data and I am always looking for new projects to work on. 
    I have worked on projects in a variety of industries including Education, Agribuisness, and Supply chains.
    Feel free to reach out to me if you have any questions or would like to work together.
    """
    st.info(content)

tagline = """
Below you can find some of the apps I have built in Python. Feel free to explore them and let me know what you think.
"""
st.write(tagline)
    
col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
