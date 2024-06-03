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

import pandas as pd

# Function to save inputs to DataFrame
def save_inputs_to_dataframe(bed_share, num_locations, preference_type, priority_holds, beds_input, arr_GRZ, arr_HOS_High, arr_EMD, arr_GPR_High, arr_GPR_Low, serv_High_Home, serv_High_Hwa, serv_High_WLZ,serv_High_WMO,serv_High_Dead,serv_High_GRZV,serv_GRZ_Home, serv_GRZ_Hwa, serv_GRZ_WLZ,serv_GRZ_WMO,serv_GRZ_Dead,serv_GRZ_GRZV,serv_Low_Home, serv_Low_Hwa, serv_Low_WLZ,serv_Low_WMO,serv_Low_Dead,serv_Low_GRZV, p_Home_HC, p_HwA_HC, p_pall_HC, p_wlz_HC, p_wmo_HC, p_dead_HC,p_Home_LC, p_HwA_LC, p_pall_LC, p_wlz_LC, p_wmo_LC, p_dead_LC,p_Home_GRZ, p_HwA_GRZ, p_pall_GRZ, p_wlz_GRZ, p_wmo_GRZ, p_dead_GRZ,\
               opening_time_EMD_start,opening_time_EMD_end,opening_time_Huisarts_start,opening_time_Huisarts_end,opening_time_ELV_start,opening_time_ELV_end,open_in_weekend,subrun,k_per_sub,pat_warm,max_TRW,Adm_days,n_p_nurs):
    # Initialize dictionaries to store bed and nurse values for each location
    bed_values_dict = {f'{care_type}_beds': [] for care_type in ['elv_high_complex', 'high_complex', 'grz', 'shared', 'elv_low_complex', 'trw', 'total','emergency']}
    nurse_values_dict = {f'{care_type}_nurses': [] for care_type in ['elv_high_complex', 'high_complex', 'grz', 'shared', 'elv_low_complex', 'trw', 'total']}

    # Iterate through each location
    for i in range(1, num_locations + 1):
        # Initialize lists for the current location
        bed_values = {f'{care_type}_beds': 0 for care_type in ['elv_high_complex', 'high_complex', 'grz', 'shared', 'elv_low_complex', 'trw', 'total','emergency']}
        nurse_values = {f'{care_type}_nurses': 0 for care_type in ['elv_high_complex', 'high_complex', 'grz', 'shared', 'elv_low_complex', 'trw', 'total']}

        # Populate lists based on inputs received for the current location
        for item in beds_input:
            if isinstance(item, dict) and item['type'] == 'Input':
                input_id = item['props']['id']
                value = item['props']['value']
                location = int(input_id.split('_')[1])
                if location == i:
                    if 'elv' in input_id:
                        care_type = input_id.split('_')[2] +'_'+input_id.split('_')[3] + '_' + input_id.split('_')[4]
                    elif 'high' in input_id:
                        care_type = input_id.split('_')[2] + '_' + input_id.split('_')[3]
                    else:
                        care_type = input_id.split('_')[2]
                    if value:  # Check if the value is not empty
                        if 'nurses' in input_id:
                            nurse_values[f'{care_type}_nurses'] = int(value)
                        else:
                            bed_values[f'{care_type}_beds'] = int(value)
                            
        # Append values to the dictionaries
        for key in bed_values:
            bed_values_dict[key].append(bed_values[key])
        for key in nurse_values:
            nurse_values_dict[key].append(nurse_values[key])

    # Create a DataFrame
    df = pd.DataFrame(bed_values_dict)
    df_nurses = pd.DataFrame(nurse_values_dict)

    # Combine the nurse values DataFrame with the bed values DataFrame
    df = pd.concat([df, df_nurses], axis=1)

    # Creating a new DataFrame with each column containing a list of values from the corresponding column in df
    df1 = pd.DataFrame()
    for col in df.columns:
        if '_nurses' in col:
            df1[col] = [df[col][:2].tolist()]
        else:
            df1[col] = [df[col][:2].tolist()]

    # Add additional information to the DataFrame
    df1['Scen_full_bed_share'] = True if bed_share in ['full'] else False
    df1['Scen_part_bed_share'] = True if bed_share == 'partial' else False
    df1['Scen_NO_bed_share'] = True if bed_share in ['none','trw'] else False
    df1['Scen_total_bed_share'] = True if bed_share == 'total' else False
    df1['Scen_TRW'] = True if bed_share == 'trw' else False

    df1['Preference Type'] = preference_type
    df1['Priority Holds'] = 'priority_holds' in priority_holds
    df1['Number of Locations'] = num_locations
    
    df1['Arrival GRZ per dag'] = arr_GRZ
    df1['Arrival HOS High per dag'] = arr_HOS_High
    df1['Arrival EMD per dag'] = arr_EMD
    df1['Arrival GPR High per dag'] = arr_GPR_High
    df1['Arrival GPR Low per dag'] = arr_GPR_Low
    
    df1['Ligduur High complex care Home'] = serv_High_Home
    df1['Ligduur High complex care Hwa'] = serv_High_Hwa
    df1['Ligduur High complex care WLZ'] = serv_High_WLZ
    df1['Ligduur High complex care WMO'] = serv_High_WMO
    df1['Ligduur High complex care Dead'] = serv_High_Dead
    df1['Ligduur High complex care GRZV'] = serv_High_GRZV
    
    df1['Ligduur GRZ care Home'] = serv_GRZ_Home
    df1['Ligduur GRZ care Hwa'] = serv_GRZ_Hwa
    df1['Ligduur GRZ care WLZ'] = serv_GRZ_WLZ
    df1['Ligduur GRZ care WMO'] = serv_GRZ_WMO
    df1['Ligduur GRZ care Dead'] = serv_GRZ_Dead
    df1['Ligduur GRZ care GRZV'] = serv_GRZ_GRZV
    
    df1['Ligduur laag complex care Home'] = serv_Low_Home
    df1['Ligduur laag complex care Hwa'] = serv_Low_Hwa
    df1['Ligduur laag complex care WLZ'] = serv_Low_WLZ
    df1['Ligduur laag complex care WMO'] = serv_Low_WMO
    df1['Ligduur laag complex care Dead'] = serv_Low_Dead
    df1['Ligduur laag complex care GRZV'] = serv_Low_GRZV
    
    df1['Percentage uitstroom Home High Complex'] = p_Home_HC/100
    df1['Percentage uitstroom Home with adjustments High Complex'] = p_HwA_HC/100
    df1['Percentage uitstroom GRZ care High Complex'] = p_pall_HC/100
    df1['Percentage uitstroom WLZ High Complex'] = p_wlz_HC/100
    df1['Percentage uitstroom WMO High Complex'] = p_wmo_HC/100
    df1['Percentage uitstroom Dead High Complex'] = p_dead_HC/100
    df1['Percentage uitstroom Home Low Complex'] = p_Home_LC/100
    df1['Percentage uitstroom Home with adjustments Low Complex'] = p_HwA_LC/100
    df1['Percentage uitstroom GRZ care Low Complex'] = p_pall_LC/100
    df1['Percentage uitstroom WLZ Low Complex'] = p_wlz_LC/100
    df1['Percentage uitstroom WMO Low Complex'] = p_wmo_LC/100
    df1['Percentage uitstroom Dead Low Complex'] = p_dead_LC/100
    df1['Percentage uitstroom Home GRZ'] = p_Home_GRZ/100
    df1['Percentage uitstroom Home with adjustments GRZ'] = p_HwA_GRZ/100
    df1['Percentage uitstroom GRZ care GRZ'] = p_pall_GRZ/100
    df1['Percentage uitstroom WLZ GRZ'] = p_wlz_GRZ/100
    df1['Percentage uitstroom WMO GRZ'] = p_wmo_GRZ/100
    df1['Percentage uitstroom Dead GRZ'] = p_dead_GRZ/100

    df1['EMD starttijd'] =opening_time_EMD_start 
    df1['EMD eindtijd'] = opening_time_EMD_end
    df1['ELV starttijd'] = opening_time_ELV_start
    df1['ELV eindtijd'] = opening_time_ELV_end
    df1['Huisarts starttijd'] = opening_time_Huisarts_start
    df1['Huisarts eindtijd'] = opening_time_Huisarts_end
    df1['Open weekend'] = 1 if open_in_weekend else 0
    df1['n_subruns'] = subrun
    df1['patienten per subrun'] = k_per_sub
    df1['patienten voor warming'] = pat_warm
    df1['Max dagen TRW'] = max_TRW
    df1['Adm_days'] = Adm_days
    df1['Number of patients per nurse']= n_p_nurs
    df1['Maximaal aantal dagen TRW'] = max_TRW
    df1['n_loc'] = num_locations
    
    # Saving the DataFrame to a CSV file
    df1.to_csv('inputs.csv', index=False)

