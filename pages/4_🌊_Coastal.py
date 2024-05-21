"""
Blanco et al.
Red Sea mangroves
"""
import streamlit as st
import leafmap.foliumap as leafmap
from folium.plugins import MiniMap

# Page configuration
st.set_page_config(
    page_title="Red sea mangroves extent",
    page_icon="🌊",
    layout="wide"
    )

pbf = st.secrets["pbf"]

st.title("Coastal")

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

mangroves = pbf["mangroves"]

options='''{
  "vectorTileLayerStyles": {
    "mangroves": function(f) {
      var color = "#f74370"; 
      return {
        fillOpacity: 1,
        fillColor: color,
        fill: true,
        weight: 1,
        color: "#f74370",
        opacity: 1,
      };
    }
  }    
}'''
m.add_vector_tile(mangroves,options, "Mangroves", attribution="Blanco, J. et al.")

m.to_streamlit(height=700)

