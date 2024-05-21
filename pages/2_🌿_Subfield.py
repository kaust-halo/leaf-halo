"""
Li et al. (in review)
Nationwide KSA subfield division dynamics
"""
import streamlit as st
import leafmap.foliumap as leafmap
from folium.plugins import MiniMap

# Page configuration
st.set_page_config(
    page_title="Subfield division dynamics",
    page_icon="🌿",
    layout="wide"
    )

xyz_layers = st.secrets["xyz"]

st.title("KSA subfield division dynamics")

year = 2023

m = leafmap.Map(
    locate_control=False, 
    search_control=False, 
    draw_export=False, 
    draw_control=False,
    minimap_control=False,
    measure_control=False,
    latlon_control=True,
    center=[24.5, 44.4],
    zoom=5
)
MiniMap(zoom_level_offset=-9, position="bottomleft").add_to(m)

optical = xyz_layers["optical"].replace("YYYY", str(year))
subfield = xyz_layers["subfield"].replace("YYYY", str(year))

m.add_tile_layer(
    url=optical,
    name=f"{year} optical basemap",
    attribution="Landsat, KAUST-HALO",
    max_native_zoom=13,
    shown = True
)

m.add_tile_layer(
    url=subfield,
    name=f"{year} subfield division",
    attribution="KAUST-HALO",
    max_native_zoom=13,
    shown = True
)
m.to_streamlit(height=700)