# Main Streamlit app
def main():
    st.title('Simulation Inputs')

    # Input fields for simulation parameters
    bed_share = st.radio('Bed Share Type', ['full', 'partial', 'none', 'total', 'trw'])
    num_locations = st.number_input('Number of Locations', min_value=1, step=1, value=1)
    preference_type = st.selectbox('Preference Type', ['type1', 'type2', 'type3'])
    priority_holds = st.multiselect('Priority Holds', ['hold1', 'hold2', 'hold3'])

    # Other input fields for each location
    for i in range(num_locations):
        st.header(f'Location {i+1}')
        # Add input fields here for each location

    # Button to save inputs and run simulation
    if st.button('Save Inputs'):
        save_inputs_to_dataframe(bed_share, num_locations, preference_type, priority_holds, beds_input, arr_GRZ, arr_HOS_High, arr_EMD, arr_GPR_High, arr_GPR_Low, serv_High_Home, serv_High_Hwa, serv_High_WLZ,serv_High_WMO,serv_High_Dead,serv_High_GRZV,serv_GRZ_Home, serv_GRZ_Hwa, serv_GRZ_WLZ,serv_GRZ_WMO,serv_GRZ_Dead,serv_GRZ_GRZV,serv_Low_Home, serv_Low_Hwa, serv_Low_WLZ,serv_Low_WMO,serv_Low_Dead,serv_Low_GRZV, p_Home_HC, p_HwA_HC, p_pall_HC, p_wlz_HC, p_wmo_HC, p_dead_HC,p_Home_LC, p_HwA_LC, p_pall_LC, p_wlz_LC, p_wmo_LC, p_dead_LC,p_Home_GRZ, p_HwA_GRZ, p_pall_GRZ, p_wlz_GRZ, p_wmo_GRZ, p_dead_GRZ,\
               opening_time_EMD_start,opening_time_EMD_end,opening_time_Huisarts_start,opening_time_Huisarts_end,opening_time_ELV_start,opening_time_ELV_end,open_in_weekend,subrun,k_per_sub,pat_warm,max_TRW,Adm_days,n_p_nurs)
        st.success('Inputs saved successfully!')
