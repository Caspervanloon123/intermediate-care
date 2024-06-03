import streamlit as st 
import pandas as pd

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")


# Input box voor het aantal locaties
num_locations = st.number_input("Voer het aantal locaties in", min_value=1, step=1)

# Checkbox voor het aangeven van prioriteit
prioriteit = st.checkbox("Prioriteit")

# Functie om de invoervelden voor aankomsten te tonen
def show_arrival_inputs():
    st.subheader("Aankomsten GRZ:")
    arrival_GRZ = st.number_input("Arrival GRZ per dag", value=0.54)

    st.subheader("Aankomsten High Complex:")
    arrival_HOS_High = st.number_input("Arrival HOS High per dag", value=0.94)
    arrival_EMD = st.number_input("Arrival EMD per dag", value=0.83)
    arrival_GPR_High = st.number_input("Arrival GPR High per dag", value=1.34)

    st.subheader("Aankomsten Low Complex:")
    arrival_GPR_Low = st.number_input("Arrival GPR Low per dag", value=1.91)

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")

# Knop om de aankomsten te tonen
if st.button("Aankomsten"):
    show_arrival_inputs()
