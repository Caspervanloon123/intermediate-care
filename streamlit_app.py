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
if bed_share == "Scen_shared_beds_Full":
    beds_High = []
    beds_Low = []
    nurs_low = []
    nurs_high = []
    beds_EMRD = []
    for i in range(0, n_loc):
        st.title('Location ' + str(i+1))
        beds_ELV_High = st.number_input(f"Number of ELV High Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
        nurs_ELV_High = st.number_input(f"Number of ELV High Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
        beds_ELV_Low = st.number_input(f"Number of ELV Low Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
        nurs_ELV_Low = st.number_input(f"Number of ELV Low Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
        beds_ELV_EMRD = st.number_input(f"Number of Emergency beds location {i+1}", min_value=0, step=1, value=0, format="%d")   
        beds_High.append(beds_ELV_High)
        beds_Low.append(beds_ELV_Low) 
        nurs_low.append(nurs_ELV_Low)
        nurs_high.append(nurs_ELV_High)
        beds_EMRD.append(beds_ELV_EMRD)
    inputs["elv_high_complex_beds"]  = beds_High
    inputs["elv_low_complex_beds"] = beds_Low
    inputs["elv_high_complex_nurses"] = nurs_high
    inputs["elv_low_complex_nurses"] = nurs_low
    inputs["emergency_beds"] = beds_EMRD
        

elif bed_share == "Scen_NO_Sharing":
    beds_G = []
    beds_High = []
    beds_low = []
    nurs_low = []
    nurs_high = []
    nurs_G = []
    beds_EMRD = []
    for i in range(1,n_loc):
        st.title('Location ', i)
        beds_GRZ = st.number_input("Number of GRZ beds location", min_value=0, step=1, value=0, format="%d")
        nurs_GRZ = st.number_input("Number of GRZ nurses location", min_value=0, step=1, value=0, format="%d")
        beds_High_Complex = st.number_input("Number of High Complex beds location", min_value=0, step=1, value=0, format="%d")
        nurs_High_Complex = st.number_input("Number of High Complex nurses location", min_value=0, step=1, value=0, format="%d")
        beds_ELV_Low = st.number_input("Number of ELV Low Complex beds location", min_value=0, step=1, value=0, format="%d")
        nurs_ELV_Low = st.number_input("Number of ELV Low Complex nurses location", min_value=0, step=1, value=0, format="%d")
        beds_ELV_EMRD = st.number_input("Number of Emergency beds", min_value=0, step=1, value=0, format="%d")
        beds_High.append(beds_High)
        beds_low.append(beds_ELV_Low)
        beds_G.append(beds_GRZ)
        nurs_G.append(nurs_GRZ)
        nurs_low.append(nurs_ELV_Low)
        nurs_high.append(nurs_ELV_High)
        beds_EMRD.append(beds_ELV_EMRD)
    inputs["high_complex_beds"]  = beds_High
    inputs["elv_low_complex_beds"] = beds_low
    inputs["high_complex_nurses"] = nurs_high
    inputs["elv_low_complex_nurses"] = nurs_low
    inputs["grz_beds"] = beds_G
    inputs["grz_nurses"] = nurs_G
    inputs["emergency_beds"] = beds_EMRD
elif bed_share == "Scen_Part_bed_share":
    beds_G = []
    beds_High = []
    beds_low = []
    nurs_low = []
    nurs_high = []
    nurs_G = []
    beds_shared = []
    beds_EMRD = []
    for i in range(1,n_loc):
        st.title('Location ', i)
        beds_GRZ = st.number_input("Number of GRZ beds location", min_value=0, step=1, value=0, format="%d")
        nurs_GRZ = st.number_input("Number of GRZ nurses location", min_value=0, step=1, value=0, format="%d")
        beds_High_Complex = st.number_input("Number of High Complex beds location", min_value=0, step=1, value=0, format="%d")
        nurs_High_Complex = st.number_input("Number of High Complex nurses location", min_value=0, step=1, value=0, format="%d")
        beds_ELV_Low = st.number_input("Number of ELV Low Complex beds location", min_value=0, step=1, value=0, format="%d")
        nurs_ELV_Low = st.number_input("Number of ELV Low Complex nurses location", min_value=0, step=1, value=0, format="%d")
        beds_ELV_Shared = st.number_input("Number of Shared beds", min_value=0, step=1, value=0, format="%d")
        beds_ELV_EMRD = st.number_input("Number of Emergency beds", min_value=0, step=1, value=0, format="%d")
        beds_High.append(beds_High)
        beds_low.append(beds_ELV_Low)
        beds_G.append(beds_GRZ)
        nurs_G.append(nurs_GRZ)
        nurs_low.append(nurs_ELV_Low)
        nurs_high.append(nurs_ELV_High)
        beds_shared.append(beds_ELV_Shared)
        beds_EMRD.append(beds_ELV_EMRD)
    inputs["high_complex_beds"]  = beds_High
    inputs["elv_low_complex_beds"] = beds_low
    inputs["high_complex_nurses"] = nurs_high
    inputs["elv_low_complex_nurses"] = nurs_low
    inputs["grz_beds"] = beds_G
    inputs["grz_nurses"] = nurs_G
    inputs["shared_beds"] = beds_shared
    inputs["emergency_beds"] = beds_EMRD
elif bed_share == "Scen_Triage_ward":
    beds_G = []
    beds_High = []
    beds_low = []
    nurs_low = []
    nurs_high = []
    nurs_G = []
    beds_TRW = []
    beds_EMRD = []
    for i in range(1,n_loc):
        st.title('Location ', i)
        beds_GRZ = st.number_input("Number of GRZ beds location", min_value=0, step=1, value=0, format="%d")
        nurs_GRZ = st.number_input("Number of GRZ nurses location", min_value=0, step=1, value=0, format="%d")
        beds_High_Complex = st.number_input("Number of High Complex beds location", min_value=0, step=1, value=0, format="%d")
        nurs_High_Complex = st.number_input("Number of High Complex nurses location", min_value=0, step=1, value=0, format="%d")
        beds_ELV_Low = st.number_input("Number of ELV Low Complex beds location", min_value=0, step=1, value=0, format="%d")
        nurs_ELV_Low = st.number_input("Number of ELV Low Complex nurses location", min_value=0, step=1, value=0, format="%d")
        beds_ELV_TRW = st.number_input("Number of Observation beds", min_value=0, step=1, value=0, format="%d")
        beds_ELV_EMRD = st.number_input("Number of Emergency beds", min_value=0, step=1, value=0, format="%d")
        beds_High.append(beds_High)
        beds_low.append(beds_ELV_Low)
        beds_G.append(beds_GRZ)
        nurs_G.append(nurs_GRZ)
        nurs_low.append(nurs_ELV_Low)
        nurs_high.append(nurs_ELV_High)
        beds_TRW.append(beds_ELV_TRW)
        beds_EMRD.append(beds_ELV_EMRD)
    inputs["high_complex_beds"]  = beds_High
    inputs["elv_low_complex_beds"] = beds_low
    inputs["high_complex_nurses"] = nurs_high
    inputs["elv_low_complex_nurses"] = nurs_low
    inputs["grz_beds"] = beds_G
    inputs["grz_nurses"] = nurs_G
    inputs["trw_beds"] = beds_TRW
    inputs["emergency_beds"] = beds_EMRD

elif bed_share == "Scen_Total_Sharing":
    beds_Total = []
    nurs_Total = []
    beds_EMRD = []
    for i in range(0, n_loc):
        st.title('Location ' + str(i+1))
        beds_ELV_Total = st.number_input(f"Number of ELV Total beds location {i+1}", min_value=0, step=1, value=0, format="%d")
        nurs_ELV_Total = st.number_input(f"Number of ELV Total nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
        beds_ELV_EMRD = st.number_input(f"Number of Emergency beds location {i+1}", min_value=0, step=1, value=0, format="%d")   
        beds_Total.append(beds_ELV_Total)
        nurs_Total.append(beds_ELV_Total) 
        beds_EMRD.append(beds_ELV_EMRD)
    inputs["total_beds"]  = beds_Total
    inputs["total_nurses"] = nurs_Total
    inputs["emergency_beds"] = beds_EMRD


def simulate(df1):
    return 1

# Button to display the dataframe
if st.button('Display DataFrame'):
    # Convert the inputs dictionary to a DataFrame
    df1 = pd.DataFrame([inputs])
    st.write(simulate(df1))
    st.write(df1)

