import streamlit as st
import leafmap.leafmap as leafmap
import leafmap.common as common


def app():
    st.title("Home")

    st.markdown(
        """
    A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu). 
    To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    https://share.streamlit.io/giswqs/streamlit-template?page=upload

    """
    )

    m = leafmap.Map(center=[13.417190312820402, 123.3315990573133], zoom=8)
    m.add_basemap("HYBRID")
    m.add_basemap("ROADMAP")
    # m.whiteboxgui(tree=TRUE)  //cant't add whiteboxgui to leafmap.leafmap
    # m.save_draw_features("data.geojson")  //does nothing
    m.to_streamlit(height=700)

