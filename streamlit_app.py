import streamlit as st 
import pandas as pd

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")


# Input box voor het aantal locaties
num_locations = st.number_input("Voer het aantal locaties in", min_value=1, step=1)

# Checkbox voor het aangeven van prioriteit
prioriteit = st.checkbox("Prioriteit")

# Function to show the arrival inputs
def show_arrival_inputs():
    st.subheader("Aankomsten GRZ:")
    arrival_GRZ = st.number_input("Arrival GRZ per dag", value=0.54)

    st.subheader("Aankomsten High Complex:")
    arrival_HOS_High = st.number_input("Arrival HOS High per dag", value=0.94)
    arrival_EMD = st.number_input("Arrival EMD per dag", value=0.83)
    arrival_GPR_High = st.number_input("Arrival GPR High per dag", value=1.34)

    st.subheader("Aankomsten Low Complex:")
    arrival_GPR_Low = st.number_input("Arrival GPR Low per dag", value=1.91)

# Title of the application
st.title("STRC Waiting Time Calculator")

# Flag to track the visibility of the arrival inputs
show_inputs = st.checkbox("Aankomsten")

# Show the arrival inputs if the checkbox is checked
if show_inputs:
    show_arrival_inputs()
# Function to show or hide the service inputs based on a boolean flag
def show_or_hide_service_inputs(flag):
    if flag:
        st.subheader("Ligduur High Complex:")
        serv_High_Home = st.number_input("Ligduur High complex care Home (dagen)", value=31.1)
        serv_High_Hwa = st.number_input("Ligduur High complex care Hwa (dagen)", value=43.9)
        serv_High_GRZV = st.number_input("Ligduur High complex care GRZV (dagen)", value=29.8)
        serv_High_WLZ = st.number_input("Ligduur High complex care WLZ (dagen)", value=47.8)
        serv_High_WMO = st.number_input("Ligduur High complex care WMO (dagen)", value=22.9)
        serv_High_Dead = st.number_input("Ligduur High complex care Dead (dagen)", value=22.9)

        st.subheader("Percentage Ligduur GRZ:")
        serv_GRZ_Home = st.number_input("Ligduur GRZ care Home (dagen)", value=31.1)
        serv_GRZ_Hwa = st.number_input("Ligduur GRZ care Hwa (dagen)", value=43.9)
        serv_GRZ_GRZV = st.number_input("Ligduur GRZ care GRZV (dagen)", value=0)
        serv_GRZ_WMO = st.number_input("Ligduur GRZ care WMO (dagen)", value=22.9)
        serv_GRZ_WLZ = st.number_input("Ligduur GRZ care WLZ (dagen)", value=47.8)
        serv_GRZ_Dead = st.number_input("Ligduur GRZ care Dead (dagen)", value=22.9)

        st.subheader("Ligduur Low Complex:")
        serv_Low_Home = st.number_input("Ligduur laag complex care Home (dagen)", value=31.1)
        serv_Low_Hwa = st.number_input("Ligduur laag complex care Hwa (dagen)", value=43.9)
        serv_Low_GRZV = st.number_input("Ligduur laag complex care GRZV (dagen)", value=29.8)
        serv_Low_WMO = st.number_input("Ligduur laag complex care WMO (dagen)", value=22.9)
        serv_Low_WLZ = st.number_input("Ligduur laag complex care WLZ (dagen)", value=47.8)
        serv_Low_Dead = st.number_input("Ligduur laag complex care Dead (dagen)", value=22.9)
    else:
        st.write("")  # Empty placeholder to hide the inputs

# Title of the application
st.title("STRC Waiting Time Calculator")

# Checkbox to toggle the visibility of the service inputs
show_service_inputs = st.checkbox("Ligduur")

# Show or hide the service inputs based on the checkbox state
if show_service_inputs:
    show_or_hide_service_inputs(show_service_inputs)
