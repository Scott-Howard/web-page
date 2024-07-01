# code a home page for the website
# code a contact me page for the website
#add a navigation bar to the website
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)
    
    with col2:
        st.title("Scott Howard")
        content = """
        Welcome to my website. I am a data scientist and machine learning engineer. 
        I have experience in Python, R, SQL, and machine learning. 
        I have a passion for data and I am always looking for new projects to work on. Feel free to reach out to me if you have any questions or would like to work together.
        """
        st.info(content)