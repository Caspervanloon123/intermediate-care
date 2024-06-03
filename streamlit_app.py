import streamlit as st 
import pandas as pd

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")


# Input box voor het aantal locaties
num_locations = st.number_input("Voer het aantal locaties in", min_value=1, step=1)

# Checkbox voor het aangeven van prioriteit
prioriteit = st.checkbox("Prioriteit")

def show_or_hide_arrival_inputs(flag):
    if flag:
        st.subheader("Aankomsten GRZ:")
        arrival_GRZ = st.number_input("Arrival GRZ per dag", value=0.54)

        st.subheader("Aankomsten High Complex:")
        arrival_HOS_High = st.number_input("Arrival HOS High per dag", value=0.94)
        arrival_EMD = st.number_input("Arrival EMD per dag", value=0.83)
        arrival_GPR_High = st.number_input("Arrival GPR High per dag", value=1.34)

        st.subheader("Aankomsten Low Complex:")
        arrival_GPR_Low = st.number_input("Arrival GPR Low per dag", value=1.91)
    else:
        st.write("")  # Empty placeholder to hide the inputs

# Title of the application
st.title("STRC Waiting Time Calculator")

# Flag to track the visibility of the arrival inputs
show_inputs = False

# Button to toggle the visibility of the arrival inputs
if st.button("Aankomsten"):
    show_inputs = not show_inputs  # Toggle the flag

# Show or hide the arrival inputs based on the flag
show_or_hide_arrival_inputs(show_inputs)
