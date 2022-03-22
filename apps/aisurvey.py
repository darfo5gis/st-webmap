import streamlit as st
import leafmap.kepler as leafmap
import requests
import geopandas as gpd

def app():
    st.title("Avian Influenza Surveillance")
    
    m= leafmap.Map(center=[13.5, 123.15], zoom=8)
    
    municities = (
        'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/r5_municities_camsur.json'
    )
    ai = (
        'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/ai.geojson'
    )
    bp2_benes = (
        'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/bp2benes.geojson'
    )
    config = (
        'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/config/vector/m_config.json'
    )

    base_url = (
        'https://da5odk.site/v1/projects/5/forms/1/submissions.csv.zip'
    )

    auth = {
    "email": "darfo5.gis@gmail.com",
    "password": "Bicol.DB'5"
    }

    data = requests.post(base_url, auth=auth)


    gdf = gpd.read_file(municities)
    gdf1 = gpd.read_file(ai)
    gdf2 = gpd.read_file(bp2_benes)
    gdf_data = gpd.read_file(data)

    m.add_gdf(gdf, layer_name='Municities')
    m.add_gdf(gdf1, layer_name='AI case')
    m.add_gdf(gdf2, layer_name='BP2 Livelihood Assistance beneficiaries')
    m.add_gdf(gdf_data, layer_name='ODK Data')
    m.load_config(config)
    m.to_streamlit(height=900, width=900, responsive=True, scrolling=True)