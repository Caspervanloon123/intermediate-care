import streamlit as st 
import pandas as pd

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")

# List of scenario variables
scenario_vars = [
    "Scen_shared_beds_Full", "Scen_NO_Sharing", "Scen_Part_bed_share", "Scen_Triage_ward", "Scen_Total_Sharing"
]

# Grouped variables
groups = {
    "Aankomst": ["arr_HOS_High", "arr_GPR_High", "arr_EMD", "arr_HOS_GRZ", "arr_GPR_Low"],
    "Servicetijden": [
        "serv_HOS_High", "serv_Home_High", "serv_Home_GRZ", "serv_Dead_High", "serv_Dead_GRZ", "serv_GRZV_High",
        "serv_GRZV_GRZ", "serv_Pall_High", "serv_Pall_GRZ", "serv_WMO_High", "serv_WLZ_High", "serv_WMO_GRZ",
        "serv_WLZ_GRZ", "serv_Home_Low", "serv_Dead_Low", "serv_GRZV_Low", "serv_Pall_Low", "serv_WMO_Low",
        "serv_WLZ_Low"
    ],
    "Uitstroomkansen": [
        "out_p_Home_High", "out_p_Home_GRZ", "out_p_Dead_High", "out_p_Dead_GRZ", "out_p_WMO_High", "out_p_WMO_GRZ",
        "out_p_WLZ_High", "out_p_WLZ_GRZ", "out_p_GRZV_High", "out_p_GRZV_GRZ", "out_p_Pall_High", "out_p_Pall_GRZ",
        "out_p_Home_Low", "out_p_Dead_Low", "out_p_WMO_Low", "out_p_WLZ_Low", "out_p_GRZV_Low", "out_p_Pall_Low"
    ],
    "Openingstijden": [
        "time_Max_Opn_EMD", "Opening_weekday", "EMD_start_time", "EMD_end_time", "GPR_start_time",
        "GPR_end_time", "p_opn_weekend", "time_max_opn_ELV"
    ],
    "Overig": [
        "n_patients_per_nurse", "Adm_days", "Max_days_TRW", "n_subruns", "n_clients_per_subrun", "n_clients_for_warming"
    ]
}

# Dictionary to store the inputs
inputs = {var: False for var in scenario_vars}  # Initialize scenario variables to False

# Streamlit interface
st.title('Simulation Inputs')

# Dropdown menu for the scenario variables
dropdown_var = st.selectbox("Choose Scenario", scenario_vars)
inputs[dropdown_var] = True  # Set the chosen scenario to True

# Checkbox for Priority
inputs["Priority"] = st.checkbox("Priority")

# Dropdown menu for Preference
preference_options = ["FCFS", "Voorkeur", "Model"]
inputs["Preference"] = st.selectbox("Preference", preference_options)

# Expanders for grouped variables
for group_name, group_vars in groups.items():
    with st.expander(group_name):
        for var in group_vars:
            inputs[var] = st.number_input(var, value=0)

# Button to display the dataframe
if st.button('Display DataFrame'):
    # Convert the inputs dictionary to a DataFrame
    df1 = pd.DataFrame([inputs])
    st.write(df1)
