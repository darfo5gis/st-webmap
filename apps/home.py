import streamlit as st
import leafmap.heremap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
    A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu). 
    To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    https://share.streamlit.io/giswqs/streamlit-template?page=upload

    """
    )

    m = leafmap.Map(center=[13.30, 124.15], zoom=8)
    m.add_basemap("ROADMAP")
    m.add_basemap("HYBRID")
    m.to_streamlit(height=700)

