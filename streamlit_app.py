import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, avianflu, aisurvey  # import your app modules here

st.set_page_config(page_title="DA-RFO V (Bicol) Geospatial App", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = {
    "home": {"title": "Home", "icon": "house"},
    "avianflu": {"title": "Avian Influenza Updates", "icon": "map"},
    "aisurvey": {"title": "Avian Influenza Surveillance", "icon": "map"}
}

titles = [app["title"] for app in apps.values()]
icons = [app["icon"] for app in apps.values()]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Department of Agriculture Regional Field Office 5 Webmaps",
        options=titles,
        icons=icons,
        menu_icon="building",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://share.streamlit.io/darfo5gis/st-webmap) is created from a template by [Qiusheng Wu](https://wetlands.io). You can follow him on social media:
            [GitHub](https://github.com/giswqs) | [Twitter](https://twitter.com/giswqs) | [YouTube](https://www.youtube.com/c/QiushengWu) | [LinkedIn](https://www.linkedin.com/in/qiushengwu).
        """    
        
    )

for app in apps:
    if apps[app]["title"] == selected:
        eval(f"{app}.app()")
        break
