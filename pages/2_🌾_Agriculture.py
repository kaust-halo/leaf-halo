"""
Lopez et al. (in preparation)

"""
import streamlit as st
import leafmap.foliumap as leafmap
from folium.plugins import MiniMap

# Page configuration
st.set_page_config(
    page_title="Saudi agriculture",
    page_icon="🌾",
    layout="wide"
    )

xyz_layers = st.secrets["xyz"]
pbf_layers = st.secrets["pbf"]

st.title("Agriculture in Saudi Arabia")

year = 2015

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

optical = xyz_layers["optical"].replace("YYYY", str(year)).replace(".png","")
agriculture = pbf_layers["agriculture"].replace("YYYY", str(year))
et_xyz = xyz_layers["field_et"].replace("YYYY", str(year))
fuse_xyz = xyz_layers["field_use"].replace("YYYY", str(year))


m.add_tile_layer(
    url=optical,
    name=f"{year} optical basemap",
    attribution="Landsat, KAUST-HALO",
    max_native_zoom=13,
    shown = True
)

options_fieldUse='''{
  "vectorTileLayerStyles": {
    "2015ETm3": function(f) {
      var color = "#ffffcc"; 
      if (f.fieldUse >= 0.25) {
        color = "#c2e699";
      }
      if (f.fieldUse >= 0.5) {
        color = "#78c679";
      }
      if (f.fieldUse >= 0.75) {
        color = "#31a354";
      }
      if (f.fieldUse >= 1) {
        color = "#006837";
      }
      return {
        fillOpacity: 1,
        fillColor: color,
        fill: true,
        weight: 1,
        color: "white",
        opacity: 1,
      };
    }
  }    
}'''

options_et='''{
  "vectorTileLayerStyles": {
    "2015ETm3": function(f) {
      var color = "#86340c"; 
      if (f.ET >= 250) {
        color = "#c49e0d";
      }
      if (f.ET >= 500) {
        color = "#f3fe34";
      }
      if (f.ET >= 750) {
        color = "#aefeae";
      }
      if (f.ET >= 1000) {
        color = "#11f9fd";
      }
      if (f.ET >= 1250) {
        color = "#698afc";
      }
      if (f.ET >= 1500) {
        color = "#5813fc";
      }
      return {
        fillOpacity: 1,
        fillColor: color,
        fill: true,
        weight: 1,
        color: "white",
        opacity: 1,
      };
    }
  }    
}'''

# As vector tiles:
#m.add_vector_tile(agriculture,options_fieldUse, "Field use", attribution="KAUST-HALO")
#m.add_vector_tile(agriculture,options_et, "Annual ET", attribution="KAUST-HALO")

# As pre-rendered rasters:
m.add_tile_layer(
    url=fuse_xyz,
    name=f"{year} annual use (%)",
    attribution="KAUST-HALO",
    max_native_zoom=13,
    shown = True
)

m.add_tile_layer(
    url=et_xyz,
    name=f"{year} annual ET",
    attribution="KAUST-HALO",
    max_native_zoom=13,
    shown = True
)


m.to_streamlit(height=700)

