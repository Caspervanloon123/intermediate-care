import streamlit as st 
import pandas as pd

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")



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


# Checkbox to toggle the visibility of the service inputs
show_service_inputs = st.checkbox("Ligduur")

# Show or hide the service inputs based on the checkbox state
if show_service_inputs:
    show_or_hide_service_inputs(show_service_inputs)
# Function to show or hide the extra inputs based on a boolean flag
def show_or_hide_extra_inputs(flag):
    if flag:
        st.subheader("Percentage uitstroom High Complex:")
        p_Home_HC = st.number_input("Percentage uitstroom Home (%) High Complex", value=57.8)
        p_HwA_HC = st.number_input("Percentage uitstroom Home with adjustments (%) High Complex", value=10.7)
        p_pall_HC = st.number_input("Percentage uitstroom GRZV care (%) High Complex", value=3.4)
        p_wlz_HC = st.number_input("Percentage uitstroom WLZ (%) High Complex", value=19.8)
        p_wmo_HC = st.number_input("Percentage uitstroom WMO (%) High Complex", value=2.3)
        p_dead_HC = st.number_input("Percentage uitstroom Dead (%) High Complex", value=6)

        st.subheader("Percentage uitstroom GRZ:")
        p_Home_GRZ = st.number_input("Percentage uitstroom Home (%) GRZ", value=60)
        p_HwA_GRZ = st.number_input("Percentage uitstroom Home with adjustments (%) GRZ", value=10.7)
        p_pall_GRZ = st.number_input("Percentage uitstroom GRZV care (%) GRZ", value=0)
        p_wlz_GRZ = st.number_input("Percentage uitstroom WLZ (%) GRZ", value=21)
        p_wmo_GRZ = st.number_input("Percentage uitstroom WMO (%) GRZ", value=2.3)
        p_dead_GRZ = st.number_input("Percentage uitstroom Dead (%) GRZ", value=6)

        st.subheader("Percentage uitstroom Low Complex:")
        p_Home_LC = st.number_input("Percentage uitstroom Home (%) Low Complex", value=70)
        p_HwA_LC = st.number_input("Percentage uitstroom Home with adjustments (%) Low Complex", value=14)
        p_pall_LC = st.number_input("Percentage uitstroom GRZV care (%) Low Complex", value=2)
        p_wlz_LC = st.number_input("Percentage uitstroom WLZ (%) Low Complex", value=10)
        p_wmo_LC = st.number_input("Percentage uitstroom WMO (%) Low Complex", value=2)
        p_dead_LC = st.number_input("Percentage uitstroom Dead (%) Low Complex", value=2)
    else:
        st.write("")  # Empty placeholder to hide the inputs



# Checkbox to toggle the visibility of the extra inputs
show_extra_inputs = st.checkbox("Uitstroomkansen")

# Show or hide the extra inputs based on the checkbox state
if show_extra_inputs:
    show_or_hide_extra_inputs(show_extra_inputs)


# Function to show or hide the opening hours inputs based on a boolean flag
def show_or_hide_opening_hours_inputs(flag):
    if flag:
        st.subheader("Openingstijd EMD:")
        opening_time_EMD_start = st.number_input("Openingstijd EMD start", min_value=0, max_value=24, value=0)
        opening_time_EMD_end = st.number_input("Openingstijd EMD end", min_value=0, max_value=24, value=24)

        st.subheader("Openingstijd Huisarts:")
        opening_time_Huisarts_start = st.number_input("Openingstijd Huisarts start", min_value=0, max_value=24, value=8)
        opening_time_Huisarts_end = st.number_input("Openingstijd Huisarts end", min_value=0, max_value=24, value=17)

        st.subheader("Openingstijd ELV:")
        opening_time_ELV_start = st.number_input("Openingstijd ELV start", min_value=0, max_value=24, value=8)
        opening_time_ELV_end = st.number_input("Openingstijd ELV end", min_value=0, max_value=24, value=17)

        open_in_weekend = st.checkbox("Open in weekend", value=False)
    else:
        st.write("")  # Empty placeholder to hide the inputs



# Checkbox to toggle the visibility of the opening hours inputs
show_opening_hours_inputs = st.checkbox("Openingstijden")

# Show or hide the opening hours inputs based on the checkbox state
if show_opening_hours_inputs:
    show_or_hide_opening_hours_inputs(show_opening_hours_inputs)

# Function to show or hide the "Overig" inputs based on a boolean flag
def show_or_hide_overig_inputs(flag):
    if flag:
        st.subheader("Overig:")
        subrun = st.number_input("Aantal subruns", value=1)
        k_per_sub = st.number_input("Aantal patienten per subrun", value=1000)
        pat_warm = st.number_input("Aantal patienten voor warming", value=500)
        max_TRW = st.number_input("Maximaal aantal dagen TRW", value=14)
        Adm_days = st.number_input("Admission days", value=1.5)
        n_p_nurs = st.number_input("Number of patients per nurse", value=2)
    else:
        st.write("")  # Empty placeholder to hide the inputs

# Checkbox to toggle the visibility of the "Overig" inputs
show_overig_inputs = st.checkbox("Overig")

# Show or hide the "Overig" inputs based on the checkbox state
if show_overig_inputs:
    show_or_hide_overig_inputs(show_overig_inputs)


# Preference Type Dropdown
preference_type_options = ['First Come First Serve', 'Only Preference', 'Balance']
selected_preference_type = st.selectbox('Select Preference Type:', preference_type_options, index=0)


def display_bed_share_inputs(value, num_locations):
    beds_input = []

    if not num_locations or num_locations == 0:
        return beds_input  # Return an empty list if no locations are provided

    for i in range(num_locations):
        col1, col2 = st.columns(2)  # Split the layout into two columns
        if value in ['none']:
            with col1:
                beds_input.extend([
                    st.text_input(f'Location {i+1} _ High Complex Beds:', key=f'loc_{i+1}_high_complex_beds'),
                    st.text_input(f'Location {i+1} _ GRZ Beds:', key=f'loc_{i+1}_grz_beds'),
                    st.text_input(f'Location {i+1} _ Shared Beds:', key=f'loc_{i+1}_shared_beds'),
                    st.text_input(f'Location {i+1} _ ELV Low Complex Beds:', key=f'loc_{i+1}_elv_low_complex_beds'),
                    st.text_input(f'Location {i+1} _ Emergency Beds:', key=f'loc_{i+1}_emergency_beds')
                ])
            with col2:
                beds_input.extend([
                    st.text_input(f'Location {i+1} _ High Complex Nurses:', key=f'loc_{i+1}_high_complex_nurses'),
                    st.text_input(f'Location {i+1} _ GRZ Nurses:', key=f'loc_{i+1}_grz_nurses'),
                    st.text_input(f'Location {i+1} _ ELV Low Complex Nurses:', key=f'loc_{i+1}_elv_low_complex_nurses')
                ])
        # Add conditions for other bed share types

    return beds_input

# Example usage
num_locations = st.number_input("Number of Locations", min_value=0, value=1, step=1)
selected_bed_share = st.selectbox("Select Bed Share", ['none', 'full', 'partial', 'total', 'trw'])  # Add other options if needed
bed_share_inputs = display_bed_share_inputs(selected_bed_share, num_locations)

# Display the inputs
for input_element in bed_share_inputs:
    st.write(input_element)
