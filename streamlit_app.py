import streamlit as st 
import pandas as pd

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")


# Input box voor het aantal locaties
num_locations = st.number_input("Voer het aantal locaties in", min_value=1, step=1)

# Checkbox voor het aangeven van prioriteit
prioriteit = st.checkbox("Prioriteit")

# Toon het ingevoerde aantal locaties en de prioriteit
st.write("Aantal locaties:", num_locations)
if prioriteit:
    st.write("Prioriteit: Ja")
else:
    st.write("Prioriteit: Nee")
