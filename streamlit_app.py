import streamlit as st 
import pandas as pd

# Titel van de applicatie
st.title("STRC Waiting Time Calculator")

# List of variables
variables = [
    "Scen_shared_beds_Full", "Scen_NO_Sharing", "Scen_Part_bed_share", "Scen_Triage_ward", "Scen_Total_Sharing",
    "Priority", "Preference", "n_loc", "n_subruns", "n_clients_per_subrun", "n_clients_for_warming",
    "arr_HOS_High", "arr_GPR_High", "arr_EMD", "arr_HOS_GRZ", "arr_GPR_Low",
    "out_p_Home_High", "out_p_Home_GRZ", "out_p_Dead_High", "out_p_Dead_GRZ", "out_p_WMO_High", "out_p_WMO_GRZ",
    "out_p_WLZ_High", "out_p_WLZ_GRZ", "out_p_GRZV_High", "out_p_GRZV_GRZ", "out_p_Pall_High", "out_p_Pall_GRZ",
    "out_p_Home_Low", "out_p_Dead_Low", "out_p_WMO_Low", "out_p_WLZ_Low", "out_p_GRZV_Low", "out_p_Pall_Low",
    "serv_HOS_High", "serv_Home_High", "serv_Home_GRZ", "serv_Dead_High", "serv_Dead_GRZ", "serv_GRZV_High",
    "serv_GRZV_GRZ", "serv_Pall_High", "serv_Pall_GRZ", "serv_WMO_High", "serv_WLZ_High", "serv_WMO_GRZ",
    "serv_WLZ_GRZ", "serv_Home_Low", "serv_Dead_Low", "serv_GRZV_Low", "serv_Pall_Low", "serv_WMO_Low",
    "serv_WLZ_Low", "time_Max_Opn_EMD", "Opening_weekday", "EMD_start_time", "EMD_end_time", "GPR_start_time",
    "GPR_end_time", "p_opn_weekend", "Adm_days", "Max_days_TRW", "n_patients_per_nurse", "time_max_opn_ELV"
]

# Dictionary to store the inputs
inputs = {}

# Streamlit interface
st.title('Simulation Inputs')

# Create input boxes for each variable
for var in variables:
    inputs[var] = st.number_input(var, value=0)

# Button to display the dataframe
if st.button('Display DataFrame'):
    # Convert the inputs dictionary to a DataFrame
    df1 = pd.DataFrame([inputs])
    st.write(df1)

