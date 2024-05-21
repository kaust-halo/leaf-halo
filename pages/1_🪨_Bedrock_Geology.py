"""
Geo2bg
"""
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(
    page_title="Bedrock geology of the Arabian Peninsula",
    page_icon="",
    layout="wide"
    )

markdown = """
Bedrock geology of the Arabian Peninsula.
[Source](https://doi.org/10.5066/P9GI9NS4)
"""


st.sidebar.title("About")
st.sidebar.info(markdown)

geo_layers = st.secrets["geo"]
url = geo_layers["geo2bg"]

m = leafmap.Map()

color_dict={
    "Q": "#f9f27f", # Quaternary
    "Qf": "#f9f27f", # Quaternary (fluvial)
    "Qe": "#f9f27f", # Quaternary (eolian)
    "Qsk": "#f9f27f", # Quaternary (sahbka)
    "QT": "#ffe619", # Quaternary-Tertiary (could be "Neogene")
    "T": "rgb(253,154,82)", # Tertiary (could be "Paleogene")
    "TK": "rgb(253,167,95)", # Tertiary-Cretaceous (could be Paleocene)
    "K": "#7fc64e", # Cretaceous
    "KJ": "rgb(140,205,87)", # Cretaceous-Jurassic (could be Lower Cretaceous)
    "J": "#34b2c9", # Jurassic
    "JTr": "rgb(189,140,195)", # Jurassic-Triassic (will use Upper Triassic)
    "Tr": "#812b92", # Triassic
    "TrP": "rgb(251,167,148)", # Triassic-Permian (could be Lopingian)
    "P": "#f04028", # Permian
    "C": "#67a599", # Carboniferous
    "D": "#cb8c37", # Devonian
    "DSO": "rgb(179,225,182)", # Devonian-Silurian-Ordovician (will use Silurian)
    "OCm": "rgb(26,157,111)", #Ordovician-Cambrian (will use Lower ordovician)
    "Cm": "#7fa056", # Cambrian
    "Mz": "rgb(103,197,202)", # Mesozoic
    "MzPz": "rgb(103,197,202)", # Mesozoic-Paleozoic
    "Pz": "rgb(153,192,141)", # Paleozoic
    "pC": "rgb(247,67,112)", # PreCambrian undifferentiated
    "Kv": "#7fc64e", # Cretaceous volcanics
    "TKv": "rgb(253,154,82)", # Tertiary-Cretaceous volcanics
    "TKi": "rgb(253,154,82)", # Tertiary-Cretaceous intrusives
    "Qv": "#f9f27f", # Quaternary volcanics
    "QTv": "#f9f27f", # Quaternary-Tertiary volcanics
    "Czi": "rgb(242,249,29)", # Cenozoic intrusives
    "MzCzi": "rgb(103,197,202)", # Mesozoic-Cenozoic intrusives
    "MzCzv": "rgb(103,197,202)", # Mesozoic-Cenozoic volcanics
    "Pzi": "rgb(153,192,141)", # Paleozoic intrusives
    "H2O": "#00000000", # Ocean sea or open water
# * based on the Commission for the Geological Map of the World (CGWM). Paris, France.
}

def style(feature):
    return {
        "fillColor": color_dict.get(feature["properties"]["GLG"],"#000000"),
        "color": "black",
        "weight":0.25,
        "fillOpacity": 0.7
    }

m.add_geojson(
    url, layer_name="geo2bg",
    style_function=style,
    attribution="Pollastro, R.M., 1998",
)

m.to_streamlit(height=700)