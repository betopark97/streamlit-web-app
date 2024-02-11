import streamlit as st

st.set_page_config(
    page_icon="🧑‍💻",
    page_title="Roberto's Portfolio"
)

header = st.container()

info = st.container()


with header:

    col1, col2 = st.columns(2, gap="small")
    
    with col1:
        st.image("./images/profile.png", use_column_width="auto")
    
    with col2:
        st.title("Roberto Park")