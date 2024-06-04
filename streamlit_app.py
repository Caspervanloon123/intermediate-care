import streamlit as st 
import pandas as pd

# Inject custom CSS
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
   
    </style>
    """, unsafe_allow_html=True)

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
# Input for number of locations (integer only)
n_loc = st.number_input("Number of Locations", min_value=0, step=1, value=0, format="%d")
inputs["n_loc"] = n_loc
# Dropdown menu for the scenario variables
dropdown_var = st.selectbox("Choose Scenario", scenario_vars)
inputs[dropdown_var] = True  # Set the chosen scenario to True
bed_share = dropdown_var



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
#beds_input = {'high_complex': [], 'grz': [], 'shared': [],  'elv_high_complex': [], 'elv_low_complex':[], 'trw': [], 'total_elv_beds':[], 'emergency':[]}
if bed_share == "Scen_shared_beds_Full":
    for i in range(1,n_loc):
        st.number_input("Number of ELV High Complex beds location", min_value=0, step=1, value=0, format="%d")
# elif bed_share == :

# elif bed_share == :

# elif bed_share == :

# elif bed_share == :
# Button to display the dataframe
if st.button('Display DataFrame'):
    # Convert the inputs dictionary to a DataFrame
    df1 = pd.DataFrame([inputs])
    st.write(df1)

