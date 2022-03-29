import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd

def app():
    st.title("Avian Influenza Updates")
    
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
    libmanan = ('https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/barangays-municity-ph051718000.0.01.json')

    gdf_libmanan = gpd.read_file(libmanan)
    gdf = gpd.read_file(municities)
    gdf1 = gpd.read_file(ai)
    gdf2 = gpd.read_file(bp2_benes)
    m.add_gdf(gdf_libmanan, layer_name='Barangays')
    m.add_gdf(gdf, layer_name='Municities')
    m.add_gdf(gdf1, layer_name='AI case')
    m.add_gdf(gdf2, layer_name='BP2 Livelihood Assistance beneficiaries')
    m.load_config(config)
    m.to_streamlit(height=900, width=900, responsive=True, scrolling=True)