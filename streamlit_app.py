#import matplotlib.pyplot as plt
import streamlit as st 
import pandas as pd

page_bg_img = """
<style>
[data-testid="header-permalink-button"]{

}
</style> 
"""
st.markdown(page_bg_img,unsafe_allow_html = True)

# st.set_page_config(layout="wide")
st.title("ELV SIMULATIE")
col1, col2, col3 = st.columns((2, 3, 3)) 

with col1:
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
    from decimal import Decimal
    
    # Define default decimal values for all variables
    default_values = {
        "Aankomst Hoog Complex vanuit ziekenhuis per dag": 0.94,
        "Aankomst vanaf Huisarts Hoog Complex per dag": 1.34,
        "Aankomst vanaf de Spoedeisendehulp per dag": 0.83,
        "Aankomst Geriatrische Zorg in Ziekenhuis per dag": 0.54,
        "Aankomst Laag Complexe zorg vanaf de Huisarts": 1.91,
        "Ligduur Hoog Complex naar Huis": 31.1,
        "Ligduur Geriatrische Zorg naar Huis": 31.1,
        "Ligduur Hoog Complex Dood": 22.9,
        "Ligduur Geriatrische Zorg Dood": 22.9,
        "Ligduur Hoog Complex naar Geriatrische Zorg": 29.8,
        "Ligduur Hoog Complex naar Huis met aanpassingen": 43.9,
        "Ligduur Geriatrische Zorg naar Huis met aanpassingen": 43.9,
        "Ligduur Hoog Complex WMO": 22.9,
        "Ligduur Hoog Complex WLZ": 47.8,
        "Ligduur Geriatrische Zorg WMO": 22.9,
        "Ligduur Geriatrische Zorg WLZ": 47.8,
        "Ligduur Laag Complex naar Huis": 31.1,
        "Ligduur Laag Complex Dood": 22.9,
        "Ligduur Laag Complex Geriatrische Zorg": 29.8,
        "Ligduur Laag Complex naar Huis met aanpassingen": 43.9,
        "Ligduur Laag Complex WMO": 22.9,
        "Ligduur Laag Complex WLZ": 47.8,
        "Percentage Hoog Complex naar Huis": 57.8,
        "Percentage Geriatrische Zorg naar Huis": 60.0,
        "Percentage Hoog Complex Dood": 6.0,
        "Percentage Geriatrische Zorg Dood": 6.0,
        "Percentage Hoog Complex WMO": 2.3,
        "Percentage Geriatrische Zorg WMO": 2.3,
        "Percentage Hoog Complex WLZ": 19.8,
        "Percentage Geriatrische Zorg WLZ": 21.0,
        "Percentage Hoog Complex naar Geriatrische Zorg": 3.4,
        "Percentage Hoog Complex naar Huis met aanpassingen": 10.7,
        "Percentage Geriatrische Zorg naar Huis met aanpassingen": 10.7,
        "Percentage Laag Complex naar Huis": 70.0,
        "Percentage Laag Complex Dood": 2.0,
        "Percentage Laag Complex WMO": 2.0,
        "Percentage Laag Complex WLZ": 10.0,
        "Percentage Laag Complex naar Geriatrische Zorg": 2.0,
        "Percentage Laag Complex naar Huis met aanpassingen": 14.0,
        "Spoedeisendehulp openingstijd": 0,
        "Spoedeisendehulp sluitingstijd": 24,
        "Openingstijd Huisarts": 8.0,
        "Sluittijd Huisarts": 17.0,
        "Opname in het weekend": False,
        "Openingstijd ELV": 8.0,
        "Sluitingstijd ELV": 17.0,
        "Aantal patienten per verpleegkundige": 3,
        "Transfertijd": 1.5,
        "Maximaal aantal dagen observatie": 14.0,
        "Aantal subruns": 1,
        "Aantal patienten per subrun": 1000,
        "Aantal patienten voor warming": 500,
    }
    
    
    # List of scenario variables
    scenario_vars_1 = [
        "Volledige beddeldeling", "Geen beddendeling", "Partiële beddendeling", "Observatiebedden", "Totale beddendeling"
    ]
    scenario_vars = [
        "Scen_shared_beds_Full","Scen_Total_Sharing","Scen_Triage_ward","Scen_NO_Sharing","Scen_Part_bed_share"
    ]
    
    # Grouped variables
    groups = {
        "Aankomst": ["Aankomst Hoog Complex vanuit ziekenhuis per dag", "Aankomst vanaf Huisarts Hoog Complex per dag", "Aankomst vanaf de Spoedeisendehulp per dag", "Aankomst Geriatrische Zorg in Ziekenhuis per dag", "Aankomst Laag Complexe zorg vanaf de Huisarts"],
        "Ligduur": [
            "Ligduur Hoog Complex naar Huis", "Ligduur Geriatrische Zorg naar Huis", "Ligduur Hoog Complex Dood", "Ligduur Geriatrische Zorg Dood", "Ligduur Hoog Complex naar Geriatrische Zorg",
             "Ligduur Hoog Complex naar Huis met aanpassingen", "Ligduur Geriatrische Zorg naar Huis met aanpassingen", "Ligduur Hoog Complex WMO", "Ligduur Hoog Complex WLZ", "Ligduur Geriatrische Zorg WMO",
            "Ligduur Geriatrische Zorg WLZ", "Ligduur Laag Complex naar Huis", "Ligduur Laag Complex Dood", "Ligduur Laag Complex Geriatrische Zorg", "Ligduur Laag Complex naar Huis met aanpassingen", "Ligduur Laag Complex WMO",
            "Ligduur Laag Complex WLZ"
        ],
        "Uitstroomkansen": [
            "Percentage Hoog Complex naar Huis", "Percentage Geriatrische Zorg naar Huis", "Percentage Hoog Complex Dood", "Percentage Geriatrische Zorg Dood", "Percentage Hoog Complex WMO", "Percentage Geriatrische Zorg WMO",
            "Percentage Hoog Complex WLZ", "Percentage Geriatrische Zorg WLZ", "Percentage Hoog Complex naar Geriatrische Zorg", "Percentage Hoog Complex naar Huis met aanpassingen", "Percentage Geriatrische Zorg naar Huis met aanpassingen",
            "Percentage Laag Complex naar Huis", "Percentage Laag Complex Dood", "Percentage Laag Complex WMO", "Percentage Laag Complex WLZ", "Percentage Laag Complex naar Geriatrische Zorg", "Percentage Laag Complex naar Huis met aanpassingen"
        ],
        "Openingstijden": [
            "Spoedeisendehulp openingstijd", "Spoedeisendehulp sluitingstijd", "Openingstijd Huisarts",
            "Sluittijd Huisarts", "Opname in het weekend", "Openingstijd ELV", "Sluitingstijd ELV"
        ],
        "Overig": [
            "Aantal patienten per verpleegkundige", "Transfertijd", "Maximaal aantal dagen observatie", "Aantal subruns", "Aantal patienten per subrun", "Aantal patienten voor warming"
        ]
    }
    
    # Streamlit interface

    # Input for number of locations (integer only)
    Inputs_1 = pd.DataFrame()
    inputs = pd.DataFrame()
    
    n_loc = st.number_input("Aantal locaties", min_value=0, step=1, value=0, format="%d")
    Inputs_1.loc[0,"n_loc"] = n_loc
    
    # Dropdown menu for the scenario variables
    dropdown_var = st.selectbox("Beddeling", scenario_vars_1)
    bed_share = dropdown_var
    if dropdown_var == "Volledige beddeldeling":
        Inputs_1.loc[0,"Scen_shared_beds_Full"] = True
        Inputs_1.loc[0,"Scen_Total_Sharing"] = False
        Inputs_1.loc[0,"Scen_Triage_ward"] = False
        Inputs_1.loc[0,"Scen_NO_Sharing"] = False
        Inputs_1.loc[0,"Scen_Part_bed_share"] = False
    elif dropdown_var == "Totale beddendeling":
        Inputs_1.loc[0,"Scen_shared_beds_Full"] = False
        Inputs_1.loc[0,"Scen_Total_Sharing"] = True
        Inputs_1.loc[0,"Scen_Triage_ward"] = False
        Inputs_1.loc[0,"Scen_NO_Sharing"] = False
        Inputs_1.loc[0,"Scen_Part_bed_share"] = False
    elif dropdown_var == "Observatiebedden":
        Inputs_1.loc[0,"Scen_shared_beds_Full"] = False
        Inputs_1.loc[0,"Scen_Total_Sharing"] = False
        Inputs_1.loc[0,"Scen_Triage_ward"] = True
        Inputs_1.loc[0,"Scen_NO_Sharing"] = True
        Inputs_1.loc[0,"Scen_Part_bed_share"] = False
    elif dropdown_var == "Partiële beddendeling":
        Inputs_1.loc[0,"Scen_shared_beds_Full"] = False
        Inputs_1.loc[0,"Scen_Total_Sharing"] = False
        Inputs_1.loc[0,"Scen_Triage_ward"] = False
        Inputs_1.loc[0,"Scen_NO_Sharing"] = False
        Inputs_1.loc[0,"Scen_Part_bed_share"]= True
    elif dropdown_var == "Geen beddendeling":
        Inputs_1.loc[0,"Scen_shared_beds_Full"] = False
        Inputs_1.loc[0,"Scen_Total_Sharing"] = False
        Inputs_1.loc[0,"Scen_Triage_ward"] = False
        Inputs_1.loc[0,"Scen_NO_Sharing"] = True
        Inputs_1.loc[0,"Scen_Part_bed_share"] = False
    
    # Checkbox for Priority
    Priority = st.checkbox("Priority")
    Inputs_1.loc[0,"Priority"] = Priority
    
    # Dropdown menu for Preference
    preference_options = ["FCFS", "Voorkeur", "Model"]
    preference = st.selectbox("Allocatie", preference_options)
    Inputs_1.loc[0,"preference"] = preference

    for group_name, group_vars in groups.items():
        with st.expander(group_name):
            for var in group_vars:
                default_value = default_values[var]  # Get default value for the variable
                if var == "Opname in het weekend":
                    Inputs_1.loc[0, var] = st.checkbox(var)
                else:
                    Inputs_1.loc[0, var] = st.number_input(var, value=default_value)
    #st.button('Start Simulation')
with col2:
    # with col2:
    if bed_share == "Volledige beddeldeling":
        listofzeros = 0
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
        data = {
            "elv_high_complex_beds": [beds_High],
            "elv_low_complex_beds": [beds_Low],
            "elv_high_complex_nurses": [nurs_high],
            "elv_low_complex_nurses": [nurs_low],
            "emergency_beds": [beds_EMRD],
            "high_complex_beds": [0],
            "grz_beds": [0],
            "shared_beds": [0],
            "trw_beds": [0],
            "total_beds": [0],
            "high_complex_nurses": [0],
            "grz_nurses": [0],
            "shared_nurses": [0],
            "trw_nurses": [0],
            "total_nurses": [0]
        }
        df = pd.DataFrame(data)
    
        # Concatenate the DataFrame with the existing DataFrame
        inputs = pd.concat([inputs, df], ignore_index=True)
    
    elif bed_share == "Geen beddendeling":
        listofzeros = 0
        beds_G = []
        beds_High = []
        beds_low = []
        nurs_low = []
        nurs_high = []
        nurs_G = []
        beds_EMRD = []
        for i in range(0, n_loc):
            st.title('Location '+ str(i+1))
            beds_GRZ = st.number_input(f"Number of GRZ beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_GRZ = st.number_input(f"Number of GRZ nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_High_Complex = st.number_input(f"Number of High Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_High_Complex = st.number_input(f"Number of High Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_Low = st.number_input(f"Number of ELV Low Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_ELV_Low = st.number_input(f"Number of ELV Low Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_EMRD = st.number_input(f"Number of Emergency beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_High.append(beds_High_Complex)
            beds_low.append(beds_ELV_Low)
            beds_G.append(beds_GRZ)
            nurs_G.append(nurs_GRZ)
            nurs_low.append(nurs_ELV_Low)
            nurs_high.append(nurs_High_Complex)
            beds_EMRD.append(beds_ELV_EMRD)
            
        data = {
            "elv_high_complex_beds": [0],
            "elv_low_complex_beds": [beds_low],
            "elv_high_complex_nurses": [0],
            "elv_low_complex_nurses": [nurs_low],
            "emergency_beds": [beds_EMRD],
            "high_complex_beds": [beds_High],
            "grz_beds": [beds_G],
            "shared_beds": [0],
            "trw_beds": [0],
            "total_beds": [0],
            "high_complex_nurses": [nurs_high],
            "grz_nurses": [nurs_G],
            "shared_nurses": [0],
            "trw_nurses": [0],
            "total_nurses": [0]
        }
        df = pd.DataFrame(data)
    
        # Concatenate the DataFrame with the existing DataFrame
        inputs = pd.concat([inputs, df], ignore_index=True)
    elif bed_share == "Partiële beddendeling":
        listofzeros = 0
        beds_G = []
        beds_High = []
        beds_low = []
        nurs_low = []
        nurs_high = []
        nurs_G = []
        beds_shared = []
        beds_EMRD = []
        for i in range(0, n_loc):
            st.title('Location '+ str(i+1))
            beds_GRZ = st.number_input(f"Number of GRZ beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_GRZ = st.number_input(f"Number of GRZ nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_High_Complex = st.number_input(f"Number of High Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_High_Complex = st.number_input(f"Number of High Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_Low = st.number_input(f"Number of ELV Low Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_ELV_Low = st.number_input(f"Number of ELV Low Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_Shared = st.number_input(f"Number of Shared beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_EMRD = st.number_input(f"Number of Emergency beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_High.append(beds_High_Complex)
            beds_low.append(beds_ELV_Low)
            beds_G.append(beds_GRZ)
            nurs_G.append(nurs_GRZ)
            nurs_low.append(nurs_ELV_Low)
            nurs_high.append(nurs_High_Complex)
            beds_shared.append(beds_ELV_Shared)
            beds_EMRD.append(beds_ELV_EMRD)
        data = {
            "elv_high_complex_beds": [0],
            "elv_low_complex_beds": [beds_low],
            "elv_high_complex_nurses": [0],
            "elv_low_complex_nurses": [nurs_low],
            "emergency_beds": [beds_EMRD],
            "high_complex_beds": [beds_High],
            "grz_beds": [beds_G],
            "shared_beds": [beds_shared],
            "trw_beds": [0],
            "total_beds": [0],
            "high_complex_nurses": [nurs_high],
            "grz_nurses": [nurs_GRZ],
            "shared_nurses": [0],
            "trw_nurses": [0],
            "total_nurses": [0]
        }
        df = pd.DataFrame(data)
    
        # Concatenate the DataFrame with the existing DataFrame
        inputs = pd.concat([inputs, df], ignore_index=True)
    elif bed_share == "Observatiebedden":
        listofzeros = 0
        beds_G = []
        beds_High = []
        beds_low = []
        nurs_low = []
        nurs_high = []
        nurs_G = []
        beds_TRW = []
        beds_EMRD = []
        for i in range(0, n_loc):
            st.title('Location '+ str(i+1))
            beds_GRZ = st.number_input(f"Number of GRZ beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_GRZ = st.number_input(f"Number of GRZ nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_High_Complex = st.number_input(f"Number of High Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_High_Complex = st.number_input(f"Number of High Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_Low = st.number_input(f"Number of ELV Low Complex beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            nurs_ELV_Low = st.number_input(f"Number of ELV Low Complex nurses location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_TRW = st.number_input(f"Number of Observation beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_ELV_EMRD = st.number_input(f"Number of Emergency beds location {i+1}", min_value=0, step=1, value=0, format="%d")
            beds_High.append(beds_High_Complex)
            beds_low.append(beds_ELV_Low)
            beds_G.append(beds_GRZ)
            nurs_G.append(nurs_GRZ)
            nurs_low.append(nurs_ELV_Low)
            nurs_high.append(nurs_High_Complex)
            beds_TRW.append(beds_ELV_TRW)
            beds_EMRD.append(beds_ELV_EMRD)
        data = {
            "elv_high_complex_beds": [0],
            "elv_low_complex_beds": [beds_low],
            "elv_high_complex_nurses": [0],
            "elv_low_complex_nurses": [nurs_low],
            "emergency_beds": [beds_EMRD],
            "high_complex_beds": [beds_High],
            "grz_beds": [beds_G],
            "shared_beds": [0],
            "trw_beds": [beds_TRW],
            "total_beds": [0],
            "high_complex_nurses": [nurs_high],
            "grz_nurses": [nurs_GRZ],
            "shared_nurses": [0],
            "trw_nurses": [0],
            "total_nurses": [0]
        }
        df = pd.DataFrame(data)
    
        # Concatenate the DataFrame with the existing DataFrame
        inputs = pd.concat([inputs, df], ignore_index=True)
    elif bed_share == "Totale beddendeling":
        listofzeros = 0
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
        data = {
            "elv_high_complex_beds": [0],
            "elv_low_complex_beds": [0],
            "elv_high_complex_nurses": [0],
            "elv_low_complex_nurses": [0],
            "emergency_beds": [beds_EMRD],
            "high_complex_beds": [0],
            "grz_beds": [0],
            "shared_beds": [0],
            "trw_beds": [0],
            "total_beds": [beds_Total],
            "high_complex_nurses": [0],
            "grz_nurses": [0],
            "shared_nurses": [0],
            "trw_nurses": [0],
            "total_nurses": [nurs_Total]
        }
        df = pd.DataFrame(data)
    
        # Concatenate the DataFrame with the existing DataFrame
        inputs = pd.concat([inputs, df], ignore_index=True)
    
    df_tot = pd.concat([Inputs_1,inputs],axis = 1)
    def simulate(input):
        for loop_nr in range(len(input)):
            from datetime import datetime
    
            # BEGIN # -----------------------------------------
            import pandas as pd
            import random as rd
            import math
            import numpy as np
            import operator
            import bisect
            import time
            #import matplotlib.pyplot as plt
            #import scipy.stats
            #import ast
            #import os
            from random import randrange
            import json
            import random
            
            print('')
            print('-------------------------------------------------')
            print('---------------- LOOP NUMBER ', loop_nr,'-----------------')
            print('-------------------------------------------------')
            print('')
        
            # INPUT <<<<<<<<<<<<<<
        
            
            n_subruns = input.loc[loop_nr,'Aantal subruns']
            
            n_clients_per_subrun = input.loc[loop_nr,'Aantal patienten per subrun']
            n_clients_for_warming = input.loc[loop_nr,'Aantal patienten voor warming']
        
            print_modus = False  
        
            arr_HOS_High =  input.loc[loop_nr,'Aankomst Hoog Complex vanuit ziekenhuis per dag']
            arr_HOS_GRZ = input.loc[loop_nr,'Aankomst Geriatrische Zorg in Ziekenhuis per dag']
            arr_GPR_High = input.loc[loop_nr,'Aankomst vanaf Huisarts Hoog Complex per dag']
            arr_GPR_Low = input.loc[loop_nr,'Aankomst Laag Complexe zorg vanaf de Huisarts']
        
            arr_EMD = input.loc[loop_nr,'Aankomst vanaf de Spoedeisendehulp per dag']
            
            
            
            out_p_Home_High = input.loc[loop_nr,'Percentage Hoog Complex naar Huis']
            out_p_Dead_High = input.loc[loop_nr,'Percentage Hoog Complex Dood']
            out_p_WMO_High = input.loc[loop_nr,'Percentage Hoog Complex WMO']
            out_p_WLZ_High = input.loc[loop_nr,'Percentage Hoog Complex WLZ']
            out_p_GRZV_High = input.loc[loop_nr,'Percentage Hoog Complex naar Geriatrische Zorg']
            out_p_Pall_High = input.loc[loop_nr,'Percentage Hoog Complex naar Huis met aanpassingen']
            
            out_p_Home_Low = input.loc[loop_nr,'Percentage Laag Complex naar Huis']
            out_p_Dead_Low = input.loc[loop_nr,'Percentage Laag Complex Dood']
            out_p_WMO_Low = input.loc[loop_nr,'Percentage Laag Complex WMO']
            out_p_WLZ_Low = input.loc[loop_nr,'Percentage Laag Complex WLZ']
            out_p_GRZV_Low = input.loc[loop_nr,'Percentage Laag Complex naar Geriatrische Zorg']
            out_p_Pall_Low = input.loc[loop_nr,'Percentage Laag Complex naar Huis met aanpassingen']
            
            serv_Home_High = 1/input.loc[loop_nr,'Ligduur Hoog Complex naar Huis']
            serv_Dead_High = 1/input.loc[loop_nr,'Ligduur Hoog Complex Dood']
            
            serv_GRZV_High = 1/input.loc[loop_nr,'Ligduur Hoog Complex naar Geriatrische Zorg']
            serv_Pall_High = 1/input.loc[loop_nr,'Ligduur Hoog Complex naar Huis met aanpassingen']
            serv_WMO_High = 1/input.loc[loop_nr,'Ligduur Hoog Complex WMO']
            serv_WLZ_High = 1/input.loc[loop_nr,'Ligduur Hoog Complex WLZ']
            
            serv_Home_Low = 1/input.loc[loop_nr,'Ligduur Laag Complex naar Huis']
            serv_Dead_Low = 1/input.loc[loop_nr,'Ligduur Laag Complex Dood']
            
            serv_GRZV_Low = 1/input.loc[loop_nr,'Ligduur Laag Complex Geriatrische Zorg']
            serv_Pall_Low = 1/input.loc[loop_nr,'Ligduur Laag Complex naar Huis met aanpassingen']
            serv_WMO_Low = 1/input.loc[loop_nr,'Ligduur Laag Complex WMO']
            serv_WLZ_Low = 1/input.loc[loop_nr,'Ligduur Laag Complex WLZ']
        
            
            time_max_opn_ELV = input.loc[loop_nr,'Sluitingstijd ELV']/24
            ELV_start_time = input.loc[loop_nr,'Openingstijd ELV']/24
        
            EMD_start_time = input.loc[loop_nr,'Spoedeisendehulp openingstijd']/24
            EMD_end_time = input.loc[loop_nr,'Spoedeisendehulp sluitingstijd']/24
            GPR_start_time = input.loc[loop_nr,'Openingstijd Huisarts']/24
            GPR_end_time = input.loc[loop_nr,'Sluittijd Huisarts']/24
        
            
            p_opn_weekend = 1 if input.loc[loop_nr,'Opname in het weekend'] else 0
        
            Scen_tr_ward = input.loc[loop_nr,'Scen_Triage_ward']
            Scen_shared_beds_Full = input.loc[loop_nr,'Scen_shared_beds_Full']
            Scen_NO_Sharing = input.loc[loop_nr,'Scen_NO_Sharing']
            Scen_part_bed_Share = input.loc[loop_nr,'Scen_Part_bed_share']
            Scen_Total_Sharing = input.loc[loop_nr,'Scen_Total_Sharing']
            priority = input.loc[loop_nr,'Priority']
            Project = ''#input.loc[loop_nr,'Project']
            Preference = input.loc[loop_nr,'preference'] #Pref = pref_model, FCFS = FCFS, NO = Only fav location
            n_patients_per_nurse = input.loc[loop_nr,'Aantal patienten per verpleegkundige']
            
            
            
            
            adm_days = 1/input.loc[loop_nr,'Transfertijd']
        
            
            max_days_TRW = input.loc[loop_nr,'Maximaal aantal dagen observatie']
        
        
            
            out_p_Home_GRZ = input.loc[loop_nr,'Percentage Geriatrische Zorg naar Huis']
            out_p_Dead_GRZ = input.loc[loop_nr,'Percentage Geriatrische Zorg Dood']
            out_p_WMO_GRZ = input.loc[loop_nr,'Percentage Geriatrische Zorg WMO']
            out_p_WLZ_GRZ = input.loc[loop_nr,'Percentage Geriatrische Zorg WLZ']
            out_p_GRZV_GRZ = 0# input.loc[loop_nr,'Percentage Geriatrische Zorg GRZ care GRZ']
            out_p_Pall_GRZ = input.loc[loop_nr,'Percentage Geriatrische Zorg naar Huis met aanpassingen']
            
            serv_Home_GRZ = 1/input.loc[loop_nr,'Ligduur Geriatrische Zorg naar Huis']
            serv_Dead_GRZ = 1/input.loc[loop_nr,'Ligduur Geriatrische Zorg Dood']
            serv_GRZV_GRZ = 0#1/input.loc[loop_nr,'serv_GRZV_GRZ']
            serv_Pall_GRZ = 1/input.loc[loop_nr,'Ligduur Geriatrische Zorg naar Huis met aanpassingen']
            serv_WMO_GRZ = 1/input.loc[loop_nr,'Ligduur Geriatrische Zorg WMO']
            serv_WLZ_GRZ = 1/input.loc[loop_nr,'Ligduur Geriatrische Zorg WLZ']
        
            # start simulatie
            
            start_time = time.process_time()
            n_subrun = 0
            np.random.seed(0)
            rd.seed(0)
               
            # output values
         
            # alvast de zero lists en parameters hierin zetten
            Fairness_list = [0]
            nr_pat_trans_mean = 0
            n_beds_ELV_Low=0
            n_beds_ELV_High=0
            n_beds_GRZ=0
            n_beds_High_Complex=0
            n_beds_ELV_Low =0
            n_beds_shared = 0
            n_client = 0
            n_subrun = 0
            n_beds_ELV_total_list = []
            client_dict = {}
            output_dict = {}
            w_tot_dict = {}
            w1_dict = {}
            w2_dict = {}
            w3_dict = {}
            w4_dict = {}
            w2_dict_TRW = {}
            w3_dict_TRW = {}
            w4_dict_TRW = {}
            wait_list_1 = []
            wait_list_3 = []
            wait_list_2 = []
            type_of_w2 = []
            wait_list_1_TRW =[]
            wait_list_3_TRW = []
            wait_list_2_TRW = []
            type_of_w2_TRW = []
            wait_list_Total = []
            len_w_total_list = []
            tot_cost_trw_help = []
            n_evaluated = 0
            blabla = 0
            len_w4_list = []
            
            # output lists
                          
            bez_gr_EMDR_list = []
            len_w2_list = []
            wait_time_ELV_High = []
            wait_time_ELV_Low = []
            wait_time_from_HOSP_GRZ = []
            wait_time_from_HOSP_High = []
            wait_time_from_GPR_High = []
            wait_time_from_GPR_Low = []
            wait_time_from_GPR_High_v2 = []
            wait_time_from_GPR_Low_v2 = []
            perc_with_HOSP_adm_list = []
            nr_pat_repl_list = []
            costs_list = []
            bez_gr_list_Total = []
            abs_aanw_list = []
            bez_gr_Low_list = []
            abs_aanw_Low_list = []
            bez_gr_High_list = []
            abs_aanw_High_list = []    
            bez_gr_TRW_list = []
            abs_aanw_TRW_list = []
            len_w3_list = []
            len_w2_EMD_list = []
            len_w2_GPR_High_list = []
            len_w1_list = []
            serv_level = []
            wait_time_to_TRW = []
            los_Low_list =[]
            tot_cost_trw_List = []
            bez_gr_list_High = []
            cur_nr_ELV_Tot = 0
            
            n_beds_ELV_High_list = []
            n_beds_ELV_Low_list = []
            n_beds_GRZ_list = []
            n_beds_High_Complex_list= []
            n_beds_ELV_Low_list= []
            n_beds_shared_High_list= []
            n_beds_ELV_total_list=  []
            
            len_wtot_mean = 0
            bez_gr_EMDR_mean = 0
            loc_ELV_High = []
            loc_ELV_Low = []
            cur_nr_TRW = 0
            trans_list = []
            
            
            n_loc = int(input.loc[loop_nr,'n_loc'])
            
            def sum_lists(list_a,list_b):
                c= []
                for i in range(len(list_a)):
                    c.append( list_a[i] + list_b[i] )
                return c 
            def insert_sort(list, n): 
                bisect.insort(list, n)  
                return list
            def exp(x):
                return np.random.exponential(scale=1/x, size=None)
            
            def select_list(input_list):
                
                i = ['HOSP_adm', 'ELV_High','ELV_Low', 'TRW']
                new_list = []
                for index in i:
                    if index in input_list:
                        new_list.append(index)
                    
                return new_list
            def count_patients(loc):
                parts = loc.split("_")
                cur_nr_loc = 0
                location = ''
                if len(parts) ==2:
                    location = loc + '_' + str(extract_number(target_client))
                    n_aanw_excl_end_time = len([k for (k,v) in client_dict.items() if location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])<= v['journey'].index(location)+ 1])
                    n_aanw_incl_end_time = len([k for (k,v) in client_dict.items() if location in v['journey'] and k not in output_dict.keys() and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    n_aanw_al_in_output = len([k for (k,v) in output_dict.items() if location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    cur_nr_loc = n_aanw_excl_end_time + n_aanw_incl_end_time + n_aanw_al_in_output
                
            
                elif len(parts) == 3:
                    location = loc
                    n_aanw_excl_end_time = len([k for (k,v) in client_dict.items() if location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])<= v['journey'].index(location)+ 1])
                    n_aanw_incl_end_time = len([k for (k,v) in client_dict.items() if location in v['journey'] and k not in output_dict.keys() and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    n_aanw_al_in_output = len([k for (k,v) in output_dict.items() if location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    cur_nr_loc = n_aanw_excl_end_time + n_aanw_incl_end_time + n_aanw_al_in_output
            
                
                return cur_nr_loc
            def count_place_reserved(loc):
                parts = loc.split("_")
                location = ''
                if len(parts) ==2:
                    location = loc + '_' + str(extract_number(target_client))
                elif len(parts) == 3:
                    location = loc
                place_reserved = len([k for (k,v) in client_dict.items() if v['journey'][-1] == location and v['j_times'][v['journey'].index(location)] > current_time])   
                #len([k for (k, v) in client_dict.items() if location in v['journey']  and v['j_times'][v['journey'].index(location)] > current_time]) 
                return place_reserved
            def move_to_TRW_High(target_client, time_until_placement):
                
                client_dict[target_client]['current_loc'] = 'TRW_' +str(extract_number(target_client))
                client_dict[target_client]['journey'].append('TRW_'+str(extract_number(target_client)))
                client_dict[target_client]['j_times'].append(current_time + time_until_placement)
                
                if print_modus:
                    print(target_client, 'goes to TRW')
                    print(client_dict[target_client])
                    # discharge ook erin zetten
                High_list = ['HOS_High','GPR_High','EMD']
                GRZ_list = ['HOS_GRZ']
                if any(item in client_dict[target_client]['journey'] for item in High_list):
                    discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_High,out_p_Dead_High,out_p_WMO_High,out_p_WLZ_High,out_p_GRZV_High, out_p_Pall_High])[0]
                    client_dict[target_client]['TRW_discharge_dest'] = discharge_dest
            
                    if discharge_dest == 'Home':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_High)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'Dead':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_High)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'WMO':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_High)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement+ max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'WLZ':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_High)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'GRZV':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_High)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'Pall':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_High)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False       
            
            
                if any(item in client_dict[target_client]['journey'] for item in GRZ_list):
                
                    discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_GRZ,out_p_Dead_GRZ,out_p_WMO_GRZ,out_p_WLZ_GRZ,out_p_GRZV_GRZ, out_p_Pall_GRZ])[0]
                    client_dict[target_client]['TRW_discharge_dest'] = discharge_dest
            
                    if discharge_dest == 'Home':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_GRZ)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'Dead':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_GRZ)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'WMO':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_GRZ)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement+ max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'WLZ':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_GRZ)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'GRZV':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_GRZ)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False
                    elif discharge_dest == 'Pall':
                        event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_GRZ)
                        if event_dict['TRW_discharge_' + target_client] - current_time - time_until_placement > max_days_TRW: # moet nog verplaatsen naar ELV
                            client_dict[target_client]['to_ELV_High'] = True
                            client_dict[target_client]['ELV_High_dist_time'] = event_dict['TRW_discharge_' + target_client]
                            event_dict['TRW_discharge_' + target_client] = current_time + time_until_placement + max_days_TRW
                        else: 
                            client_dict[target_client]['to_ELV_High'] = False           
            
            
            def move_to_ELV_High_from_TRW(target_client, time_until_placement):    
                
                client_dict[target_client]['current_loc'] = 'ELV_High_'+str(extract_number(target_client))
                client_dict[target_client]['journey'].append('ELV_High_'+str(extract_number(target_client)))
                client_dict[target_client]['j_times'].append(current_time + time_until_placement)
            
                if print_modus:
                    print(target_client, 'goes to ELV High at', current_time + time_until_placement)
                    print(client_dict[target_client])
            
                # discharge ook erin zetten
            
                discharge_dest = client_dict[target_client]['TRW_discharge_dest']
                client_dict[target_client]['discharge_dest'] = discharge_dest
                event_dict['discharge_' + target_client] = client_dict[target_client]['ELV_High_dist_time'] + time_until_placement
                event_dict['check_TRW_beds'] = current_time + time_until_placement + 0.000000000001
            def move_to_ELV_High(target_client, time_until_placement):
                
                client_dict[target_client]['current_loc'] = 'ELV_High_' + str(extract_number(target_client))
                client_dict[target_client]['journey'].append('ELV_High_' + str(extract_number(target_client)))
                client_dict[target_client]['j_times'].append(current_time + time_until_placement)
                
                if print_modus:
                    print(target_client, 'gaat naar ELV_High om', current_time + time_until_placement)
                    print(client_dict[target_client])
                
                # discharge ook erin zetten
                High_list = ['HOS_High','GPR_High','EMD']
                GRZ_list = ['HOS_GRZ']
                if any(item in client_dict[target_client]['journey'] for item in High_list):
                    discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_High,out_p_Dead_High,out_p_WMO_High,out_p_WLZ_High,out_p_GRZV_High, out_p_Pall_High])[0]
                    client_dict[target_client]['discharge_dest'] = discharge_dest
                
                    if discharge_dest == 'Home':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_High)
                    elif discharge_dest == 'Dead':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_High)    
                    elif discharge_dest == 'WMO':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_High)
                    elif discharge_dest == 'WLZ':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_High)
                    elif discharge_dest == 'GRZV':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_High)
                    elif discharge_dest == 'Pall':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_High)
                
                elif any(item in client_dict[target_client]['journey'] for item in GRZ_list):
                    discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_GRZ,out_p_Dead_GRZ,out_p_WMO_GRZ,out_p_WLZ_GRZ,out_p_GRZV_GRZ, out_p_Pall_GRZ])[0]
                    client_dict[target_client]['discharge_dest'] = discharge_dest
            
                    if discharge_dest == 'Home':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_GRZ)
                    elif discharge_dest == 'Dead':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_GRZ)    
                    elif discharge_dest == 'WMO':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_GRZ)
                    elif discharge_dest == 'WLZ':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_GRZ)
                    elif discharge_dest == 'GRZV':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_GRZ)
                    elif discharge_dest == 'Pall':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_GRZ)
            
            def move_to_ELV_Emergency(target_client, time_until_placement):
                
                client_dict[target_client]['current_loc'] = 'ELV_EMDR_' + str(extract_number(target_client))
                client_dict[target_client]['journey'].append('ELV_EMDR_' + str(extract_number(target_client)))
                client_dict[target_client]['j_times'].append(current_time + time_until_placement)
                
                if print_modus:
                    print(target_client, 'gaat naar ELV_EMDR om', current_time + time_until_placement)
                    print(client_dict[target_client])
                
                # discharge ook erin zetten
                
                discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_High,out_p_Dead_High,out_p_WMO_High,out_p_WLZ_High,out_p_GRZV_High, out_p_Pall_High])[0]
                client_dict[target_client]['discharge_dest'] = discharge_dest
                
                if discharge_dest == 'Home':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_High)
                elif discharge_dest == 'Dead':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_High)    
                elif discharge_dest == 'WMO':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_High)
                elif discharge_dest == 'WLZ':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_High)
                elif discharge_dest == 'GRZV':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_High)
                elif discharge_dest == 'Pall':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_High)
            def move_to_ELV_partial_bed(target_client, time_until_placement):
                
            
                
                client_dict[target_client]['current_loc'] = 'ELV_part_' + str(extract_number(target_client))
                client_dict[target_client]['journey'].append('ELV_part_' + str(extract_number(target_client)))
                client_dict[target_client]['j_times'].append(current_time + time_until_placement)
                
                if print_modus:
                    print(target_client, 'gaat naar ELV_Part om', current_time + time_until_placement)
                    print(client_dict[target_client])
                
                # discharge ook erin zetten
                High_list = ['HOS_High','GPR_High','EMD']
                Low_list = ['GPR_Low']
                GRZ_list = ['HOS_GRZ']
                
                if any(item in client_dict[target_client]['journey'] for item in High_list):
                
                    discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_High,out_p_Dead_High,out_p_WMO_High,out_p_WLZ_High,out_p_GRZV_High, out_p_Pall_High])[0]
                    client_dict[target_client]['discharge_dest'] = discharge_dest
            
                    if discharge_dest == 'Home':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_High)
                    elif discharge_dest == 'Dead':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_High)    
                    elif discharge_dest == 'WMO':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_High)
                    elif discharge_dest == 'WLZ':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_High)
                    elif discharge_dest == 'GRZV':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_High)
                    elif discharge_dest == 'Pall':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_High)
                        
                elif any(item in client_dict[target_client]['journey'] for item in Low_list):
                    
                    discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_Low,out_p_Dead_Low,out_p_WMO_Low,out_p_WLZ_Low,out_p_GRZV_Low, out_p_Pall_Low])[0]
                    client_dict[target_client]['discharge_dest'] = discharge_dest
            
                    if discharge_dest == 'Home':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_Low)
                    elif discharge_dest == 'Dead':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_Low)    
                    elif discharge_dest == 'WMO':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_Low)
                    elif discharge_dest == 'WLZ':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_Low)
                    elif discharge_dest == 'GRZV':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_Low)
                    elif discharge_dest == 'Pall':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_Low)
                elif any(item in client_dict[target_client]['journey'] for item in GRZ_list):
                    discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_GRZ,out_p_Dead_GRZ,out_p_WMO_GRZ,out_p_WLZ_GRZ,out_p_GRZV_GRZ, out_p_Pall_GRZ])[0]
                    client_dict[target_client]['discharge_dest'] = discharge_dest
            
                    if discharge_dest == 'Home':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_GRZ)
                    elif discharge_dest == 'Dead':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_GRZ)    
                    elif discharge_dest == 'WMO':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_GRZ)
                    elif discharge_dest == 'WLZ':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_GRZ)
                    elif discharge_dest == 'GRZV':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_GRZ)
                    elif discharge_dest == 'Pall':
                        event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_GRZ)
            
            def move_to_ELV_Total(target_client,time_until_placement):
                client_dict[target_client]['current_loc'] = 'ELV_TOT_' + str(extract_number(target_client))
                client_dict[target_client]['journey'].append('ELV_TOT_' + str(extract_number(target_client)))
                client_dict[target_client]['j_times'].append(current_time + time_until_placement)
                
                if print_modus:
                    print(target_client, 'gaat naar ELV_TOT om', current_time + time_until_placement)
                    print(client_dict[target_client])
                
                
                out_p_Home_TOT = (out_p_Home_High+out_p_Home_GRZ+out_p_Home_Low)/3
                out_p_Dead_TOT = (out_p_Dead_High+out_p_Dead_GRZ+out_p_Dead_Low)/3
                out_p_WMO_TOT = (out_p_WMO_High+out_p_WMO_GRZ+out_p_WMO_Low)/3
                out_p_WLZ_TOT = (out_p_WLZ_High+out_p_WLZ_GRZ+out_p_WLZ_Low)/3
                out_p_GRZV_TOT = (out_p_GRZV_High+out_p_GRZV_GRZ+out_p_GRZV_Low)/3
                out_p_Pall_TOT = (out_p_Pall_High+out_p_Pall_GRZ+out_p_Pall_Low)/3
            
                serv_Home_TOT = (serv_Home_High+serv_Home_GRZ+serv_Home_Low)/3
                serv_Dead_TOT = (serv_Home_High+serv_Home_GRZ+serv_Home_Low)/3
                serv_WMO_TOT = (serv_Home_High+serv_Home_GRZ+serv_Home_Low)/3
                serv_WLZ_TOT = (serv_Home_High+serv_Home_GRZ+serv_Home_Low)/3
                serv_GRZV_TOT = (serv_Home_High+serv_Home_GRZ+serv_Home_Low)/3
                serv_Pall_TOT = (serv_Home_High+serv_Home_GRZ+serv_Home_Low)/3
                
                
                discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_TOT,out_p_Dead_TOT,out_p_WMO_TOT,out_p_WLZ_TOT,out_p_GRZV_TOT, out_p_Pall_TOT])[0]
                client_dict[target_client]['discharge_dest'] = discharge_dest
            
                if discharge_dest == 'Home':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_TOT)
                elif discharge_dest == 'Dead':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_TOT)    
                elif discharge_dest == 'WMO':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_TOT)
                elif discharge_dest == 'WLZ':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_TOT)
                elif discharge_dest == 'GRZV':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_TOT)
                elif discharge_dest == 'Pall':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_TOT)
                    
            
            def move_to_ELV_Low(target_client, time_until_placement):
                
                client_dict[target_client]['current_loc'] = 'ELV_Low_' + str(extract_number(target_client))
                client_dict[target_client]['journey'].append('ELV_Low_'+ str(extract_number(target_client)))
                client_dict[target_client]['j_times'].append(current_time + time_until_placement)
                
                if print_modus:
                    print(target_client, 'gaat naar ELV_Low om', current_time + time_until_placement)
                    print(client_dict[target_client])
                
                # discharge ook erin zetten
                
                discharge_dest = rd.choices(['Home', 'Dead', 'WMO', 'WLZ', 'GRZV', 'Pall'], [out_p_Home_Low,out_p_Dead_Low,out_p_WMO_Low,out_p_WLZ_Low,out_p_GRZV_Low, out_p_Pall_Low])[0]
                client_dict[target_client]['discharge_dest'] = discharge_dest
                
                if discharge_dest == 'Home':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Home_Low)
                elif discharge_dest == 'Dead':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Dead_Low)    
                elif discharge_dest == 'WMO':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WMO_Low)
                elif discharge_dest == 'WLZ':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_WLZ_Low)
                elif discharge_dest == 'GRZV':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_GRZV_Low)
                elif discharge_dest == 'Pall':
                    event_dict['discharge_' + target_client] = current_time + time_until_placement + exp(serv_Pall_Low)
            
            
            def make_conf_output(list_input):
                
                mean = round(mean_confidence_interval(list_input)[0],2)
                lower_bound = round(mean_confidence_interval(list_input)[1],2)
                upper_bound = round(mean_confidence_interval(list_input)[2],2)
                
                return str(mean) + ' (' + str(lower_bound) +',' + str(upper_bound) + ')'
            
            def move_to_HOSP(target_client):
                
                client_dict[target_client]['current_loc'] = 'HOSP_adm'
                client_dict[target_client]['journey'].append('HOSP_adm')
                client_dict[target_client]['j_times'].append(current_time)
                
                if print_modus:
                    print(target_client, 'gaat naar HOSP adm')
                    print(client_dict[target_client])
                
                # discharge ook erin zetten
            
                event_dict['HOSP_discharge_' + target_client] = current_time + exp(30)#exp(serv_HOS)
                
                # van wachtlijst afhalen
                
                if (target_client in w3_dict.keys() and target_client in output_dict.keys()) or target_client in w3_dict.keys():
                     remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                
            def mean_confidence_interval(data, confidence=0.95):
                a = 1.0 * np.array(data)
                n = len(a)
                m, se = np.mean(a), scipy.stats.sem(a)
                h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
                return m, m-h, m+h
            
            def Check_space_partial_beds(department):
                High_list = ['HOS_High', 'GPR_High', 'EMD']
                GRZ_list = ['HOS_GRZ']
                tot_patients = 0
                location = 'ELV_High_' +str(extract_number(target_client))
                if any(item in department for item in High_list):
                    n_aanw_excl_end_time = len([k for (k,v) in client_dict.items() if v['journey'][0] in High_list and location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])<= v['journey'].index(location)+ 1])
                    n_aanw_incl_end_time = len([k for (k,v) in client_dict.items() if v['journey'][0] in High_list and location in v['journey'] and k not in output_dict.keys() and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    n_aanw_al_in_output = len([k for (k,v) in output_dict.items() if v['journey'][0] in High_list and location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    n_plek_gedibst = len([k for (k,v) in client_dict.items() if v['journey'][0] in High_list and v['journey'][-1] == location and v['j_times'][v['journey'].index(location)] > current_time])   
                    cur_nr_loc = n_aanw_excl_end_time + n_aanw_incl_end_time + n_aanw_al_in_output +n_plek_gedibst
                    # if cur_nr_loc >=105:
                    #     cur_nr_loc = 105
                elif any(item in department for item in GRZ_list):
                  
                    n_aanw_excl_end_time = len([k for (k,v) in client_dict.items() if v['journey'][0] in GRZ_list and location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])<= v['journey'].index(location)+ 1])
                    n_aanw_incl_end_time = len([k for (k,v) in client_dict.items() if v['journey'][0] in GRZ_list and location in v['journey'] and k not in output_dict.keys() and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    n_aanw_al_in_output = len([k for (k,v) in output_dict.items() if v['journey'][0] in GRZ_list and location in v['journey'] and v['j_times'][v['journey'].index(location)] <= current_time and len(v['j_times'])> v['journey'].index(location)+ 1 and current_time <= v['j_times'][v['journey'].index(location)+1]])
                    n_plek_gedibst = len([k for (k,v) in client_dict.items() if v['journey'][0] in GRZ_list and v['journey'][-1] == location and v['j_times'][v['journey'].index(location)] > current_time])   
                    cur_nr_loc = n_aanw_excl_end_time + n_aanw_incl_end_time + n_aanw_al_in_output +n_plek_gedibst
                    # if cur_nr_loc >=20:
                    #     cur_nr_loc = 20
                        
                return cur_nr_loc
            
            def mean(list):
                cleaned_list = [x for x in list if not np.isnan(x)]  # Remove NaN values
                return np.mean(cleaned_list)
            
            def check_balanced_system(n_loc):
                print('-----------------------Project---------------------')
                #print(Project)
                print('---------------------------------------------------')
                print('-------------------Check balanced system----------------')
                for i in range(n_loc):
                    print("For location, ", i)
                    arrival_High = (arr_HOS_High +arr_GPR_High + arr_EMD +arr_HOS_GRZ)/n_loc
                    service_High = serv_Home_High * out_p_Home_High +serv_Dead_High * out_p_Dead_High + out_p_GRZV_High * serv_GRZV_High + out_p_WLZ_High * serv_WLZ_High + out_p_Pall_High * serv_Pall_High + out_p_WMO_High * serv_WMO_High
                    service_GRZ = serv_Home_GRZ * out_p_Home_GRZ +serv_Dead_GRZ * out_p_Dead_GRZ + out_p_GRZV_GRZ * serv_GRZV_GRZ + out_p_WLZ_GRZ * serv_WLZ_GRZ + out_p_Pall_GRZ * serv_Pall_GRZ + out_p_WMO_GRZ * serv_WMO_GRZ
                    service_ELV_high = (service_High+service_GRZ)/2
                    arrival_Low = arr_GPR_Low/n_loc
                    service_Low = serv_Home_Low * out_p_Home_Low +serv_Dead_Low * out_p_Dead_Low + out_p_GRZV_Low * serv_GRZV_Low + out_p_WLZ_Low * serv_WLZ_Low + out_p_Pall_Low * serv_Pall_Low + out_p_WMO_Low * serv_WMO_Low
                    
            
            
            
                    if Scen_shared_beds_Full:
                        n_servers_Low = n_beds_ELV_Low_list[i]
                        print("Full bed share")
                        n_servers_High = n_beds_ELV_High_list[i]
            
                        if (arrival_High/(service_ELV_high*n_servers_High)) < 1:
                            print("High System is stable rho_High equals: ", (arrival_High/(service_ELV_high*n_servers_High)))
                        else:
                            print("High System is not stable, rho_High equals: ", (arrival_High/(service_ELV_high*n_servers_High)))
            
                        if (arrival_Low/(service_Low*n_servers_Low)) < 1:
                            print("Low System is stable rho_Low equals: ", (arrival_Low/(service_Low*n_servers_Low)))
                        else:
                            print("System is not stable, rho_Low equals: ", (arrival_Low/(service_Low*n_servers_Low)))
            
                    elif Scen_part_bed_Share:
                        
                        print("Partial bed share")
                        n_servers_Low = n_beds_ELV_Low_list[i]
                        n_servers_High = n_beds_High_Complex_list[i] + n_beds_GRZ_list[i] + n_beds_shared_High_list[i]
                        arrival_High_Complex = (arr_HOS_High + arr_EMD + arr_GPR_High)/n_loc
                        arrival_GRZ = arr_HOS_GRZ/n_loc
                        if (arrival_High / (service_High * n_servers_High)) < 1:
                            print("High System is stable rho_High equals: ", (arrival_High / (service_ELV_high * n_servers_High)))
                        else:
                            print("High System is not stable, rho_High equals: ", (arrival_High / (service_ELV_high * n_servers_High)))
            
                        if (arrival_High_Complex / (service_High * (n_beds_High_Complex_list[i] + n_beds_shared_High_list[i]))) < 1:
                            print("High complex System is stable rho_High equals: ", (arrival_High_Complex / (service_High * (n_beds_High_Complex_list[i] + n_beds_shared_High_list[i]))))
                        else:
                            print("High complex System is not stable, rho_High equals: ", (arrival_High_Complex / (service_High * (n_beds_High_Complex_list[i] + n_beds_shared_High_list[i]))))
            
                        if (arrival_GRZ / (service_High * (n_beds_GRZ_list[i] + n_beds_shared_High_list[i]))) < 1:
                            print("GRZ_High System is stable rho_High equals: ", (arrival_GRZ / (service_GRZ * (n_beds_GRZ_list[i] + n_beds_shared_High_list[i]))))
                        else:
                            print("GRZ_High System is not stable, rho_High equals: ", (arrival_GRZ / (service_GRZ * (n_beds_GRZ_list[i] + n_beds_shared_High_list[i]))))
            
                        if (arrival_Low / (service_Low * n_servers_Low)) < 1:
                            print("System is stable rho_Low equals: ", (arrival_Low / (service_Low * n_servers_Low)))
                        else:
                            print("Low System is not stable, rho_Low equals: ", (arrival_Low / (service_Low * n_servers_Low)))
            
            
                    elif Scen_NO_Sharing:
                        n_servers_Low = n_beds_ELV_Low_list[i]
                        print("No bed share")
                        n_servers_High =  n_beds_High_Complex_list[i]+n_beds_GRZ_list[i]
                        arrival_High_Complex = (arr_HOS_High+arr_EMD+arr_GPR_High)/n_loc
                        arrival_GRZ = (arr_HOS_GRZ)/n_loc
                        if (arrival_High/(service_High*n_servers_High)) < 1:
                            print("High System is stable rho_High equals: ", (arrival_High/(service_ELV_high*n_servers_High)))
                        else:
                            print("High System is not stable, rho_High equals: ", (arrival_High/(service_ELV_high*n_servers_High)))
            
                        if (arrival_High_Complex/(service_High*n_beds_High_Complex_list[i])) < 1:
                            print("High complex System is stable rho_High equals: ", (arrival_High_Complex/(service_High*n_beds_High_Complex_list[i])))
                        else:
                            print("High complex System is not stable, rho_High equals: ", (arrival_High_Complex/(service_High*n_beds_High_Complex_list[i])))
            
                        if (arrival_GRZ/(service_High*n_beds_GRZ_list[i])) < 1:
                            print("GRZ System is stable rho_High equals: ", (arrival_GRZ/(service_GRZ*n_beds_GRZ_list[i])))
                        else:
                            print("GRZ System is not stable, rho_High equals: ", (arrival_GRZ/(service_GRZ*n_beds_GRZ_list[i]))) 
            
                        if (arrival_Low/(service_Low*n_servers_Low)) < 1:
                            print("Low System is stable rho_Low equals: ", (arrival_Low/(service_Low*n_servers_Low)))
                        else:
                            print("Low System is not stable, rho_Low equals: ", (arrival_Low/(service_Low*n_servers_Low)))
                        
                    elif Scen_Total_Sharing:
                        n_servers = n_beds_ELV_total_list[i]
                        print("Total bed Share")
                        arrival_total = (arr_HOS_High+arr_EMD+arr_GPR_High +arr_HOS_GRZ +arr_GPR_Low)/n_loc
                        service_total = (service_ELV_high+service_Low)/2
                        if (arrival_total/(n_servers*service_total)) < 1:
                            print(" System is stable rho_TOT equals: ", (arrival_total/(service_total*n_servers)))
                        else:
                            print(" System is not stable, rho_TOT equals: ", (arrival_total/(service_total*n_servers)))
                print('-------------------------------------------------------')
            
            def extract_number(target_client):
                if type(target_client) == list:
                    index = find_index(target_client)
                    ELV_PREV = target_client[index]
                    # Split the string using underscores as separators
                    parts = ELV_PREV.split('_')
            
                    # Check if there are at least three parts (c, 001, 3)
                    if len(parts) >= 3:
                        # Try to convert the third part to an integer
                        try:
                            number_after_second_underscore = int(parts[2])
                            return number_after_second_underscore
                        except ValueError:
                            # Handle the case where conversion to int fails
                            print("Error: Unable to convert the third part to an integer.")
                    #else:
                        #print("Error: The input string does not have enough parts.")
                else:    
                
                    # Split the string using underscores as separators
                    parts = target_client.split('_')
            
                    # Check if there are at least three parts (c, 001, 3)
                    if len(parts) >= 3:
                        # Try to convert the third part to an integer
                        try:
                            number_after_second_underscore = int(parts[2])
                            return number_after_second_underscore
                        except ValueError:
                            # Handle the case where conversion to int fails
                            print("Error: Unable to convert the third part to an integer.")
                    #else:
                        #print("Error: The input string does not have enough parts.")
            
            def find_first_client(wait_list,number,target_client):
                count =[]
                for i in wait_list:
                    if  extract_number(i) == number:
                        count.append(i)
                return count[0]
            
            
            
            def count_wait_list_loc(wait_list,target_client):
                count =0
                for i in wait_list:
                    if  extract_number(i) == extract_number(target_client):
                        count +=1
                return count
            
            def find_index(lst):
                prefix = 'ELV_'
                # Iterate over the list and check if the element contains the prefix
                for i, item in enumerate(lst):
                    if prefix in item:
                        return i  # Return the index if found
                # If the prefix is not found in any element, return None
                return None
            
            def remove_and_sort(numbers, Current_location):
                 # Find the index of nearest_location in the original list
                index = numbers.index(Current_location)
                # Remove nearest_location from the list if it exists
                if Current_location in numbers:
                    numbers.remove(Current_location)
                
               
                
                # Rotate the list so that it starts from the value after nearest_location
                sorted_numbers = numbers[index+1:] + numbers[:index+1]
                return sorted_numbers
            
            def Check_beds_free_other_location(Current_location, n_loc, target_client,TRW):
                if n_loc ==0 or n_loc ==1:
                    #print("only 1 location")
                    return False,'none'
                else:
                    Locs = [i for i in range(n_loc)]
                    Locations = remove_and_sort(Locs, Current_location)
                    for loc in Locations:
                        if any(item in client_dict[target_client]['journey'] for item in ['GPR_High', 'EMD', 'HOS_High','HOS_GRZ']):
                            if Scen_shared_beds_Full:
                                if TRW == True:
                                    if (count_patients('TRW') + count_place_reserved('TRW')) < n_beds_TRW[loc]:
                #                         print("Patient transfer to location, ", loc)
                    #                    change_target_client_location(target_client,loc)
                                        return True,loc
                                else: 
                                    if any(item in client_dict[target_client]['journey'] for item in ['GPR_High', 'EMD', 'HOS_High','HOS_GRZ']):
                                        if (count_patients('ELV_High') + count_place_reserved('ELV_High')) < n_beds_ELV_High_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                    change_target_client_location(target_client,loc)
                                            return True,loc
                                    
                            #return False
                            elif Scen_NO_Sharing:
                                if TRW == True:
                                    if (count_patients('TRW') + count_place_reserved('TRW')) < n_beds_TRW[loc]:
                #                         print("Patient transfer to location, ", loc)
                    #                    change_target_client_location(target_client,loc)
                                        return True,loc
                                else:
                                    if 'GPR_High' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('GPR_High')< n_beds_High_Complex_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                    elif 'EMD' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('EMD')<n_beds_High_Complex_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                    if 'HOS_High' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_High')< n_beds_High_Complex_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                    if 'HOS_GRZ' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_GRZ')< n_beds_GRZ_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                    
                            #return False
                            elif Scen_part_bed_Share:
                                if TRW == True:
                                    if (count_patients('TRW') + count_place_reserved('TRW')) < n_beds_TRW[loc]:
                #                         print("Patient transfer to location, ", loc)
                    #                    change_target_client_location(target_client,loc)
                                        return True,loc
                                else:
                                    if 'GPR_High' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('GPR_High')< n_beds_High_Complex_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                        elif count_patients('ELV_part') +count_place_reserved('ELV_part') < n_beds_shared_High_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                    elif 'EMD' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('EMD')< n_beds_High_Complex_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                        elif count_patients('ELV_part') +count_place_reserved('ELV_part') < n_beds_shared_High_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                    if 'HOS_High' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_High')< n_beds_High_Complex_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                        elif count_patients('ELV_part') +count_place_reserved('ELV_part') < n_beds_shared_High_list[loc]:
                    #                         print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                    if 'HOS_GRZ' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_GRZ')< n_beds_GRZ_list[loc]:
                                            print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                        elif count_patients('ELV_part') +count_place_reserved('ELV_part') < n_beds_shared_High_list[loc]:
                                            print("Patient transfer to location, ", loc)
                        #                     change_target_client_location(target_client,loc)
                                            return True,loc
                                   
                            elif Scen_Total_Sharing:
                                if TRW == True:
                                    if (count_patients('TRW') + count_place_reserved('TRW')) < n_beds_TRW[loc]:
                #                         print("Patient transfer to location, ", loc)
                    #                    change_target_client_location(target_client,loc)
                                        return True,loc
                                else:
                                    if count_patients('ELV_TOT')+count_place_reserved('ELV_TOT')< n_beds_ELV_total_list[loc]:
                                        return True,loc
                                        
                        elif any(item in client_dict[target_client]['journey'] for item in ['GPR_Low']):
                            if Scen_NO_Sharing or Scen_part_bed_Share or Scen_shared_beds_Full:
                                if (count_patients('ELV_Low') + count_place_reserved('ELV_Low')) < n_beds_ELV_Low_list[loc]:
                        #                         print("Patient transfer to location, ", loc)
                            #                     change_target_client_location(target_client,loc)
                                    return True,loc
                            elif Scen_Total_Sharing:
                                if (count_patients('ELV_Low') + count_place_reserved('ELV_Low')) < n_beds_ELV_Low_list[loc]:
                        #                         print("Patient transfer to location, ", loc)
                            #                     change_target_client_location(target_client,loc)
                                    return True,loc
                            
                return False,'none'
                        
            def change_target_client_location(target_client,nearest_location,Event):
                
                # Split the target_client string by underscores
                parts = target_client.split('_')
                
                # Check if there are at least three parts (e.g., c, 001, 1)
                if len(parts) >= 3:
                    # Update the value after the second underscore with nearest_location
                    parts[2] = nearest_location
                    
                    # Join the parts back into a single string using underscores
                    updated_target_client = '_'.join(map(str, parts))
            #         print(target_client,updated_target_client)
                    if Event == True:
                        client_dict[target_client]['journey'].append("Transfer")
                        client_dict[target_client]['j_times'].append(current_time)
                    return updated_target_client
                else:
                    print("Error: The input string does not have enough parts.")
            
            def change_string_to_list(b_list):
                # Replace the delimiter '],[' with '],[', and enclose the string with square brackets to make it valid JSON
                json_string = '[' + b_list.replace('],[', '],[') + ']'
                
                # Use json.loads() to parse the JSON string into a Python list
                result_list = json.loads(json_string)
                
                return result_list[0]
            def add_to_waiting_dict(wait_list_dict,target_client,current_time):
                import random
                if target_client not in output_dict.items():
                    
                    #print('Add ',target_client)
                    Strength = 0
                    Alternative_location = False
                    Pos_loc = 0
                    if n_loc ==1:
                        Strength = -1
                    else:
                        if Preference == 'FCFS':
                            Strength = -1 
                            Alternative_location = True
                        elif Preference == 'NO':
                            Strength = 10000000000000000000
                            Alternative_location = False
                        elif Preference == 'Pref':
                            Strength = random.choice([10,30,50,70,90,100000000000])
                            Alternative_location = False
                
                    
                        
                    wait_dict_temp = {target_client: {
                    'Preferred location' :extract_number(target_client),
                    'Arrival_time':current_time,
                    'Waiting time':0,
                    "Utility":5,
                    'Alternative location':Alternative_location,
                    'Strength': Strength,
                    'Extra waiting time':0,
                    'Skipped':False,
                    'Timestamp_skipped': 0,
                    'Times_skipped':0,
                    'Possible_locations': Show_possible_locations(target_client),
                    }}
                    wait_list_dict.update(wait_dict_temp)
                    wait_list_dict1 = dict(sorted(wait_list_dict.items(),key=lambda x: x[1]['Arrival_time']))
                    wait_list_dict = wait_list_dict1
                    update_wait_list_dict(wait_list_dict,current_time)
            
            def update_wait_list_dict(wait_list_dict,current_time):
                remove_wait_list_items(wait_list_dict, output_dict)
                for key in list(wait_list_dict.keys()):
                    wait_list_dict[key]['Waiting time'] = current_time-wait_list_dict[key]['Arrival_time']
                    wait_list_dict[key]['Utility'] = wait_list_dict[key]['Waiting time']
                    if wait_list_dict[key]['Utility'] > wait_list_dict[key]['Strength']:
                        wait_list_dict[key]['Alternative location'] = True
                    else:
                        wait_list_dict[key]['Alternative location'] = False
                        
                    if wait_list_dict[key]['Skipped'] and Preference != 'FCFS':
                        wait_list_dict[key]['Extra waiting time'] =  current_time - wait_list_dict[key]['Timestamp_skipped']
            
            def remove_from_wait_list(wait_list_dict,target_client,current_time,Fairness_list):
                client_rem = target_client
                Fairness_list.append(wait_list_dict[target_client]['Extra waiting time'])
                list(wait_list_dict.keys()).index(client_rem)
                if list(wait_list_dict.keys()).index(client_rem) != 0:
                    for key in range(list(wait_list_dict.keys()).index(client_rem)):
                        if wait_list_dict[list(wait_list_dict.keys())[key]]['Skipped'] == False:
                            wait_list_dict[list(wait_list_dict.keys())[key]]['Skipped'] = True
                            wait_list_dict[list(wait_list_dict.keys())[key]]['Timestamp_skipped'] = current_time
                            wait_list_dict[list(wait_list_dict.keys())[key]]['Times_skipped'] +=1
                        else:
                            wait_list_dict[list(wait_list_dict.keys())[key]]['Times_skipped'] +=1
                    del wait_list_dict[client_rem]
                else:
                    del wait_list_dict[client_rem]
                update_wait_list_dict(wait_list_dict,current_time)
        
            def remove_wait_list_items(wait_list_dict, output_dict):
                for key in list(wait_list_dict.keys()):
                    if key in output_dict:
                        del wait_list_dict[key]
            
            def check_first_pref_client(wait_list_dict,location):
                update_wait_list_dict(wait_list_dict,current_time)
                for key in list(wait_list_dict.keys()):
                    if wait_list_dict[key]['Preferred location'] == location:
                        return key
                    elif (location in wait_list_dict[key]['Possible_locations'] and wait_list_dict[key]['Alternative location']):
                        change_target_client_location(key,location,True)
                        #trans_list.append(key)
                        return key
            def check_zero_indexes(lst):
                zero_indexes = []
                for i, num in enumerate(lst):
                    if num == 0:
                        zero_indexes.append(i)
                return [i for i in range(len(lst)) if i not in zero_indexes]
            
            def non_zero_indexes(list1, list2):
                """
                Returns a list containing indexes where both lists have non-zero values.
            
                Args:
                list1 (list): The first list to be checked.
                list2 (list): The second list to be checked.
            
                Returns:
                list: A list containing indexes where both lists have non-zero values.
                """
                non_zero_indices = []
                for i in range(min(len(list1), len(list2))):
                    if list1[i] != 0 or list2[i] != 0:
                        non_zero_indices.append(i)
                return non_zero_indices
            
            def Show_possible_locations(target_client):
                client_pref = extract_number(target_client)
                if any(item in client_dict[target_client]['journey'] for item in ['GPR_High', 'EMD', 'HOS_High', 'HOS_GRZ']):
                    if Scen_shared_beds_Full:
                    
                        loc = (check_zero_indexes(n_beds_ELV_High_list))
                        return loc
                    
                    elif Scen_NO_Sharing:
                        if any(item in client_dict[target_client]['journey'] for item in ['GPR_High', 'EMD', 'HOS_High']):
                            loc = check_zero_indexes(n_beds_ELV_High_list)
                            return loc
                        elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                            loc = check_zero_indexes(n_beds_GRZ_list)
                            return loc
                        
                    elif Scen_part_bed_Share:
                        if any(item in client_dict[target_client]['journey'] for item in ['GPR_High', 'EMD', 'HOS_High']):
                            loc = non_zero_indexes(n_beds_ELV_High_list,n_beds_shared_High_list)
                            return loc
                        elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                            loc = non_zero_indexes(n_beds_GRZ_list,n_beds_shared_High_list)
                            return loc
                        
                    elif Scen_Total_Sharing:
                        loc = check_zero_indexes(n_beds_ELV_total_list)
                        return loc
                elif  'GPR_Low' in client_dict[target_client]['journey']:
                    if Scen_NO_Sharing or Scen_part_bed_Share or Scen_shared_beds_Full:
                        loc = check_zero_indexes(n_beds_ELV_Low_list)
                        return loc
                    elif Scen_Total_Sharing:
                        loc = check_zero_indexes(n_beds_ELV_total_list)
                        return loc
            
            def Give_possible_locations(next_event):
                import random
                
                if next_event[4:12] == 'GPR_High' or next_event[4:12] == 'HOS_High' or next_event[4:7] == 'EMD' or next_event[4:11] == 'HOS_GRZ':
                    if Scen_shared_beds_Full:
                        if next_event[4:12] == 'GPR_High' or next_event[4:12] == 'HOS_High' or next_event[4:7] == 'EMD' or next_event[4:11] == 'HOS_GRZ':
                            loc = (check_zero_indexes(n_beds_ELV_High_list))
                            #change_target_client_location(target_client,loc,False)
                                #print('changed location from ',client_pref, 'to, ', loc)
                            #print(loc)
                            return loc
                        
                    elif Scen_NO_Sharing:
                        if next_event[4:12] == 'GPR_High' or next_event[4:12] == 'HOS_High' or next_event[4:7] == 'EMD':
                
                            loc = (check_zero_indexes(n_beds_ELV_High_list))
                                #change_target_client_location(target_client,loc,False)
                            return loc
                        elif next_event[4:11] == 'HOS_GRZ':
                
                            loc = (check_zero_indexes(n_beds_GRZ_list))
                #                     change_target_client_location(target_client,loc,False)
                            return loc
                        
                    elif Scen_part_bed_Share:
                        
                        if next_event[4:12] == 'GPR_High' or next_event[4:12] == 'HOS_High' or next_event[4:7] == 'EMD':
                
                            loc = (non_zero_indexes(n_beds_ELV_High_list,n_beds_shared_High_list))
                                #change_target_client_location(target_client,loc,False)
                            return loc  
                        elif next_event[4:11] == 'HOS_GRZ':
                
                
                            loc = (non_zero_indexes(n_beds_GRZ_list,n_beds_shared_High_list))
                                #change_target_client_location(target_client,loc,False)
                            return loc
                        
                    elif Scen_Total_Sharing:
                
                        loc = (check_zero_indexes(n_beds_ELV_total_list))
                            #change_target_client_location(target_client,loc,False)
                        return loc
                elif next_event[4:11] == 'GPR_Low':
                    if Scen_shared_beds_Full or Scen_part_bed_Share or Scen_NO_Sharing:
                        loc = (check_zero_indexes(n_beds_ELV_Low_list))
                            #change_target_client_location(target_client,loc,False)
                    elif Scen_Total_Sharing:
                        loc = (check_zero_indexes(n_beds_ELV_total_list))
                    return loc
            
            def order_journeys(data, n_loc):
                ordered_data = {}
                for key, value in data.items():
                    # Zip journey and j_times together
                    zipped_data = zip(value['journey'], value['j_times'])
                    # Sort the zipped data based on j_times
                    sorted_data = sorted(zipped_data, key=lambda x: x[1])
                    # Unzip the sorted data
                    ordered_journey, ordered_j_times = zip(*sorted_data)
                    # Modify the journey names and corresponding j_times
                    modified_journey = []
                    modified_j_times = []
                    for journey, j_time in zip(ordered_journey, ordered_j_times):
                        # Check if journey contains any of the specified patterns
                        patterns = ['ELV_High_', 'ELV_Low_', 'ELV_part_', 'TRW_', 'ELV_EMDR_', 'ELV_TOT_']
                        for pattern in patterns:
                            if pattern in journey:
                                journey = journey.split(pattern)[0] + pattern[:-1]  # Remove the '_+number' part
                                break
                        modified_journey.append(journey)
                        modified_j_times.append(j_time)
                        #print("1" , modified_journey)
                    # Check if both 'ELV_High' and 'ELV_Low' are present, and handle accordingly
                    if 'ELV_High' in modified_journey and 'ELV_Low' in modified_journey:
                        #print(modified_journey)
                        if 'GPR_Low' in modified_journey:
                            
                            # If 'GPR_LOW' is present, keep 'ELV_Low' and remove 'ELV_High'
                            index = modified_journey.index('ELV_High')
                            #print(index)
                            modified_journey.remove('ELV_High')
                            # Also remove corresponding j_time
                            
                            modified_j_times.pop(index)
                        else:
                            # Otherwise, remove 'ELV_Low' and keep 'ELV_High'
                            index = modified_journey.index('ELV_Low')
                            modified_journey.remove('ELV_Low')
                    #         # Also remove corresponding j_time
                            
                            modified_j_times.pop(index)
                    # # Create a new dictionary with the ordered and modified journey names and j_times
                    else:
                        modified_journey = modified_journey
                    ordered_data[key] = {'journey': list(modified_journey), 'j_times': list(modified_j_times)}
                return ordered_data
            
            def Check_eff_beds_with_nurses(n_pat_per_nurse):
                print('------------ Check effective beds ------------------')
                if Scen_Total_Sharing:
                    for i in range(len(n_beds_ELV_total_list)):
                        if n_beds_ELV_total_list[i]-(total_nurses[i]*n_pat_per_nurse) ==0:
                            n_beds_ELV_total_list[i] = n_beds_ELV_total_list[i]
                            print('Location',i, 'Number of total shared beds available: ',n_beds_ELV_total_list[i], '      Number of effective beds:',  (total_nurses[i]*n_pat_per_nurse))
                        elif n_beds_ELV_total_list[i]-(total_nurses[i]*n_pat_per_nurse) >0:
                            
                            print('Number of total shared beds available: ',n_beds_ELV_total_list[i], '      Number of effective total shared beds:',  (total_nurses[i]*n_pat_per_nurse), ' So, ', n_beds_ELV_total_list[i]-(total_nurses[i]*n_pat_per_nurse), 'Beds lost')
                            n_beds_ELV_total_list[i] = (total_nurses[i]*n_pat_per_nurse)
                    
                        else:
                            print('Number of total shared beds available: ',n_beds_ELV_total_list[i], '      Number of total shared effective beds:',  (total_nurses[i]*n_pat_per_nurse), ' So, ', -(n_beds_ELV_total_list[i]-(total_nurses[i]*n_pat_per_nurse)), 'To many')
            
                            n_beds_ELV_total_list[i] = n_beds_ELV_total_list[i]
                elif Scen_shared_beds_Full:
                    for i in range(len(n_beds_ELV_High_list)):
            
                        if n_beds_ELV_High_list[i]-(elv_high_complex_nurses[i]*n_pat_per_nurse) == 0:
                            n_beds_ELV_High_list[i] =n_beds_ELV_High_list[i]
                            print('Location',i,'Number of ELV high complex beds available: ',n_beds_ELV_High_list[i], '      Number of ELV High complex effective beds:',  (elv_high_complex_nurses[i]*n_pat_per_nurse))
                        elif n_beds_ELV_High_list[i]-(elv_high_complex_nurses[i]*n_pat_per_nurse) >0:
                            
                            print('Location',i,'Number of ELV high complex beds available: ',n_beds_ELV_High_list[i], '      Number of ELV high complex effective beds:',  (elv_high_complex_nurses[i]*n_pat_per_nurse), ' So, ', n_beds_ELV_High_list[i]-(elv_high_complex_nurses[i]*n_pat_per_nurse), 'Beds lost')
                           
                            n_beds_ELV_High_list[i] = (elv_high_complex_nurses[i]*n_pat_per_nurse)
                        else:
                            print('Location',i,'Number of ELV high complex beds available: ',n_beds_ELV_High_list[i], '      Number of ELV high complex effective beds:',  (elv_high_complex_nurses[i]*n_pat_per_nurse), ' So, ', -(n_beds_ELV_High_list[i]-(elv_high_complex_nurses[i]*n_pat_per_nurse)), 'To many')
                            
                            
                            n_beds_ELV_High_list[i] = n_beds_ELV_High_list[i]
                    for i in range(len(n_beds_ELV_Low_list)):
                        if n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse) == 0:
                            n_beds_ELV_Low_list[i] =n_beds_ELV_Low_list[i]
                            print('Location',i,'Number of ELV Low complex beds available: ',n_beds_ELV_Low_list[i], '      Number of ELV Low effective beds:',  (elv_low_complex_nurses[i]*n_pat_per_nurse))
                        elif n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse) >0:
                            
                            print('Location',i, 'Number of ELV Low beds available: ',n_beds_ELV_Low_list[i], '      Number of ELV Low effective beds',  (elv_low_complex_nurses[i]*n_pat_per_nurse), ' So, ', n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse), 'Beds lost')
                            n_beds_ELV_Low_list[i] =elv_low_complex_nurses[i]*n_pat_per_nurse
                        else:
                            
                            print('Location',i, 'Number of ELV Low beds available: ',n_beds_ELV_Low_list[i], '      Number of ELV Low effective beds',  (elv_low_complex_nurses[i]*n_pat_per_nurse), ' So, ', -(n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse)), 'To many')
                            n_beds_ELV_Low_list[i] =n_beds_ELV_Low_list[i]
                            
                elif Scen_NO_Sharing or Scen_part_bed_Share:
                    for i in range(len(n_beds_High_Complex_list)):
            
                        if n_beds_High_Complex_list[i]-(high_complex_nurses[i]*n_pat_per_nurse) == 0:
                            n_beds_High_Complex_list[i] =n_beds_High_Complex_list[i]
                            print('Location',i, 'Number of High complex beds available: ',n_beds_High_Complex_list[i], '      Number of High complex effective beds:',  (high_complex_nurses[i]*n_pat_per_nurse))
                        elif n_beds_High_Complex_list[i]-(high_complex_nurses[i]*n_pat_per_nurse) >0:
                            
                            print('Location',i,'Number of High complex beds available: ',n_beds_High_Complex_list[i], '      Number of High complex effective beds:',  (high_complex_nurses[i]*n_pat_per_nurse), ' So, ', n_beds_High_Complex_list[i]-(high_complex_nurses[i]*n_pat_per_nurse), 'Beds lost')
                            
                            n_beds_High_Complex_list[i] = (high_complex_nurses[i]*n_pat_per_nurse)
                        else:
                            
                            print('Location',i,'Number of High complex beds available: ',n_beds_High_Complex_list[i], '      Number of High complex effective beds:',  (high_complex_nurses[i]*n_pat_per_nurse), ' So, ', -(n_beds_High_Complex_list[i]-(high_complex_nurses[i]*n_pat_per_nurse)), 'To many')
                            n_beds_High_Complex_list[i] =n_beds_High_Complex_list[i]
                    for i in range(len(n_beds_GRZ_list)):
            
                        if n_beds_GRZ_list[i]-(grz_nurses[i]*n_pat_per_nurse) == 0:
                            n_beds_GRZ_list[i] =n_beds_GRZ_list[i]
                            print('Location',i,'Number of GRZ beds available: ',n_beds_GRZ_list[i], '      Number of GRZ effective beds:',  (grz_nurses[i]*n_pat_per_nurse))
                        elif n_beds_GRZ_list[i]-(grz_nurses[i]*n_pat_per_nurse) >0:
                            
                            
                            print('Location',i,'Number of GRZ beds available: ',n_beds_GRZ_list[i], '       Number of GRZ effective beds:',  (grz_nurses[i]*n_pat_per_nurse), ' So, ', n_beds_GRZ_list[i]-(grz_nurses[i]*n_pat_per_nurse), 'Beds lost')
                            n_beds_GRZ_list[i] = (grz_nurses[i]*n_pat_per_nurse)
                        else:
                            
                            print('Location',i,'Number of GRZ beds available: ',n_beds_GRZ_list[i], '       Number of GRZ effective beds:',  (grz_nurses[i]*n_pat_per_nurse), ' So, ', -(n_beds_GRZ_list[i]-(grz_nurses[i]*n_pat_per_nurse)), 'To many')
                            n_beds_GRZ_list[i] =n_beds_GRZ_list[i]
                            
                    for i in range(len(n_beds_ELV_Low_list)):
                        if n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse) == 0:
                            n_beds_ELV_Low_list[i] =n_beds_ELV_Low_list[i]
                            print('Location',i,'Number of ELV Low beds available: ',n_beds_ELV_Low_list[i], '      Number of ELV Low effective beds:',  (elv_low_complex_nurses[i]*n_pat_per_nurse))
                        elif n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse) >0:
                            print('Location',i,'Number of ELV Low beds available: ',n_beds_ELV_Low_list[i], '     Number of ELV Low effective beds:',  (elv_low_complex_nurses[i]*n_pat_per_nurse), ' So, ', n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse), 'Beds lost')
                            
                            n_beds_ELV_Low_list[i] =elv_low_complex_nurses[i]*n_pat_per_nurse
                        else:
                            
                            print('Location',i,'Number of ELV Low beds available: ',n_beds_ELV_Low_list[i], '     Number of ELV Low effective beds:',  (elv_low_complex_nurses[i]*n_pat_per_nurse), ' So, ', -(n_beds_ELV_Low_list[i]-(elv_low_complex_nurses[i]*n_pat_per_nurse)), 'To many')
                            n_beds_ELV_Low_list[i] =n_beds_ELV_Low_list[i]
                            
                print('----------------------------------------------------')
                            
               
            def delete_events_with_target_client(event_dict, target_client):
                # Create a new dictionary to store events without the target_client
                new_event_dict = {}
                # Iterate over each key-value pair in the event_dict
                for key, value in event_dict.items():
                    # Check if the target_client is not in the key
                    if target_client not in key:
                        # If the target_client is not in the key, add it to the new_event_dict
                        new_event_dict[key] = value
                # Return the new_event_dict without the events containing the target_client
                return new_event_dict
            elv_high_complex_beds = input.loc[loop_nr,'elv_high_complex_beds']
            
            #elv_high_complex_beds = change_string_to_list(elv_high_complex_beds)
            high_complex_beds = input.loc[loop_nr, 'high_complex_beds']
            #high_complex_beds = change_string_to_list(high_complex_beds)
            grz_beds = input.loc[loop_nr,'grz_beds']
            #grz_beds = change_string_to_list(grz_beds)
            shared_beds = input.loc[loop_nr,'shared_beds']
            #shared_beds = change_string_to_list(shared_beds)
            elv_low_complex_beds = input.loc[loop_nr,'elv_low_complex_beds']
            #elv_low_complex_beds = change_string_to_list(elv_low_complex_beds)
            beds_TRW_list = input.loc[loop_nr,'trw_beds']
            #beds_TRW_list = change_string_to_list(beds_TRW_list)
            total_beds = input.loc[loop_nr,'total_beds']
            #total_beds = change_string_to_list(total_beds)
            beds_Emergency_list = input.loc[loop_nr,'emergency_beds']
            #beds_Emergency_list = change_string_to_list(beds_Emergency_list)
        
            elv_high_complex_nurses = input.loc[loop_nr,'elv_high_complex_nurses']
            #elv_high_complex_nurses = change_string_to_list(elv_high_complex_nurses)
            high_complex_nurses = input.loc[loop_nr,'high_complex_nurses']
            #high_complex_nurses = change_string_to_list(high_complex_nurses)
            grz_nurses = input.loc[loop_nr,'grz_nurses']
            #grz_nurses = change_string_to_list(grz_nurses)
            shared_nurses = input.loc[loop_nr,'shared_nurses']
            #shared_nurses = change_string_to_list(shared_nurses)
            elv_low_complex_nurses = input.loc[loop_nr,'elv_low_complex_nurses']
            #elv_low_complex_nurses = change_string_to_list(elv_low_complex_nurses)
            trw_nurses = input.loc[loop_nr,'trw_nurses']
            #trw_nurses = change_string_to_list(trw_nurses)
            total_nurses = input.loc[loop_nr,'total_nurses']
            #total_nurses = change_string_to_list(total_nurses)
            
            if Scen_shared_beds_Full:
        #         bed_list = bed_list_Full
                n_beds_ELV_High_list = elv_high_complex_beds #make_bed_variables(n_loc,"Full",bed_list)[0]
                n_beds_ELV_Low_list = elv_low_complex_beds #make_bed_variables(n_loc,"Full",bed_list)[1]
                loc_ELV_High = (check_zero_indexes(n_beds_ELV_High_list))
                loc_ELV_Low = (check_zero_indexes(n_beds_ELV_Low_list))
            elif Scen_part_bed_Share:
        #         bed_list = bed_list_Part
                n_beds_GRZ_list= grz_beds #make_bed_variables(n_loc,"Part",bed_list)[0]
                n_beds_High_Complex_list = high_complex_beds #make_bed_variables(n_loc,"Part",bed_list)[1]
                n_beds_ELV_Low_list = elv_low_complex_beds #make_bed_variables(n_loc,"Part",bed_list)[3]
                n_beds_shared_High_list= shared_beds #make_bed_variables(n_loc,"Part",bed_list)[2]
                n_beds_ELV_High_list = sum_lists(n_beds_High_Complex_list,n_beds_shared_High_list)
                n_beds_ELV_High_list = sum_lists(n_beds_ELV_High_list,n_beds_GRZ_list)
                loc_ELV_High = (check_zero_indexes(n_beds_ELV_High_list))
                loc_ELV_Low = (check_zero_indexes(n_beds_ELV_Low_list))
            #print("a")
            elif Scen_NO_Sharing: # 1
        #         bed_list = bed_list_NO
                n_beds_GRZ_list= grz_beds #make_bed_variables(n_loc,"None",bed_list)[0]
                n_beds_High_Complex_list= high_complex_beds #make_bed_variables(n_loc,"None",bed_list)[1]
                n_beds_ELV_Low_list = elv_low_complex_beds #make_bed_variables(n_loc,"None",bed_list)[2]
                n_beds_ELV_High_list = sum_lists(n_beds_High_Complex_list,n_beds_GRZ_list)
                loc_ELV_High = (check_zero_indexes(n_beds_ELV_High_list))
                loc_ELV_Low = (check_zero_indexes(n_beds_ELV_Low_list))
            elif Scen_Total_Sharing:
                n_beds_ELV_total_list =  total_beds#make_bed_variables(n_loc,"Total",bed_list)
        
                loc_ELV_High = (check_zero_indexes(n_beds_ELV_total_list))
                loc_ELV_Low = (check_zero_indexes(n_beds_ELV_total_list))
            Check_eff_beds_with_nurses(n_patients_per_nurse)
            check_balanced_system(int(n_loc))  
            perc_compl = 0
            
            print("===========================================================")
            print("================== START SIMULATION =======================")
            print("===========================================================")
        
            while n_subrun < n_subruns:
                
                if math.floor(n_subrun/n_subruns*100) > perc_compl:
                    perc_compl = math.floor(n_subrun/n_subruns*100)
                    print(perc_compl, '% completed')
                
                n_subrun += 1
                n_evaluated_current_run = 0
                    
                if n_subrun == 1:
                    
                    # initialization 
                    
                    current_time = 0
                
                    event_dict = {'timestamp_arr_HOS_GRZ': exp(arr_HOS_GRZ),
                                  'timestamp_arr_HOS_High': exp(arr_HOS_High),
                                  'timestamp_arr_GPR_High': exp(arr_GPR_High),
                                  'timestamp_arr_EMD': exp(arr_EMD),
                                  'timestamp_arr_GPR_Low': exp(arr_GPR_Low),
                                  'check_bez': EMD_end_time - 0.0001
                                 }
         
                start_time_subrun = current_time
                
                while n_evaluated_current_run <= n_clients_per_subrun:      
        
                    # ----------------------------------------------------------------
                    # --------------------------- START SIMULATION -------------------
                    # ----------------------------------------------------------------
        
                    # het kan zijn dat je nog niemand hebt die dood kan gaan. 
                    # Dan moet die ook niet 
                    # in de eventList
        
                    next_event = min(event_dict, key=event_dict.get)
                    current_time_min_1 = current_time
                    current_time = event_dict[next_event]
                    
                               
                    # ---------------------------------------------------------
                    # ------------------------------------- ARRIVAL -----------
                    # ---------------------------------------------------------
        
                    if next_event[0:3] == 'arr': 
                        
                        if print_modus:
                            print('___________________________________________________')
                            print('>>> arrival <<<')
                            print('___________________________________________________')
                        
                        if n_client == n_clients_for_warming:
                                start_time_eval = current_time
                                
                        n_client += 1
                        loc = Give_possible_locations(next_event)
        #                 print(next_event)
        #                 print(loc)
                        Location = random.choice(loc)
                        target_client = 'c_' + str(n_client) + "_" + str(Location)
                        
                        #print("target_client",target_client)
                        
                        if print_modus:
                            print('at', current_time, target_client,' arrives from', next_event[4:7])
                        if next_event[4:12] == 'GPR_High':
                            client_dict_temp = {target_client: {
                               'current_loc': next_event[4:12],
                               'journey': [next_event[4:12]],
                               'j_times': [current_time],
                               }
                            }
                        elif next_event[4:11] == 'GPR_Low':
                            client_dict_temp = {target_client: {
                               'current_loc': next_event[4:11],
                               'journey': [next_event[4:11]],
                               'j_times': [current_time],
                               }
                            }
                        elif next_event[4:11] == 'HOS_GRZ':
                            client_dict_temp = {target_client: {
                               'current_loc': next_event[4:11],
                               'journey': [next_event[4:11]],
                               'j_times': [current_time],
                               }
                            }
                        elif next_event[4:12] == 'HOS_High':
                            client_dict_temp = {target_client: {
                               'current_loc': next_event[4:12],
                               'journey': [next_event[4:12]],
                               'j_times': [current_time],
                               }
                            }    
                        elif next_event[4:7] == 'EMD' :
                            client_dict_temp = {target_client: {
                               'current_loc': next_event[4:7],
                               'journey': [next_event[4:7]],
                               'j_times': [current_time],
                               }
                            }
                        client_dict.update(client_dict_temp)
                        
                        #check_client_pref_is_possible_event(target_client,next_event,'Event')
                        
                        if Scen_tr_ward:
                            if next_event[4:7] == 'EMD' or next_event[4:12] == 'HOS_High' or next_event[4:11] == 'HOS_GRZ' or next_event[4:12] == 'GPR_High': 
                                if sum(beds_TRW_list)>0:
                                    p_observation = np.random.uniform(0,1)
                                else: 
                                    p_observation = 1
                                if p_observation < 0.1:
                                    if count_patients('TRW') + count_place_reserved('TRW') >= beds_TRW_list[extract_number(target_client)]: # op wachtlijst
                                        if Preference == 'FCFS':
                                            if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,True)[0] == True:
                                                change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,True)[1],True)
                                                time_until_placement = exp(adm_days)    
        
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5] and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
                        
                                                    time_until_placement = exp(adm_days)                
                        
                                                else: #15
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                        
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                            # move to ELV vanaf time_until_placement
                                                move_to_TRW_High(target_client, time_until_placement)
                                            else: 
                                                if print_modus:
                                                    print(target_client, 'gaat op wachtlijst')
            
                                                if next_event[4:12] == 'HOS_High'or next_event[4:7] == 'EMD':
                                                    add_to_waiting_dict(w3_dict_TRW,target_client,current_time)
                                                elif next_event[4:11] == 'HOS_GRZ':
                                                    add_to_waiting_dict(w4_dict_TRW,target_client,current_time)
                                                    #wait_list_3_TRW.append(target_client)
                                                elif next_event[4:12] == 'GPR_High':
                                                    add_to_waiting_dict(w2_dict_TRW,target_client,current_time)
                    #                                 wait_list_2_TRW.append(target_client)
                    #                                 type_of_w2_TRW.append(next_event[4:7])
                                                if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                    client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                    client_dict[target_client]['j_times'].append(current_time)
            
                                            
                                                # als vanuit SEH misschien ziekenhuisopname
            
                                                if next_event[4:7] == 'EMD':
                                    
                                                    if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                        move_to_ELV_Emergency(target_client,0)
                                                    else:
                                                        event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
            
                                                        if print_modus:
                                                            print('patient from seh en dus evt hosp opname om ', event_dict['HOSP_adm_' + target_client])
            #                                     
                                        
                                                        
                                        elif Preference == 'Pref' or Preference == 'NO':
                                            if print_modus:
                                                print(target_client, 'gaat op wachtlijst')
            
                                            if next_event[4:12] == 'HOS_High'or next_event[4:7] == 'EMD':
                                                add_to_waiting_dict(w3_dict_TRW,target_client,current_time)
                                            elif next_event[4:11] == 'HOS_GRZ':
                                                    add_to_waiting_dict(w4_dict_TRW,target_client,current_time)
                                            
                                            
                                               
                                            elif next_event[4:12] == 'GPR_High' :
                                                add_to_waiting_dict(w2_dict_TRW,target_client,current_time)
                
                                            if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                client_dict[target_client]['j_times'].append(current_time)
            
                                            # als vanuit SEH misschien ziekenhuisopname
            
                                            if next_event[0:7] == 'arr_EMD':
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                    move_to_ELV_Emergency(target_client,0)
                                                
                                                elif (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
        
                                                    event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
        
                                                    if print_modus:
                                                        print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
        
                                                else: # na 17 uur of weekend meteen ziekenhuis opname
        
                                                    if print_modus:
                                                        print('patient from EMD en na 17 of weekend dus HOSP opname')
        
                                                    move_to_HOSP(target_client)
            #                                
                                    else: # kan naar trw       
        
                                        if print_modus:
                                            print('geen wachtlijst dus kan direct naar trw')
            
                                        move_to_TRW_High(target_client, 0)
        
                                else:  #aanpassen
                                    if sum(n_beds_shared_High_list)==0:
                                        if next_event[4:12] == 'HOS_High':#3
                                            if Check_space_partial_beds('HOS_High') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#!@#$%
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
                                                        if next_event[4:12] == 'HOS_High':
                                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                            client_dict[target_client]['j_times'].append(current_time)
            #                                             wait_list_3.append(target_client)
                                                elif Preference == 'NO' or Preference == 'Pref':
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
                                                    if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                        client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                        client_dict[target_client]['j_times'].append(current_time)
        #                                             wait_list_3.append(target_client)
                                            else: #can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:#$%^
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                
                                    
                                        elif next_event[4:7] == 'EMD':
                                            if Check_space_partial_beds('EMD') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:#!@#
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                        
                                                        
                                                    elif (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                        move_to_ELV_Emergency(target_client,0)
                                                    else:#@!@
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
               
                
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_EMD and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
            
                                                            event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + time_max_opn_EMD
            
                                                            if print_modus:
                                                                print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
            
                                                        else:# na 17 uur of weekend meteen ziekenhuis opname
            
                                                            if print_modus:
                                                                print('patient from EMD en na 17 of weekend dus HOSP opname')
            
                                                            move_to_HOSP(target_client)
                                                elif Preference == 'NO' or Preference == 'Pref':
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
            
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                        move_to_ELV_Emergency(target_client,0)
                                                    
                                                    elif (current_time - math.floor(current_time) <= time_max_opn_EMD and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
            
                                                        event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + time_max_opn_EMD
            
                                                        if print_modus:
                                                            print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
            
                                                    else:# na 17 uur of weekend meteen ziekenhuis opname
            
                                                        if print_modus:
                                                            print('patient from EMD en na 17 of weekend dus HOSP opname')
            
                                                        move_to_HOSP(target_client)
                #                                     
            
                                            # anders kan deze naar ELV
                                            else:#22
            
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#23
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:####
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                
                                        elif next_event[4:12] == 'GPR_High':
                                            if Check_space_partial_beds('GPR_High') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:#$5678
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#24
                                                        add_to_waiting_dict(w2_dict,target_client,current_time)
                                                        
            #                                             
                                                elif Preference == 'NO'or Preference == 'Pref':
                                                    add_to_waiting_dict(w2_dict,target_client,current_time)
                                                
                                                        
                #                                             
                                            else:#Can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#25
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:#1234
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                
                                        elif next_event[4:11] == 'HOS_GRZ':
                                            
                                            if Check_space_partial_beds('HOS_GRZ') >= n_beds_GRZ_list[extract_number(target_client)] :
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#27
                                                        if next_event[4:11] == 'HOS_GRZ':
                                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                            client_dict[target_client]['j_times'].append(current_time)
                                                            add_to_waiting_dict(w4_dict,target_client,current_time)
            #                                             
                                                elif Preference == 'NO' or Preference == 'Pref':
                                                    add_to_waiting_dict(w4_dict,target_client,current_time)
                                                    if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                        client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                        client_dict[target_client]['j_times'].append(current_time)
                                            else:#can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#28
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                            elif next_event[4:11] == 'GPR_Low':
                                if count_patients('ELV_Low') + count_place_reserved('ELV_Low') >= n_beds_ELV_Low_list[extract_number(target_client)]: # op wachtlijst
                                    if Preference == 'FCFS':
                                        if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                            change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)  
                                            time_until_placement = exp(adm_days)    
        
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                    
                                                time_until_placement = exp(adm_days)                
                    
                                            else: #15
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                    
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                            # move to ELV vanaf time_until_placement
                                            move_to_ELV_Low(target_client, time_until_placement)
                                        else:
                                    
                                            if print_modus:
                                                    print(target_client, 'gaat op wachtlijst')
                                            add_to_waiting_dict(w1_dict,target_client,current_time)
                #                             wait_list_1.append(target_client)
                                    elif Preference == 'Pref' or Preference == 'NO':
                                        if print_modus:
                                                    print(target_client, 'gaat op wachtlijst')
                                        add_to_waiting_dict(w1_dict,target_client,current_time)
            #                             wait_list_1.append(target_client)
        
        
        
        
                                # anders kan deze naar ELV
                                else:#29
        
                                    time_until_placement = exp(adm_days)    
        
                                    p_acc_opn = np.random.uniform(0,1)
                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                        # voor 17h en geen weekend of prob accept!
        
                                        time_until_placement = exp(adm_days)                
        
                                    else:#30
                                        if math.floor(current_time) % 7 in [6,0]: 
                                            # als weekend
                                            if math.floor(current_time) % 7 == 0:
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                            else:#31
                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
        
                                            if print_modus:
                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
        
                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                            # als avond
                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
        
                                            if print_modus:
                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
        
                                    # move to ELV vanaf time_until_placement
        
                                    move_to_ELV_Low(target_client, time_until_placement)
                         
                        elif Scen_Total_Sharing:
                            if count_patients('ELV_TOT') +count_place_reserved('ELV_TOT') < n_beds_ELV_total_list[extract_number(target_client)]: #Kan naar ELV_TOTAL
                                time_until_placement = exp(adm_days)    
        
                                p_acc_opn = np.random.uniform(0,1)
                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                    # voor 17h en geen weekend of prob accept!
        
                                    time_until_placement = exp(adm_days)                
        
                                else: #15
                                    if math.floor(current_time) % 7 in [6,0]: 
                                        # als weekend
                                        if math.floor(current_time) % 7 == 0:
                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                        else:
                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
        
                                        if print_modus:
                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
        
                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                        # als avond
                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
        
                                        if print_modus:
                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
        
                                # move to ELV vanaf time_until_placement
        
                                move_to_ELV_Total(target_client, time_until_placement)
                                
                            else:
                                if Preference == 'FCFS':
                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                        time_until_placement = exp(adm_days)    
        
                                        p_acc_opn = np.random.uniform(0,1)
                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                            # voor 17h en geen weekend of prob accept!
                
                                            time_until_placement = exp(adm_days)                
                
                                        else: #15
                                            if math.floor(current_time) % 7 in [6,0]: 
                                                # als weekend
                                                if math.floor(current_time) % 7 == 0:
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                else:
                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                
                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                # als avond
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                
                                            # move to ELV vanaf time_until_placement
                                        move_to_ELV_Total(target_client,time_until_placement)
                                    if next_event[0:7] == 'arr_EMD':
                                        if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                            move_to_ELV_Emergency(target_client,0)
                                        else:#16
                                            
        
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
        
                                                event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
        
                                                if print_modus:
                                                    print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
        
                                            else: # na 17 uur of weekend meteen ziekenhuis opname
        
                                                if print_modus:
                                                    print('patient from EMD en na 17 of weekend dus HOSP opname')
        
                                                move_to_HOSP(target_client)
                                            
                                            
                                            add_to_waiting_dict(w_tot_dict,target_client,current_time)
                                    
                                        
                                    else:
                                        add_to_waiting_dict(w_tot_dict,target_client,current_time)
                                        #wait_list_Total.append(target_client)
                                        if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                            client_dict[target_client]['j_times'].append(current_time)
                                elif Preference == 'NO' or Preference == 'Pref':
                                    if next_event[0:7] == 'arr_EMD':
                                        p_acc_opn = np.random.uniform(0,1)
                                        if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                            move_to_ELV_Emergency(target_client,0)
                                        
                                        elif (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
        
                                            event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
        
                                            if print_modus:
                                                print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
        
                                        else: # na 17 uur of weekend meteen ziekenhuis opname
        
                                            if print_modus:
                                                print('patient from EMD en na 17 of weekend dus HOSP opname')
        
                                            move_to_HOSP(target_client)
                                         
                                        add_to_waiting_dict(w_tot_dict,target_client,current_time)
                                        
                                    else:
                                        add_to_waiting_dict(w_tot_dict,target_client,current_time)  
                                        if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                            client_dict[target_client]['j_times'].append(current_time)
                        elif Scen_NO_Sharing or Scen_part_bed_Share or Scen_shared_beds_Full:    
                            if next_event[4:11] == 'GPR_Low':
                                # if Scen_shared_beds_Full or Scen_part_bed_Share or Scen_NO_Sharing:
                                if count_patients('ELV_Low') + count_place_reserved('ELV_Low') >= n_beds_ELV_Low_list[extract_number(target_client)]: # op wachtlijst
                                    if Preference == 'FCFS':
                                        if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                            change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)  
                                            time_until_placement = exp(adm_days)    
        
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                    
                                                time_until_placement = exp(adm_days)                
                    
                                            else: #15
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                    
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                    
                                            # move to ELV vanaf time_until_placement
                    
                                            move_to_ELV_Low(target_client, time_until_placement)
                                        else:
                                    
                                            if print_modus:
                                                    print(target_client, 'gaat op wachtlijst')
                                            add_to_waiting_dict(w1_dict,target_client,current_time)
                #                             wait_list_1.append(target_client)
                                    elif Preference == 'Pref' or Preference == 'NO':
                                        if print_modus:
                                            print(target_client, 'gaat op wachtlijst')
                                        add_to_waiting_dict(w1_dict,target_client,current_time)
            #                             wait_list_1.append(target_client)
        
        
        
        
                                # anders kan deze naar ELV
                                else:#29
        
                                    time_until_placement = exp(adm_days)    
        
                                    p_acc_opn = np.random.uniform(0,1)
                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                        # voor 17h en geen weekend of prob accept!
        
                                        time_until_placement = exp(adm_days)                
        
                                    else:#30
                                        if math.floor(current_time) % 7 in [6,0]: 
                                            # als weekend
                                            if math.floor(current_time) % 7 == 0:
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                            else:#31
                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
        
                                            if print_modus:
                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
        
                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                            # als avond
                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
        
                                            if print_modus:
                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
        
                                    # move to ELV vanaf time_until_placement
        
                                    move_to_ELV_Low(target_client, time_until_placement)
                        
                            elif next_event[4:12] == 'HOS_High' or next_event[4:12] == 'GPR_High' or next_event[4:7] == 'EMD' or next_event[4:11] == 'HOS_GRZ':
                                if Scen_shared_beds_Full:
                                    if next_event[4:12] == 'HOS_High' or next_event[4:12] == 'GPR_High' or next_event[4:7] == 'EMD' or next_event[4:11] == 'HOS_GRZ' :
                                        if count_patients('ELV_High') + count_place_reserved('ELV_High') >= n_beds_ELV_High_list[extract_number(target_client)]: # op wachtlijst
                                            if Preference == 'FCFS':
                                                if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                    change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                    time_until_placement = exp(adm_days)    
        
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                        # voor 17h en geen weekend of prob accept!
                            
                                                        time_until_placement = exp(adm_days)                
                            
                                                    else: #15
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                            # move to ELV vanaf time_until_placement
                                                    move_to_ELV_High(target_client,time_until_placement)
                
                                                else:#17
                #                                                 
                                                    if next_event[4:12] == 'HOS_High' or next_event[4:7] == 'EMD':#1
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
                                                    elif next_event[4:11] == 'HOS_GRZ':
                                                        add_to_waiting_dict(w4_dict,target_client,current_time)
                                                        
                                                      
                                                    elif next_event[4:12] == 'GPR_High' :
                                                        add_to_waiting_dict(w2_dict,target_client,current_time)
                                                    if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                        client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                        client_dict[target_client]['j_times'].append(current_time)      
                                                    if next_event[0:7] == 'arr_EMD':
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                            move_to_ELV_Emergency(target_client,0)
                                                        
                                                        elif (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
                
                                                            event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
                
                                                            if print_modus:
                                                                print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
                
                                                        else: # na 17 uur of weekend meteen ziekenhuis opname
                
                                                            if print_modus:
                                                                print('patient from EMD en na 17 of weekend dus HOSP opname')
                
                                                            move_to_HOSP(target_client)
                #                                        
                                                        
                                                        
                                            elif Preference == 'Pref' or Preference == 'NO':
                                                if next_event[4:12] == 'HOS_High' or next_event[4:7] == 'EMD':#1
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
                                                elif next_event[4:11] == 'HOS_GRZ':
                                                    add_to_waiting_dict(w4_dict,target_client,current_time)
                                                    
                                                  
                                                elif next_event[4:12] == 'GPR_High' :
                                                    add_to_waiting_dict(w2_dict,target_client,current_time)
                                                if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                    client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                    client_dict[target_client]['j_times'].append(current_time)         
                                                if next_event[0:7] == 'arr_EMD':
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                        move_to_ELV_Emergency(target_client,0)
                                                    
                                                    elif (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
            
                                                        event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
            
                                                        if print_modus:
                                                            print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
            
                                                    else: # na 17 uur of weekend meteen ziekenhuis opname
            
                                                        if print_modus:
                                                            print('patient from EMD en na 17 of weekend dus HOSP opname')
            
                                                        move_to_HOSP(target_client)
                #                                             
                                        # anders kan deze naar ELV
                                        else: #18
                
                                            time_until_placement = exp(adm_days)    
                
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                
                                                time_until_placement = exp(adm_days)                
                
                                            else:
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                
                                            # move to ELV vanaf time_until_placement
                
                                            move_to_ELV_High(target_client, time_until_placement)
                                    
                                                             #print("b")
                                   
                                            
                                elif Scen_part_bed_Share or Scen_NO_Sharing:
                                    if sum(n_beds_shared_High_list)==0:
                                        if next_event[4:12] == 'HOS_High':#3
                                            if Check_space_partial_beds('HOS_High') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#!@#$%
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
                                                        if next_event[4:12] == 'HOS_High':
                                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                            client_dict[target_client]['j_times'].append(current_time)
            #                                             wait_list_3.append(target_client)
                                                elif Preference == 'NO' or Preference == 'Pref':
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
                                                    if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                        client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                        client_dict[target_client]['j_times'].append(current_time)
        #                                             wait_list_3.append(target_client)
                                            else: #can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:#$%^
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                
                                    
                                        elif next_event[4:7] == 'EMD':
                                            if Check_space_partial_beds('EMD') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:#!@#
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                        
                                                        
                                                    elif (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                        move_to_ELV_Emergency(target_client,0)
                                                    else:#@!@
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
               
                
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
            
                                                            event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
            
                                                            if print_modus:
                                                                print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
            
                                                        else:# na 17 uur of weekend meteen ziekenhuis opname
            
                                                            if print_modus:
                                                                print('patient from EMD en na 17 of weekend dus HOSP opname')
            
                                                            move_to_HOSP(target_client)
                                                elif Preference == 'NO' or Preference == 'Pref':
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
            
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                        move_to_ELV_Emergency(target_client,0)
                                                    
                                                    elif (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
            
                                                        event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
            
                                                        if print_modus:
                                                            print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
            
                                                    else:# na 17 uur of weekend meteen ziekenhuis opname
            
                                                        if print_modus:
                                                            print('patient from EMD en na 17 of weekend dus HOSP opname')
            
                                                        move_to_HOSP(target_client)
                #                                     
            
                                            # anders kan deze naar ELV
                                            else:#22
            
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#23
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:####
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                
                                        elif next_event[4:12] == 'GPR_High':
                                            if Check_space_partial_beds('GPR_High') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:#$5678
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#24
                                                        add_to_waiting_dict(w2_dict,target_client,current_time)
                                                        
            #                                             
                                                elif Preference == 'NO'or Preference == 'Pref':
                                                    add_to_waiting_dict(w2_dict,target_client,current_time)
                                                
                                                        
                #                                             
                                            else:#Can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#25
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:#1234
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                
                                        elif next_event[4:11] == 'HOS_GRZ':
                                            
                                            if Check_space_partial_beds('HOS_GRZ') >= n_beds_GRZ_list[extract_number(target_client)] :
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        time_until_placement = exp(adm_days)    
            
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                        
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#27
                                                        if next_event[4:11] == 'HOS_GRZ':
                                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                            client_dict[target_client]['j_times'].append(current_time)
                                                            add_to_waiting_dict(w4_dict,target_client,current_time)
            #                                             
                                                elif Preference == 'NO' or Preference == 'Pref':
                                                    add_to_waiting_dict(w4_dict,target_client,current_time)
                                                    if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                        client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                        client_dict[target_client]['j_times'].append(current_time)
                                            else:#can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#28
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                               
                                    elif sum(n_beds_shared_High_list)>0:
                                        if next_event[4:12] == 'HOS_High':#3
                                            if Check_space_partial_beds('HOS_High') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if count_patients('ELV_part')+count_place_reserved('ELV_part') < n_beds_shared_High_list[extract_number(target_client)]:
                                                    time_until_placement = exp(adm_days)    
            
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                        # voor 17h en geen weekend of prob accept!
                            
                                                        time_until_placement = exp(adm_days)                
                            
                                                    else: #15
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                    move_to_ELV_partial_bed(target_client,time_until_placement)
                                                else:
                                                    if Preference == 'FCFS':
                                                        if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                            change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                            time_until_placement = exp(adm_days)    
                
                                                            p_acc_opn = np.random.uniform(0,1)
                                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                                # voor 17h en geen weekend of prob accept!
                                    
                                                                time_until_placement = exp(adm_days)                
                                    
                                                            else: #15
                                                                if math.floor(current_time) % 7 in [6,0]: 
                                                                    # als weekend
                                                                    if math.floor(current_time) % 7 == 0:
                                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                    else:
                                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                    
                                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                    # als avond
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                    
                                                            # move to ELV vanaf time_until_placement
                                                            move_to_ELV_High(target_client,time_until_placement)
                                                        else:#!@#$%
                                                            if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                                client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                                client_dict[target_client]['j_times'].append(current_time)
                                                                add_to_waiting_dict(w3_dict,target_client,current_time)
               
                                                    elif Preference == 'NO' or Preference == 'Pref':
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
                                                        if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                            client_dict[target_client]['j_times'].append(current_time)
           
                                            else: #can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:#$%^
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                
                                        elif next_event[4:7] == 'EMD':
                                            if  Check_space_partial_beds('EMD') >= n_beds_High_Complex_list[extract_number(target_client)]: #Waiting line
                                                if count_patients('ELV_part')+count_place_reserved('ELV_part') < n_beds_shared_High_list[extract_number(target_client)]:
                                                    time_until_placement = exp(adm_days)    
            
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                        # voor 17h en geen weekend of prob accept!
                            
                                                        time_until_placement = exp(adm_days)                
                            
                                                    else: #15
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                    move_to_ELV_partial_bed(target_client,time_until_placement)
                                                else:
                                                    if Preference == 'FCFS':
                                                        if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                            change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                            time_until_placement = exp(adm_days)    
                
                                                            p_acc_opn = np.random.uniform(0,1)
                                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                                # voor 17h en geen weekend of prob accept!
                                    
                                                                time_until_placement = exp(adm_days)                
                                    
                                                            else: #15
                                                                if math.floor(current_time) % 7 in [6,0]: 
                                                                    # als weekend
                                                                    if math.floor(current_time) % 7 == 0:
                                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                    else:#!@#
                                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                    # als avond
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                            move_to_ELV_High(target_client,time_until_placement)
                                                        elif (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                            move_to_ELV_Emergency(target_client,0)
                                                        else:#@!@
                                                            add_to_waiting_dict(w3_dict,target_client,current_time)
                   
                    
                                                            p_acc_opn = np.random.uniform(0,1)
                                                            if (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
                
                                                                event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
                
                                                                if print_modus:
                                                                    print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
                
                                                            else:# na 17 uur of weekend meteen ziekenhuis opname
                
                                                                if print_modus:
                                                                    print('patient from EMD en na 17 of weekend dus HOSP opname')
                
                                                                move_to_HOSP(target_client)
                                                    elif Preference == 'NO' or Preference == 'Pref':
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
             
                                                       
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (math.floor(current_time) % 7 in [6,0] or  current_time - math.floor(current_time) > time_max_opn_ELV )and (count_patients('ELV_EMDR')+count_place_reserved('ELV_EMDR') <beds_Emergency_list[extract_number(target_client)]): 
                                                            move_to_ELV_Emergency(target_client,0)
                                                    
                                                        elif (current_time - math.floor(current_time) <= EMD_end_time and math.floor(current_time) % 7 in [1,2,3,4,5]) or p_acc_opn <= p_opn_weekend: # voor 17h
                
                                                            event_dict['HOSP_adm_' + target_client] = math.floor(current_time) + EMD_end_time
                
                                                            if print_modus:
                                                                print('patient from EMD en voor 17 doordeweeks dus evt HOSP opname om ', event_dict['HOSP_adm_' + target_client])
                
                                                        else:# na 17 uur of weekend meteen ziekenhuis opname
                
                                                            if print_modus:
                                                                print('patient from EMD en na 17 of weekend dus HOSP opname')
                
                                                            move_to_HOSP(target_client)
                #                                     
            
                                            # anders kan deze naar ELV
                                            else:#22
            
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#23
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:####
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                              
        
                                        elif next_event[4:12] == 'GPR_High':
                                            if Check_space_partial_beds('GPR_High') >= n_beds_High_Complex_list[extract_number(target_client)]:
                                                if count_patients('ELV_part')+count_place_reserved('ELV_part') < n_beds_shared_High_list[extract_number(target_client)]:
                                                    time_until_placement = exp(adm_days)    
            
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                        # voor 17h en geen weekend of prob accept!
                            
                                                        time_until_placement = exp(adm_days)                
                            
                                                    else: #15
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                    move_to_ELV_partial_bed(target_client,time_until_placement)
                                                else:
                                                    if Preference == 'FCFS':
                                                        if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                            change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                            time_until_placement = exp(adm_days)    
                
                                                            p_acc_opn = np.random.uniform(0,1)
                                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                                # voor 17h en geen weekend of prob accept!
                                    
                                                                time_until_placement = exp(adm_days)                
                            
                                                            else: #15
                                                                if math.floor(current_time) % 7 in [6,0]: 
                                                                    # als weekend
                                                                    if math.floor(current_time) % 7 == 0:
                                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                    else:#$5678
                                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                    
                                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                    # als avond
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                            move_to_ELV_High(target_client,time_until_placement)
                                                        else:#24
                                                            add_to_waiting_dict(w2_dict,target_client,current_time)
                                                            
                #                                             
                                                    elif Preference == 'NO'or Preference == 'Pref':
                                                        add_to_waiting_dict(w2_dict,target_client,current_time)
                                                
                                                        
                #                                             
                                            else:#Can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#25
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:#1234
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                              
                                        elif next_event[4:11] == 'HOS_GRZ':
                                            if Check_space_partial_beds('HOS_GRZ') >= n_beds_GRZ_list[extract_number(target_client)] :
                                                if count_patients('ELV_part')+count_place_reserved('ELV_part') < n_beds_shared_High_list[extract_number(target_client)]:
                                                
                                                    time_until_placement = exp(adm_days)    
            
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                        # voor 17h en geen weekend of prob accept!
                            
                                                        time_until_placement = exp(adm_days)                
                            
                                                    else: #15
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                    move_to_ELV_partial_bed(target_client,time_until_placement)
                                                else:
                                                    if Preference == 'FCFS':
                                                        if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                            change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                            time_until_placement = exp(adm_days)    
                
                                                            p_acc_opn = np.random.uniform(0,1)
                                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                                # voor 17h en geen weekend of prob accept!
                                    
                                                                time_until_placement = exp(adm_days)                
                                    
                                                            else: #15
                                                                if math.floor(current_time) % 7 in [6,0]: 
                                                                    # als weekend
                                                                    if math.floor(current_time) % 7 == 0:
                                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                    else:
                                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                    
                                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                    # als avond
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                    
                                                                    if print_modus:
                                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                    
                                                            # move to ELV vanaf time_until_placement
                                                            move_to_ELV_High(target_client,time_until_placement)
                                                        else:#27
                                                            if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                                client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                                client_dict[target_client]['j_times'].append(current_time)
                                                                add_to_waiting_dict(w4_dict,target_client,current_time)
                #                                             
                                                    elif Preference == 'NO' or Preference == 'Pref':
                                                        add_to_waiting_dict(w4_dict,target_client,current_time)
                                                        if next_event[4:12] == 'HOS_High'or next_event[4:11] == 'HOS_GRZ':
                                                            client_dict[target_client]['journey'].append('Extra_Hosp_adm')#1
                                                            client_dict[target_client]['j_times'].append(current_time)
                                            else:#can go to ELV
                                                time_until_placement = exp(adm_days)    
            
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
            
                                                    time_until_placement = exp(adm_days)                
            
                                                else:#28
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                                # move to ELV vanaf time_until_placement
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                               
                                    
        
                        del event_dict[next_event]
        
                    # ---------------------------------------------------------------
                    # -------------------------- CHECK TRW BEDS ---------------------
                    # --------------------------------------------------------------- 
                      
                    elif next_event[0:14] == 'check_TRW_beds': 
                     
                        if print_modus:
                            print('___________________________________________________')
                            print('>>> check_trw_beds <<<')
                            print('___________________________________________________')
                            
                        if count_patients('TRW_'+str(extract_number(target_client))) + count_place_reserved('TRW_'+str(extract_number(target_client))) <beds_TRW_list[extract_number(target_client)] :
                        
                            # iemand doorschuiven
                                
                            target_client_found = False
                            if priority:
                                if check_first_pref_client(w4_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:#len(w2_dict_TRW) > 0: # priority
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1], client_dict[client_3]['j_times'][-1])
                                    if min_of_wait == check_first_pref_client(w3_dict_TRW, extract_number(target_client)):
                                        target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
        #                             del wait_list_2_TRW[0]
        #                             del type_of_w2_trw[0]
                                        if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_'+target_client]
                                    else:
                                        target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w4_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:
                                    target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w3_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                    if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w2_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:#len(w3_dict_TRW) > 0:
                                    target_client = check_first_pref_client(w2_dict_TRW,extract_number(target_client)) #wait_list_3_TRW[0]   
                                    target_client_found = True
                                    remove_from_wait_list(w2_dict_TRW, target_client,current_time)
                                    #del wait_list_3_TRW[0]
                            else:
                                if check_first_pref_client(w2_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)) and check_first_pref_client(w4_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:#len(w3_dict)>0 and len(w2_dict)>0:
                                    client_2 = check_first_pref_client(w2_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1], client_dict[client_3]['j_times'][-1],client_dict[client_4]['j_times'][-1])
                                    if min_of_wait == client_dict[client_2]['j_times'][-1]:
                                        target_client = client_2
                                        target_client_found = True
                                        remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
        
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                    elif min_of_wait ==  client_dict[client_3]['j_times'][-1]:#45
                                        target_client = client_3 #wait_list_3[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)
                                        #del wait_list_3[0]
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                    else:
                                        target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w2_dict_TRW, extract_number(target_client)) and check_first_pref_client(w4_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:
                                    client_2 = check_first_pref_client(w2_dict_TRW, extract_number(target_client))
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1],client_dict[client_4]['j_times'][-1])
                                    if min_of_wait == client_dict[client_2]['j_times'][-1]:
                                        target_client = client_2
                                        target_client_found = True
                                        remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
                                    else:
                                        target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w2_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    client_2 = check_first_pref_client(w2_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1], client_dict[client_3]['j_times'][-1])
                                    if min_of_wait == client_dict[client_2]['j_times'][-1]:
                                        target_client = client_2
                                        target_client_found = True
                                        remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
                                    else:
                                        target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w4_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_4]['j_times'][-1], client_dict[client_3]['j_times'][-1])
                                    if min_of_wait == client_dict[client_4]['j_times'][-1]:
                                        target_client = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                    else:
                                        target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w3_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                    if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                        del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w2_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w2_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w4_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    target_client_found = True
                                    remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                            if print_modus:
                                    print('nieuwe klant gevonden voor bed trw is',target_client_found)
                                    if target_client_found:
                                        print('dit is', target_client)
                        
                            if target_client_found:
                                
                                move_to_TRW_High(target_client,  0)
                                       
                            else:
                                if print_modus:
                                    print('Niemand schuift door naar trw')       
        
                        del event_dict[next_event]
                    
                    # ---------------------------------------------------------------
                    # -------------------------- HOSPITAL ADMISSION -----------------
                    # --------------------------------------------------------------- 
                      
                    elif next_event[0:8] == 'HOSP_adm':
                     
                        if print_modus:
                            print('___________________________________________________')
                            print('>>> HOSP_adm <<<')
                            print('___________________________________________________')
                            
                        target_client = next_event[9:]
                        move_to_HOSP(target_client)
        
                        if print_modus:
                            print('client', target_client, 'gaat naar HOSPital')
                        
        
                        del event_dict[next_event]
                        
                        
                    # ---------------------------------------------------------
                    # ------------------------------------- TIMESTAMP ---------
                    # ---------------------------------------------------------
        
                    elif next_event[0:9] == 'timestamp': 
        
                        if next_event[10:] == 'arr_HOS_High':
                            
                            event_dict[next_event] = current_time + exp(arr_HOS_High)
                            empty_key_not_found = True
                            extra_str = ''
                            while empty_key_not_found:
                                if 'arr_HOS_High' + extra_str in event_dict.keys():
                                    extra_str += '_'
                                else:
                                    empty_key_not_found = False
                                    event_dict['arr_HOS_High' + extra_str] = event_dict[next_event]
                                    
                        elif next_event[10:] == 'arr_HOS_GRZ':
                            
                            event_dict[next_event] = current_time + exp(arr_HOS_GRZ)
                            empty_key_not_found = True
                            extra_str = ''
                            while empty_key_not_found:
                                if 'arr_HOS_GRZ' + extra_str in event_dict.keys():
                                    extra_str += '_'
                                else:
                                    empty_key_not_found = False
                                    event_dict['arr_HOS_GRZ' + extra_str] = event_dict[next_event]
                            
                        elif next_event[10:] == 'arr_GPR_High':
                            
                            event_dict[next_event] = current_time + exp(arr_GPR_High)
                            empty_key_not_found = True
                            extra_str = ''
                            while empty_key_not_found:
                                if 'arr_GPR_High' + extra_str in event_dict.keys():
                                    extra_str += '_'
                                else:
                                    empty_key_not_found = False
                                    event_name = 'arr_GPR_High' + extra_str
                                    event_dict[event_name] = event_dict[next_event]
                                    arrival_time = event_dict[event_name] - math.floor(event_dict[event_name])
                                    
                                    # check te vroeg of te laat?
        
                                    if arrival_time > GPR_end_time:
                                        # wordt verplaatst naar volgende dag
                                        event_dict[event_name] = math.ceil(event_dict[event_name]) + GPR_start_time + (arrival_time-GPR_end_time)
                                    elif arrival_time < GPR_start_time:
                                        # wordt verplaatst naar later op de dag
                                        event_dict[event_name] = math.floor(event_dict[event_name]) + GPR_start_time + (arrival_time+1-GPR_end_time)
                                        
                                    
                        elif next_event[10:] == 'arr_EMD':
                            
                            event_dict[next_event] = current_time + exp(arr_EMD)
                            empty_key_not_found = True
                            extra_str = ''
                            while empty_key_not_found:
                                if 'arr_EMD' + extra_str in event_dict.keys():
                                    extra_str += '_'
                                else:
                                    empty_key_not_found = False
                                    event_name = 'arr_EMD' + extra_str
                                    event_dict[event_name] = event_dict[next_event]
                                    arrival_time = event_dict[event_name] - math.floor(event_dict[event_name])
                                    if arrival_time > EMD_end_time:
                                        # wordt verplaatst naar volgende dag
                                        event_dict[event_name] = math.ceil(event_dict[event_name]) + EMD_start_time + (arrival_time-EMD_end_time)
                                    elif arrival_time < EMD_start_time:
                                        # wordt verplaatst naar later op de dag
                                        event_dict[event_name] = math.floor(event_dict[event_name]) + EMD_start_time + (arrival_time+1-EMD_end_time)
        
                        elif next_event[10:] == 'arr_GPR_Low':
                            
                            event_dict[next_event] = current_time + exp(arr_GPR_Low)
                            empty_key_not_found = True
                            extra_str = ''
                            while empty_key_not_found:
                                if 'arr_GPR_Low' + extra_str in event_dict.keys():
                                    extra_str += '_'
                                else:
                                    empty_key_not_found = False
                                    event_name = 'arr_GPR_Low' + extra_str
                                    event_dict[event_name] = event_dict[next_event]
                                    arrival_time = event_dict[event_name] - math.floor(event_dict[event_name])
                                    
                                    # check te vroeg of te laat?
        
                                    if arrival_time > GPR_end_time:
                                        # wordt verplaatst naar volgende dag
                                        event_dict[event_name] = math.ceil(event_dict[event_name]) + GPR_start_time + (arrival_time-GPR_end_time)
                                    elif arrival_time < GPR_start_time:
                                        # wordt verplaatst naar later op de dag
                                        event_dict[event_name] = math.floor(event_dict[event_name]) + GPR_start_time + (arrival_time+1-GPR_end_time)
                    # ---------------------------------------------------------------
                    # -------------------------- HOSPITAL DISCHARGE -----------------
                    # --------------------------------------------------------------- 
                      
                    elif next_event[0:14] == 'HOSP_discharge':
                    
                        if print_modus:
                            print('___________________________________________________')
                            print('>>> HOSP_discharge <<<')
                            print('___________________________________________________')
                            
                        target_client = next_event[15:]
                        if print_modus:
                            print('HOSP discharge of client', target_client)
                        
                        if Scen_tr_ward:
                            if target_client in w2_dict_TRW.items() or w3_dict_TRW.items() or w4_dict_TRW.items():    
                            
                        
                                if count_patients('TRW') + count_place_reserved('TRW') >= beds_TRW_list[extract_number(target_client)]: # op wachtlijst
                                    if target_client in w3_dict.items():
                                        remove_from_wait_list(w3_dict,target_client,current_time)
                                        add_to_waiting_dict(w3_dict_TRW,target_client,current_time)
                                    else:
                                        add_to_waiting_dict(w3_dict_TRW,target_client,current_time)
                                    if target_client in w4_dict.items():
                                        remove_from_wait_list(w4_dict,target_client,current_time)
                                        add_to_waiting_dict(w4_dict_TRW,target_client,current_time)
                                    else:
                                        add_to_waiting_dict(w4_dict_TRW,target_client,current_time)
                                    if target_client in w2_dict.items():
                                        remove_from_wait_list(w2_dict,target_client,current_time)
                                        add_to_waiting_dict(w2_dict_TRW,target_client,current_time)
                                    else:
                                        add_to_waiting_dict(w2_dict_TRW,target_client,current_time)
                                    #wait_list_3_TRW.append(target_client)
                                    
                                    if print_modus:
                                        print(target_client, 'gaat op wachtlijst voor TRW') 
                                
                                    client_dict[target_client]['journey'].append('wait_at_HOSP')#1
                                    client_dict[target_client]['j_times'].append(current_time)
                    
                                else: # kan direct door
                                    p_acc_opn = np.random.uniform(0,1)
                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                        # voor 17h en geen weekend of prob accept!
            
                                        time_until_placement = exp(adm_days)                
            
                                    else: #15
                                        if math.floor(current_time) % 7 in [6,0]: 
                                            # als weekend
                                            if math.floor(current_time) % 7 == 0:
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                            else:
                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                            if print_modus:
                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                            # als avond
                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                            if print_modus:
                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                    move_to_TRW_High(target_client,  time_until_placement) 
                                    
                            else:#45555
                                if sum(beds_TRW_list)>0:
                                    p_observation = np.random.uniform(0,1)
                                else: 
                                    p_observation = 1
                                if p_observation < 0.1:
                                    if count_patients('TRW') + count_place_reserved('TRW') >= beds_TRW_list[extract_number(target_client)]: # op wachtlijst
                                        if target_client in w3_dict.items():
                                            remove_from_wait_list(w3_dict,target_client,current_time)
                                            add_to_waiting_dict(w3_dict_TRW,target_client,current_time)
                                        else:
                                            add_to_waiting_dict(w3_dict_TRW,target_client,current_time)
                                        if target_client in w4_dict.items():
                                            remove_from_wait_list(w4_dict,target_client,current_time)
                                            add_to_waiting_dict(w4_dict_TRW,target_client,current_time)
                                        else:
                                            add_to_waiting_dict(w4_dict_TRW,target_client,current_time)
                                        if target_client in w2_dict.items():
                                            remove_from_wait_list(w2_dict,target_client,current_time)
                                            add_to_waiting_dict(w2_dict_TRW,target_client,current_time)
                                        else:
                                            add_to_waiting_dict(w2_dict_TRW,target_client,current_time)
                                        #wait_list_3_TRW.append(target_client)
                                        
                                        if print_modus:
                                            print(target_client, 'gaat op wachtlijst voor TRW') 
                                    
                                        client_dict[target_client]['journey'].append('wait_at_HOSP')#1
                                        client_dict[target_client]['j_times'].append(current_time)
                    
                                    else: # kan direct door
                                        p_acc_opn = np.random.uniform(0,1)
                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                            # voor 17h en geen weekend of prob accept!
                
                                            time_until_placement = exp(adm_days)                
                
                                        else: #15
                                            if math.floor(current_time) % 7 in [6,0]: 
                                                # als weekend
                                                if math.floor(current_time) % 7 == 0:
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                else:
                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                
                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                # als avond
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                
                                        move_to_TRW_High(target_client,  time_until_placement) 
                                else:#aanpassen
                                    
                                    if sum(n_beds_shared_High_list)==0:
                                        if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:
                                            if Check_space_partial_beds('HOS_High') >= n_beds_High_Complex_list[extract_number(target_client)]: #Waiting list
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#gg
                                                        if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:#1
                                                               
                                                            add_to_waiting_dict(w3_dict,target_client,current_time)
                                                    #wait_list_3.append(target_client)
                                                        
                    
                                                        if print_modus:
                                                            print(target_client, 'gaat op wachtlijst') 
                    
                                                        client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                                        client_dict[target_client]['j_times'].append(current_time)
                                                elif Preference == 'Pref' or Preference == 'NO':
                                                    if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD'in client_dict[target_client]['journey']:#1
                                                               
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
                                                    #wait_list_3.append(target_client)
                                                    
                
                                                    if print_modus:
                                                        print(target_client, 'gaat op wachtlijst') 
                
                                                    client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                                    client_dict[target_client]['j_times'].append(current_time)
                
                                            else: # kan direct door
                
                                                if print_modus:
                                                    print(target_client, 'gaat direct naar ELV_High') 
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
                        
                                                    time_until_placement = exp(adm_days)                
                        
                                                else: #15
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                        
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                
                #                               
                
                                                move_to_ELV_High(target_client, time_until_placement)
                                        elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                                            if Check_space_partial_beds('HOS_GRZ') >= n_beds_GRZ_list[extract_number(target_client)]: #Waiting list
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:#22
                                                        add_to_waiting_dict(w4_dict,target_client,current_time)
                                                        #wait_list_3.append(target_client)
                                                        if print_modus:
                                                            print(target_client, 'gaat op wachtlijst') 
                
                                                        client_dict[target_client]['journey'].append('wait_at_HOSP')#4
                                                        client_dict[target_client]['j_times'].append(current_time)
                                                elif Preference == 'NO' or Preference == 'Pref':
                                                    add_to_waiting_dict(w4_dict,target_client,current_time)
                                                    #wait_list_3.append(target_client)
                                                    if print_modus:
                                                        print(target_client, 'gaat op wachtlijst') 
                
                                                    client_dict[target_client]['journey'].append('wait_at_HOSP')#4
                                                    client_dict[target_client]['j_times'].append(current_time)
                                            else: # kan direct door
                
                                                if print_modus:
                                                    print(target_client, 'gaat direct naar ELV_High') 
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
                        
                                                    time_until_placement = exp(adm_days)                
                        
                                                else: #15
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                        
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                                move_to_ELV_High(target_client, time_until_placement)
                                    
                                    
                            
                        else:#No triage ward
                            if Scen_shared_beds_Full:
                                if count_patients('ELV_High') + count_place_reserved('ELV_High') >= n_beds_ELV_High_list[extract_number(target_client)]: # Full System
                                    if Preference == 'FCFS':
                                        if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                            change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                    
                                                time_until_placement = exp(adm_days)                
                    
                                            else: #15
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                    
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                    
                                            # move to ELV vanaf time_until_placement
                                            move_to_ELV_High(target_client,time_until_placement)
                                            
                                        else: #waiting list
                                            if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:#1
                                                       
                                                add_to_waiting_dict(w3_dict,target_client,current_time)
                                            #wait_list_3.append(target_client)
                                            elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                                                add_to_waiting_dict(w4_dict,target_client,current_time)
        
                                            if print_modus:
                                                print(target_client, 'gaat op wachtlijst') 
        
                                            client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                            client_dict[target_client]['j_times'].append(current_time)
                                    elif Preference == 'Pref' or Preference == 'NO':
                                        if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD'in client_dict[target_client]['journey']:#1
                                                       
                                            add_to_waiting_dict(w3_dict,target_client,current_time)
                                        #wait_list_3.append(target_client)
                                        elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                                            add_to_waiting_dict(w4_dict,target_client,current_time)
        
                                        if print_modus:
                                            print(target_client, 'gaat op wachtlijst') 
        
                                        client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                        client_dict[target_client]['j_times'].append(current_time)
        
                                else: # kan direct door
        
                                    if print_modus:
                                        print(target_client, 'gaat direct naar ELV_High') 
                                    p_acc_opn = np.random.uniform(0,1)
                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                        # voor 17h en geen weekend of prob accept!
            
                                        time_until_placement = exp(adm_days)                
            
                                    else: #15
                                        if math.floor(current_time) % 7 in [6,0]: 
                                            # als weekend
                                            if math.floor(current_time) % 7 == 0:
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                            else:
                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                            if print_modus:
                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                            # als avond
                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                            if print_modus:
                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
        
                                    move_to_ELV_High(target_client, time_until_placement)
        
                            elif Scen_part_bed_Share or Scen_NO_Sharing:
                                if sum(n_beds_shared_High_list)==0:
                                    if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_High') >= n_beds_High_Complex_list[extract_number(target_client)]: #Waiting list
                                            if Preference == 'FCFS':
                                                if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                    change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                        # voor 17h en geen weekend of prob accept!
                            
                                                        time_until_placement = exp(adm_days)                
                            
                                                    else: #15
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                    move_to_ELV_High(target_client,time_until_placement)
                                                else:#gg
                                                    if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:#1
                                                           
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
                                                #wait_list_3.append(target_client)
                                                    
                
                                                    if print_modus:
                                                        print(target_client, 'gaat op wachtlijst') 
                
                                                    client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                                    client_dict[target_client]['j_times'].append(current_time)
                                            elif Preference == 'Pref' or Preference == 'NO':
                                                if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD'in client_dict[target_client]['journey']:#1
                                                           
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
                                                #wait_list_3.append(target_client)
                                                
            
                                                if print_modus:
                                                    print(target_client, 'gaat op wachtlijst') 
            
                                                client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                                client_dict[target_client]['j_times'].append(current_time)
            
                                        else: # kan direct door
            
                                            if print_modus:
                                                print(target_client, 'gaat direct naar ELV_High') 
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                    
                                                time_until_placement = exp(adm_days)                
                    
                                            else: #15
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                    
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
            #                               
            
                                            move_to_ELV_High(target_client, time_until_placement)
                                    elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_GRZ') >= n_beds_GRZ_list[extract_number(target_client)]: #Waiting list
                                            if Preference == 'FCFS':
                                                if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                    change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                    p_acc_opn = np.random.uniform(0,1)
                                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                        # voor 17h en geen weekend of prob accept!
                            
                                                        time_until_placement = exp(adm_days)                
                            
                                                    else: #15
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                            
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                            
                                                            if print_modus:
                                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                            
                                                    # move to ELV vanaf time_until_placement
                                                    move_to_ELV_High(target_client,time_until_placement)
                                                else:#22
                                                    add_to_waiting_dict(w4_dict,target_client,current_time)
                                                    #wait_list_3.append(target_client)
                                                    if print_modus:
                                                        print(target_client, 'gaat op wachtlijst') 
            
                                                    client_dict[target_client]['journey'].append('wait_at_HOSP')#4
                                                    client_dict[target_client]['j_times'].append(current_time)
                                            elif Preference == 'NO' or Preference == 'Pref':
                                                add_to_waiting_dict(w4_dict,target_client,current_time)
                                                #wait_list_3.append(target_client)
                                                if print_modus:
                                                    print(target_client, 'gaat op wachtlijst') 
            
                                                client_dict[target_client]['journey'].append('wait_at_HOSP')#4
                                                client_dict[target_client]['j_times'].append(current_time)
                                        else: # kan direct door
            
                                            if print_modus:
                                                print(target_client, 'gaat direct naar ELV_High') 
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                    
                                                time_until_placement = exp(adm_days)                
                    
                                            else: #15
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                    
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                            move_to_ELV_High(target_client, time_until_placement)
                                elif sum(n_beds_shared_High_list)>0:
                                    if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_High') >= n_beds_High_Complex_list[extract_number(target_client)]: #Waiting list
                                            
                                            if count_patients('ELV_part')+ count_place_reserved('ELV_part')<n_beds_shared_High_list[extract_number(target_client)]:
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
                        
                                                    time_until_placement = exp(adm_days)                
                        
                                                else: #15
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                        
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                move_to_ELV_partial_bed(target_client, time_until_placement)
                                            else: #45
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:
                                                        add_to_waiting_dict(w3_dict,target_client,current_time)
                                                        #wait_list_3.append(target_client)
                                                        if print_modus:
                                                            print(target_client, 'gaat op wachtlijst') 
                
                                                        client_dict[target_client]['journey'].append('wait_at_HOSP')#3
                                                        client_dict[target_client]['j_times'].append(current_time)
                                                elif Preference == 'Pref' or Preference == 'NO':
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
                                                    #wait_list_3.append(target_client)
                                                    if print_modus:
                                                        print(target_client, 'gaat op wachtlijst') 
            
                                                    client_dict[target_client]['journey'].append('wait_at_HOSP')#3
                                                    client_dict[target_client]['j_times'].append(current_time)
                                        else: # kan direct door
            
                                            if print_modus:
                                                print(target_client, 'gaat direct naar ELV_High') 
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                    
                                                time_until_placement = exp(adm_days)                
                    
                                            else: #15
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                    
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                            move_to_ELV_High(target_client, time_until_placement)  
                                            # print('break 7')
                                            # print(target_client)
                                            # break
                                    elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                                        if Check_space_partial_beds('HOS_GRZ') >= n_beds_High_Complex_list[extract_number(target_client)]: #Waiting list
                                            
                                            if count_patients('ELV_part')+ count_place_reserved('ELV_part')<n_beds_shared_High_list[extract_number(target_client)]:
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
                        
                                                    time_until_placement = exp(adm_days)                
                        
                                                else: #15
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                        
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                move_to_ELV_partial_bed(target_client, time_until_placement)
                                            else: #455
                                                if Preference == 'FCFS':
                                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                        p_acc_opn = np.random.uniform(0,1)
                                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                            # voor 17h en geen weekend of prob accept!
                                
                                                            time_until_placement = exp(adm_days)                
                                
                                                        else: #15
                                                            if math.floor(current_time) % 7 in [6,0]: 
                                                                # als weekend
                                                                if math.floor(current_time) % 7 == 0:
                                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                                else:
                                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                                
                                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                                # als avond
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                
                                                                if print_modus:
                                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                
                                                        # move to ELV vanaf time_until_placement
                                                        move_to_ELV_High(target_client,time_until_placement)
                                                    else:
                                                        add_to_waiting_dict(w4_dict,target_client,current_time)
                                                        #wait_list_3.append(target_client)
                                                        if print_modus:
                                                            print(target_client, 'gaat op wachtlijst') 
                
                                                        client_dict[target_client]['journey'].append('wait_at_HOSP')#3
                                                        client_dict[target_client]['j_times'].append(current_time)
                                                elif Preference == 'Pref' or Preference == 'NO':
                                                    add_to_waiting_dict(w4_dict,target_client,current_time)
                                                    #wait_list_3.append(target_client)
                                                    if print_modus:
                                                        print(target_client, 'gaat op wachtlijst') 
                
                                                    client_dict[target_client]['journey'].append('wait_at_HOSP')#3
                                                    client_dict[target_client]['j_times'].append(current_time)
                                            
                                                
                                        else: # kan direct door
            
                                            if print_modus:
                                                print(target_client, 'gaat direct naar ELV_High') 
                                            p_acc_opn = np.random.uniform(0,1)
                                            if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                # voor 17h en geen weekend of prob accept!
                    
                                                time_until_placement = exp(adm_days)                
                    
                                            else: #15
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                    
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                    
                                                    if print_modus:
                                                        print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                            move_to_ELV_High(target_client, time_until_placement)
                                            # print('break 6')
                                            # print(target_client)
                                            # break
            
            
                                    
                                    
                            elif Scen_Total_Sharing:
                                if count_patients('ELV_TOT')+ count_place_reserved('ELV_TOT')<n_beds_ELV_total_list[extract_number(target_client)]:
                                    p_acc_opn = np.random.uniform(0,1)
                                    if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                        # voor 17h en geen weekend of prob accept!
            
                                        time_until_placement = exp(adm_days)                
            
                                    else: #15
                                        if math.floor(current_time) % 7 in [6,0]: 
                                            # als weekend
                                            if math.floor(current_time) % 7 == 0:
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                            else:
                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                            if print_modus:
                                                print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
            
                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                            # als avond
                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
            
                                            if print_modus:
                                                print('het is avond dus plaatsing naar ELV over', time_until_placement) 
            
                                    # move to ELV vanaf time_until_placement
                                        
                                    move_to_ELV_Total(target_client, time_until_placement)
                                elif Preference == 'FCFS':
                                    if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                        change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                        p_acc_opn = np.random.uniform(0,1)
                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                            # voor 17h en geen weekend of prob accept!
                
                                            time_until_placement = exp(adm_days)                
                
                                        else: #15
                                            if math.floor(current_time) % 7 in [6,0]: 
                                                # als weekend
                                                if math.floor(current_time) % 7 == 0:
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                else:
                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                
                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                # als avond
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                
                                        # move to ELV vanaf time_until_placement
                                        move_to_ELV_Total(target_client,time_until_placement)
                                    else:
                                        if any(item in client_dict[target_client]['journey'] for item in ['HOS_GRZ' , 'HOS_High' , 'EMD']):#'HOS_GRZ' or 'HOS_High' or 'EMD' in client_dict[target_client]['journey']:
                                            client_dict[target_client]['journey'].append('wait_at_HOSP')#8
                                            client_dict[target_client]['j_times'].append(current_time)
            
                                        
                                            add_to_waiting_dict(w_tot_dict,target_client,current_time)
        
                                elif Preference == 'NO' or Preference == 'Pref':
                                    if any(item in client_dict[target_client]['journey'] for item in ['HOS_GRZ' , 'HOS_High' , 'EMD']):#'HOS_GRZ' or 'HOS_High' or 'EMD' in client_dict[target_client]['journey']:
                                        client_dict[target_client]['journey'].append('wait_at_HOSP')#8
                                        client_dict[target_client]['j_times'].append(current_time)
         
                                    
                                        add_to_waiting_dict(w_tot_dict,target_client,current_time)
        
                                    
                        del event_dict[next_event]
                      
                    # ---------------------------------------------------------------
                    # -----------------------------------CHECK BEZETTING ------------
                    # ---------------------------------------------------------------
        
                    elif next_event[0:9] == 'check_bez':
                        if print_modus:
                            print('___________________________________________________')
                            print('>>> check_bez <<<')
                            print('___________________________________________________')
                            
                        if n_client > n_clients_for_warming:
                            
         
                            
                            # check bezettingsgraad
                            cur_nr_ELV_Tot = 0
                            
                            for i in range(n_loc):
                                cur_nr_ELV_Tot+= count_patients('ELV_High_'+str(i)) + count_patients('ELV_Low_'+str(i)) +count_patients('ELV_part_'+str(i)) +count_patients('ELV_TOT_'+str(i)) +count_patients('ELV_EMDR_'+str(i))
                                abs_aanw_list.append(cur_nr_ELV_Tot)
                                if Scen_shared_beds_Full:
                                    if (cur_nr_ELV_Tot/(sum(n_beds_ELV_High_list) + sum(n_beds_ELV_Low_list) +sum(beds_Emergency_list)))>1:
                                        bez_gr_list_Total.append(1)
                                    else:
                                        bez_gr_list_Total.append((cur_nr_ELV_Tot/(sum(n_beds_ELV_High_list) + sum(n_beds_ELV_Low_list) +sum(beds_Emergency_list))))
                                elif Scen_NO_Sharing:#4
                                    if (cur_nr_ELV_Tot/(sum(n_beds_High_Complex_list)+sum(n_beds_GRZ_list) + sum((n_beds_ELV_Low_list))+sum(beds_Emergency_list)))>1:
                                        bez_gr_list_Total.append(1)
                                    else:
                                        bez_gr_list_Total.append((cur_nr_ELV_Tot/(sum(n_beds_High_Complex_list)+sum(n_beds_GRZ_list) + sum((n_beds_ELV_Low_list))+sum(beds_Emergency_list))))
                                elif Scen_part_bed_Share:
                                    if cur_nr_ELV_Tot/(sum(n_beds_High_Complex_list)+sum(n_beds_GRZ_list)+sum(n_beds_shared_High_list)+ sum(n_beds_ELV_Low_list)+sum(beds_Emergency_list))>1:
                                        bez_gr_list_Total.append(1)
                                    else: 
                                        bez_gr_list_Total.append(cur_nr_ELV_Tot/(sum(n_beds_High_Complex_list)+sum(n_beds_GRZ_list)+sum(n_beds_shared_High_list)+ sum(n_beds_ELV_Low_list)+sum(beds_Emergency_list)))
                                elif Scen_Total_Sharing:
                                    if cur_nr_ELV_Tot/(sum(n_beds_ELV_total_list))>1:
                                        bez_gr_list_Total.append(1)
                                    else:
                                        bez_gr_list_Total.append(cur_nr_ELV_Tot/(sum(n_beds_ELV_total_list)))
                            
                            # check bezettingsgraad
                            cur_nr_ELV_High =0
                            cur_nr_ELV_Total = 0
                            for i in range(n_loc):
                                cur_nr_ELV_High += count_patients('ELV_High_'+str(i)) +count_patients('ELV_part_'+str(i)) +count_patients('ELV_EMDR_'+str(i))
                                abs_aanw_High_list.append(cur_nr_ELV_High)
                            if Scen_Total_Sharing!= True and sum(n_beds_ELV_High_list) >0:
                                bz_gr = cur_nr_ELV_High/sum(n_beds_ELV_High_list)
                                if bz_gr >1:
                                    bz_gr = 1
                                else:
                                    bz_gr = cur_nr_ELV_High/sum(n_beds_ELV_High_list)
                                if Scen_shared_beds_Full:
                                    bez_gr_list_High.append(bz_gr)
                                elif Scen_NO_Sharing:#5
                                    bez_gr_list_High.append(bz_gr)
                                elif Scen_part_bed_Share:
                                    bez_gr_list_High.append(bz_gr)
                                abs_aanw_High_list.append(cur_nr_ELV_High)
        
                            
                            if Scen_Total_Sharing != True:
                                if sum(n_beds_ELV_Low_list)>0:
                                    # check bezettingsgraad
                                    cur_nr_ELV_Low=0
                                    for i in range(n_loc):
                                        cur_nr_ELV_Low += count_patients('ELV_Low')
                                    bez_gr_Low_list.append((cur_nr_ELV_Low/sum(n_beds_ELV_Low_list)))
                                    abs_aanw_Low_list.append(cur_nr_ELV_Low)
        
                            cur_nr_EMDR = 0
                            if sum(beds_Emergency_list)>0:
                                for loc in range(n_loc):
                                    cur_nr_EMDR += count_patients('ELV_EMDR_'+str(loc))
                                bez_gr_EMDR_list.append(cur_nr_EMDR/sum(beds_Emergency_list))
                            
                                
                            #bezettingsgraad TRW
                            if Scen_tr_ward:
                                for loc in range(n_loc):
                                    cur_nr_TRW += count_patients('TRW_'+str(loc))
                                if sum(beds_TRW_list)>0:
                                    bez_gr_TRW_list.append(cur_nr_TRW/sum(beds_TRW_list))
                                abs_aanw_TRW_list.append(cur_nr_TRW) 
                            else:#49
                                cur_nr_TRW = 0
                                bez_gr_TRW_list.append(0)
                                abs_aanw_TRW_list.append(0)
                            # check wachtlijstaantal
                            if Scen_tr_ward:
                                len_w3_list.append(len(w3_dict))
                                len_w2_list.append(len(w2_dict))
                                len_w1_list.append(len(w1_dict))
                                len_w4_list.append(len(w4_dict))
                            else:
                                len_w4_list.append(len(w4_dict))
                                len_w3_list.append(len(w3_dict))
            #                     len_w2_EMD_list.append(type_of_w2.count('EMD'))
            #                     len_w2_GPR_High_list.append(type_of_w2.count('GPR_High'))
                                len_w2_list.append(len(w2_dict))
                                len_w1_list.append(len(w1_dict))
                            len_w_total_list.append(len(w_tot_dict))
                    
                        event_dict['check_bez'] += 1
                        
                    # ---------------------------------------------------------------
                    # ------------------------------------------- TRW DISCHARGE ---------
                    # ---------------------------------------------------------------
        
                    elif next_event[0:13] == 'TRW_discharge':
                        
                        if print_modus:
                            print('___________________________________________________')
                            print('>>> trw discharge <<<')
                            print('___________________________________________________')
                            print('discharge of', next_event[14:])
                            print('current_time', current_time)
        
                        target_client = next_event[14:]
                        prev = target_client
                        
                        Previous_Client = client_dict[prev]['journey']
                        curr_loc = client_dict[target_client]['current_loc']
        
                        if client_dict[target_client]['to_ELV_High']:
                            target_loc = 'ELV_High'
                          
                        else:#48
                            target_loc = client_dict[target_client]['TRW_discharge_dest']
                        
                        if target_loc != 'ELV_High': # diegene gaat dus na trw naar huis
        
                            client_dict[target_client]['journey'].append(target_loc)
                            client_dict[target_client]['j_times'].append(current_time)
                            
                            if n_client > n_clients_for_warming:
                                n_evaluated += 1
                                n_evaluated_current_run += 1
                            
                                # output measures bepalen
                                
                                client_output_temp = {target_client: {
                                   'journey': client_dict[target_client]['journey'],
                                   'j_times': client_dict[target_client]['j_times'],
                                   }
                                }
                            
                                output_dict.update(client_output_temp)
                                
                                if print_modus:
                                    print(client_output_temp)
                                
                            #del client_dict[target_client]
                            
                            # iemand anders doorschuiven
                            
                            target_client_found = False
                            if priority:
                                if check_first_pref_client(w4_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:#len(w2_dict_TRW) > 0: # priority
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1], client_dict[client_3]['j_times'][-1])
                                    if min_of_wait == check_first_pref_client(w3_dict_TRW, extract_number(target_client)):
                                        target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
        #                             del wait_list_2_TRW[0]
        #                             del type_of_w2_trw[0]
                                        if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_'+target_client]
                                    else:
                                        target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w4_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:
                                    target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w3_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                    if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w2_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:#len(w3_dict_TRW) > 0:
                                    target_client = check_first_pref_client(w2_dict_TRW,extract_number(target_client)) #wait_list_3_TRW[0]   
                                    target_client_found = True
                                    remove_from_wait_list(w2_dict_TRW, target_client,current_time)
                                    #del wait_list_3_TRW[0]
                            else:
                                if check_first_pref_client(w2_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)) and check_first_pref_client(w4_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:#len(w3_dict)>0 and len(w2_dict)>0:
                                    client_2 = check_first_pref_client(w2_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1], client_dict[client_3]['j_times'][-1],client_dict[client_4]['j_times'][-1])
                                    if min_of_wait == client_dict[client_2]['j_times'][-1]:
                                        target_client = client_2
                                        target_client_found = True
                                        remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
        
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                    elif min_of_wait ==  client_dict[client_3]['j_times'][-1]:#45
                                        target_client = client_3 #wait_list_3[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)
                                        #del wait_list_3[0]
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                    else:
                                        target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w2_dict_TRW, extract_number(target_client)) and check_first_pref_client(w4_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))>0:
                                    client_2 = check_first_pref_client(w2_dict_TRW, extract_number(target_client))
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1],client_dict[client_4]['j_times'][-1])
                                    if min_of_wait == client_dict[client_2]['j_times'][-1]:
                                        target_client = client_2
                                        target_client_found = True
                                        remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
                                    else:
                                        target_client = check_first_pref_client(w4_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w2_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    client_2 = check_first_pref_client(w2_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_2]['j_times'][-1], client_dict[client_3]['j_times'][-1])
                                    if min_of_wait == client_dict[client_2]['j_times'][-1]:
                                        target_client = client_2
                                        target_client_found = True
                                        remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
                                    else:
                                        target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w4_dict_TRW, extract_number(target_client)) and check_first_pref_client(w3_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    client_4 = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    client_3 = check_first_pref_client(w3_dict_TRW, extract_number(target_client))
                                    min_of_wait = min(client_dict[client_4]['j_times'][-1], client_dict[client_3]['j_times'][-1])
                                    if min_of_wait == client_dict[client_4]['j_times'][-1]:
                                        target_client = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                        target_client_found = True
                                        remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                                    else:
                                        target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                        target_client_found = True
                                        remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                        if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                            del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w3_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w3_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                                    if (client_dict[target_client]['journey'][0] == 'EMD' or client_dict[target_client]['journey'][0] == 'GPR_High')   and 'HOSP_adm_' +target_client in event_dict:#3
                                        del event_dict['HOSP_adm_' + target_client]
                                elif check_first_pref_client(w2_dict_TRW,extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w2_dict_TRW,extract_number(target_client)) #w2_dict_TRW[0]
                                    target_client_found = True
                                    remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
                                elif check_first_pref_client(w4_dict_TRW, extract_number(target_client)):#len(list({k:v['Preferred location']  for (k,v) in w4_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))>0 and len(list({k:v['Preferred location']  for (k,v) in w2_dict_TRW.items()if v['Preferred location']==extract_number(prev)}.values()))==0 and len(list({k:v['Preferred location']  for (k,v) in w3_dict_TRW.items()if v['Preferred location']==extract_number(target_client)}.values()))==0:
                                    target_client = check_first_pref_client(w4_dict_TRW, extract_number(target_client))
                                    target_client_found = True
                                    remove_from_wait_list(w4_dict_TRW,target_client,current_time,Fairness_list)
                            if print_modus:
                                    print('nieuwe klant gevonden voor bed trw is',target_client_found)
                                    if target_client_found:
                                        print('dit is', target_client)
                        
                            if target_client_found:
                                
                                move_to_TRW_High(target_client,  0)
                                        
                        elif target_loc == 'ELV_High':# na trw volgt een elv opname
                        
                           # doorplaatsen als mogelijk
                                       
                            client_dict[target_client]['journey'].append('TRW_discharge')
                            client_dict[target_client]['j_times'].append(current_time)
                        
        
                            if sum(n_beds_shared_High_list)==0:
                                if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:
                                    if Check_space_partial_beds('HOS_High') >= n_beds_High_Complex_list[extract_number(target_client)]: #Waiting list
                                        if Preference == 'FCFS':
                                            if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
                        
                                                    time_until_placement = exp(adm_days)                
                        
                                                else: #15
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                        
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                move_to_ELV_High_from_TRW(target_client,time_until_placement)
                                            else:#gg
                                                if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD' in client_dict[target_client]['journey']:#1
                                                       
                                                    add_to_waiting_dict(w3_dict,target_client,current_time)
                                            #wait_list_3.append(target_client)
                                                
            
                                                if print_modus:
                                                    print(target_client, 'gaat op wachtlijst') 
            
                                                client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                                client_dict[target_client]['j_times'].append(current_time)
                                        elif Preference == 'Pref' or Preference == 'NO':
                                            if 'HOS_High' in client_dict[target_client]['journey'] or 'EMD'in client_dict[target_client]['journey']:#1
                                                       
                                                add_to_waiting_dict(w3_dict,target_client,current_time)
                                            #wait_list_3.append(target_client)
                                            
        
                                            if print_modus:
                                                print(target_client, 'gaat op wachtlijst') 
        
                                            client_dict[target_client]['journey'].append('wait_at_HOSP')#2
                                            client_dict[target_client]['j_times'].append(current_time)
        
                                    else: # kan direct door
        
                                        if print_modus:
                                            print(target_client, 'gaat direct naar ELV_High') 
                                        p_acc_opn = np.random.uniform(0,1)
                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                            # voor 17h en geen weekend of prob accept!
                
                                            time_until_placement = exp(adm_days)                
                
                                        else: #15
                                            if math.floor(current_time) % 7 in [6,0]: 
                                                # als weekend
                                                if math.floor(current_time) % 7 == 0:
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                else:
                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                
                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                # als avond
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
        
        #                               
        
                                        move_to_ELV_High_from_TRW(target_client, time_until_placement)
                                elif 'HOS_GRZ' in client_dict[target_client]['journey']:
                                    if Check_space_partial_beds('HOS_GRZ') >= n_beds_GRZ_list[extract_number(target_client)]: #Waiting list
                                        if Preference == 'FCFS':
                                            if Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[0] == True:
                                                change_target_client_location(target_client,Check_beds_free_other_location(extract_number(target_client),n_loc,target_client,False)[1],True)
                                                p_acc_opn = np.random.uniform(0,1)
                                                if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                                    # voor 17h en geen weekend of prob accept!
                        
                                                    time_until_placement = exp(adm_days)                
                        
                                                else: #15
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                        
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                        
                                                        if print_modus:
                                                            print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                        
                                                # move to ELV vanaf time_until_placement
                                                move_to_ELV_High_from_TRW(target_client,time_until_placement)
                                            else:#22
                                                add_to_waiting_dict(w4_dict,target_client,current_time)
                                                #wait_list_3.append(target_client)
                                                if print_modus:
                                                    print(target_client, 'gaat op wachtlijst') 
        
                                                client_dict[target_client]['journey'].append('wait_at_HOSP')#4
                                                client_dict[target_client]['j_times'].append(current_time)
                                        elif Preference == 'NO' or Preference == 'Pref':
                                            add_to_waiting_dict(w4_dict,target_client,current_time)
                                            #wait_list_3.append(target_client)
                                            if print_modus:
                                                print(target_client, 'gaat op wachtlijst') 
        
                                            client_dict[target_client]['journey'].append('wait_at_HOSP')#4
                                            client_dict[target_client]['j_times'].append(current_time)
                                    else: # kan direct door
        
                                        if print_modus:
                                            print(target_client, 'gaat direct naar ELV_High') 
                                        p_acc_opn = np.random.uniform(0,1)
                                        if (current_time - math.floor(current_time) <= time_max_opn_ELV and math.floor(current_time) % 7 in [1,2,3,4,5]and current_time-math.floor(current_time)>=ELV_start_time) or p_acc_opn <= p_opn_weekend: 
                                            # voor 17h en geen weekend of prob accept!
                
                                            time_until_placement = exp(adm_days)                
                
                                        else: #15
                                            if math.floor(current_time) % 7 in [6,0]: 
                                                # als weekend
                                                if math.floor(current_time) % 7 == 0:
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                                                else:
                                                    time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is weekend dus plaatsing naar ELV over', time_until_placement) 
                
                                            elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                # als avond
                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)
                
                                                if print_modus:
                                                    print('het is avond dus plaatsing naar ELV over', time_until_placement) 
                                        move_to_ELV_High_from_TRW(target_client, time_until_placement)
                            
                        del event_dict[next_event]
                        
        
                    # ---------------------------------------------------------------
                    # ------------------------------------------- DISCHARGE ---------
                    # ---------------------------------------------------------------
        
        
                    elif next_event[0:9] == 'discharge':
                        
                        if print_modus:
                            print('___________________________________________________')
                            print('>>> discharge <<<')
                            print('___________________________________________________')
                            print('discharge of', next_event[10:])
                            print('current_time', current_time)
                        target_client = next_event[10:]
                        if 'HOSP_adm_'+target_client in event_dict:
                            del event_dict['HOSP_adm_'+target_client]
                        if (target_client in w1_dict.keys() and target_client in output_dict.keys()) or target_client in w1_dict.keys():
                                remove_from_wait_list(w1_dict,target_client,current_time,Fairness_list)
                        elif (target_client in w2_dict.keys() and target_client in output_dict.keys()) or target_client in w2_dict.keys():
                            remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
                   
                        elif (target_client in w2_dict_TRW.keys() and target_client in output_dict.keys()) or target_client in w2_dict_TRW.keys():
                            remove_from_wait_list(w2_dict_TRW,target_client,current_time,Fairness_list)
                    
                        elif (target_client in w3_dict.keys() and target_client in output_dict.keys()) or target_client in w3_dict.keys():
                            remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                        elif (target_client in w4_dict.keys() and target_client in output_dict.keys()) or target_client in w4_dict.keys():
                            remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
                        elif (target_client in w3_dict_TRW.keys() and target_client in output_dict.keys()) or target_client in w3_dict_TRW.keys():
                            remove_from_wait_list(w3_dict_TRW,target_client,current_time,Fairness_list)
                        elif target_client in w_tot_dict:
                            remove_from_wait_list(w_tot_dict,target_client,current_time,Fairness_list)
                        if 'HOSP_adm_'+target_client in event_dict:
                            del event_dict['HOSP_adm_'+target_client] 
                        if 'HOSP_discharge_'+target_client in event_dict and 'HOSP_adm' in client_dict[target_client]['journey']:
                            del event_dict['HOSP_discharge_'+target_client]
                        if 'ELV_EMDR_'+str(extract_number(target_client)) in client_dict[target_client]['journey']:
                            if target_client in w3_dict.keys():
                                remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                                                      
                            prev = target_client
                            client_dict[target_client]['journey'].append(target_loc)
                            client_dict[target_client]['j_times'].append(current_time)
        
                            if n_client > n_clients_for_warming:
                                n_evaluated += 1
                                n_evaluated_current_run += 1
        
                                # output measures bepalen
        
                                client_output_temp = {target_client: {
                                   'journey': client_dict[target_client]['journey'],
                                   'j_times': client_dict[target_client]['j_times'],
                                   }
                                }
        
                                output_dict.update(client_output_temp)
                            if print_modus:
                                print('niemand elv')
                                
                        else:
        
                            target_client = next_event[10:]
                            prev = target_client
                            Previous_Client = client_dict[prev]['journey']
                            curr_loc = client_dict[target_client]['current_loc']
                            target_loc = client_dict[target_client]['discharge_dest']
        
                            if Scen_Total_Sharing:
                                client_dict[target_client]['journey'].append(target_loc)
                                client_dict[target_client]['j_times'].append(current_time)
        
                                if n_client > n_clients_for_warming:
                                    n_evaluated += 1
                                    n_evaluated_current_run += 1
        
                                    # output measures bepalen
        
                                    client_output_temp = {target_client: {
                                       'journey': client_dict[target_client]['journey'],
                                       'j_times': client_dict[target_client]['j_times'],
                                       }
                                    }
        
                                    output_dict.update(client_output_temp)
        
                                    if print_modus:
                                        print(client_output_temp)
        
        
        
                                target_client_found = False
                                if count_patients('ELV_TOT') + count_place_reserved('ELV_TOT') < n_beds_ELV_total_list[extract_number(prev)]:
                                    if check_first_pref_client(w_tot_dict, extract_number(prev)):#len(list({k:v['Preferred location']  for (k,v) in w_tot_dict.items()if v['Preferred location']==extract_number(prev)}.values()))>0:#len(w_tot_dict)>0:
                                        target_client_found = True
                                        target_client = check_first_pref_client(w_tot_dict, extract_number(prev))
                                        if target_client_found:
                                            p_acc_opn = np.random.uniform(0,1)
            
                                            # als geen weekend of geen avond of p_acc_opn door toeval
                                            if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time )or p_acc_opn <= p_opn_weekend:
            
                                                time_until_placement = exp(adm_days) 
            
                                            else:#48
            
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
            
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
            
                                                    if print_modus:
                                                            print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
            
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
            
                                                    if print_modus:
                                                        print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
            
            
                                            move_to_ELV_Total(target_client, time_until_placement)
                                    else:
                                        if print_modus:
                                            print('niemand schuift door')
                            elif  Scen_shared_beds_Full or Scen_part_bed_Share or Scen_NO_Sharing or Scen_tr_ward:
                                if 'GPR_Low' in Previous_Client:
                                    client_dict[target_client]['journey'].append(target_loc)
                                    client_dict[target_client]['j_times'].append(current_time)
        
                                    if n_client > n_clients_for_warming:
                                        n_evaluated += 1
                                        n_evaluated_current_run += 1
        
                                        # output measures bepalen
        
                                        client_output_temp = {target_client: {
                                           'journey': client_dict[target_client]['journey'],
                                           'j_times': client_dict[target_client]['j_times'],
                                           }
                                        }
        
                                        output_dict.update(client_output_temp)
        
                                        if print_modus:
                                            print(client_output_temp)
                                    
        
        
                                    # iemand anders doorschuiven
        
                                    target_client_found = False
        
        
                                    if check_first_pref_client(w1_dict, extract_number(prev)):
                                        target_client = check_first_pref_client(w1_dict, extract_number(prev))
                                        target_client_found = True
                                        remove_from_wait_list(w1_dict,target_client,current_time,Fairness_list)
            #                             del wait_list_1[0]
        
        
        
                                    if print_modus:
                                            print('nieuwe klant gevonden voor bed is',target_client_found)
                                            if target_client_found:
                                               print('dit is', target_client)
        
                                    time_until_placement = exp(adm_days)                 
        
                                    if target_client_found: #and 
                                        if count_patients('ELV_Low')+count_place_reserved('ELV_Low')<n_beds_ELV_Low_list[extract_number(target_client)]:
                                            p_acc_opn = np.random.uniform(0,1)
            
                                            # als geen weekend of geen avond of p_acc_opn door toeval
                                            if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time)or p_acc_opn <= p_opn_weekend:
            
                                                time_until_placement = exp(adm_days) 
            
                                            else:#47
            
                                                if math.floor(current_time) % 7 in [6,0]: 
                                                    # als weekend
            
                                                    if math.floor(current_time) % 7 == 0:
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                    else:
                                                        time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
            
                                                    if print_modus:
                                                            print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
            
                                                elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                    # als avond
                                                    time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
            
                                                    if print_modus:
                                                        print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
            
                                            move_to_ELV_Low(target_client, time_until_placement)
        
                                elif any(item in Previous_Client for item in ['GPR_High', 'EMD', 'HOS_High','HOS_GRZ']):
                                    client_dict[target_client]['journey'].append(target_loc)
                                    client_dict[target_client]['j_times'].append(current_time)
        
                                    if n_client > n_clients_for_warming:
                                        n_evaluated += 1
                                        n_evaluated_current_run += 1
        
                                        # output measures bepalen
        
                                        client_output_temp = {target_client: {
                                           'journey': client_dict[target_client]['journey'],
                                           'j_times': client_dict[target_client]['j_times'],
                                           }
                                        }
        
                                        output_dict.update(client_output_temp)
        
                                        if print_modus:
                                            print(client_output_temp)
        
        
          
        
        
                                    # iemand anders doorschuiven
        
                                    target_client_found = False
        
                                    if Scen_shared_beds_Full:
                                        if priority:
                                            if (check_first_pref_client(w3_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))): 
                                                client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                client_4 = check_first_pref_client(w4_dict,extract_number(prev)) 
                                                min_of_wait = min(client_dict[(client_4)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1])
                                                if min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                    target_client = client_3
                                                    target_client_found = True
                                                    remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
            
                                                    if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                        del event_dict['HOSP_adm_' + target_client]
                                                else:
                                                    target_client = client_4
                                                    target_client_found = True
                                                    remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
        
                                            elif check_first_pref_client(w3_dict,extract_number(prev)) and not check_first_pref_client(w4_dict,extract_number(prev)): 
                                                target_client = check_first_pref_client(w3_dict,extract_number(prev))
                                                target_client_found = True
                                                remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                                            elif check_first_pref_client(w4_dict,extract_number(prev)) and not check_first_pref_client(w3_dict,extract_number(prev)):
                                                target_client = check_first_pref_client(w4_dict,extract_number(prev))
                                                target_client_found = True
                                                remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
                                            elif check_first_pref_client(w2_dict,extract_number(prev)):
                                                target_client = check_first_pref_client(w2_dict,extract_number(prev))
                                                target_client_found = True
                                                remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
                                            
                                        else:
                                            if (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))): 
                                                client_2 = check_first_pref_client(w2_dict,extract_number(prev)) 
                                                client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                client_4 = check_first_pref_client(w4_dict,extract_number(prev))
                                                min_of_wait = min(client_dict[(client_2)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1],client_dict[(client_4)]['j_times'][-1])
                                                if min_of_wait == client_dict[(client_2)]['j_times'][-1]:
                                                    target_client = client_2
                                                    target_client_found = True
                                                    remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
            
                                                    
                                                elif min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                    target_client = client_3
                                                    target_client_found = True
                                                    remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)
                                                    if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                        del event_dict['HOSP_adm_' + target_client]
                                                else:
                                                    target_client = client_4
                                                    target_client_found = True
                                                    remove_from_wait_list(w4_dict,client_4,current_time,Fairness_list)
                                            elif check_first_pref_client(w3_dict,extract_number(prev)) and not (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))):
                                                target_client = check_first_pref_client(w3_dict,extract_number(prev))
                                                target_client_found = True
                                                remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                                                if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                        del event_dict['HOSP_adm_' + target_client]
                                                
                                            elif check_first_pref_client(w2_dict,extract_number(prev)) and not (check_first_pref_client(w3_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))):
                                                target_client = check_first_pref_client(w2_dict,extract_number(prev))
                                                target_client_found = True
                                                remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
           
                                                                                                                                                                                                                                                      
                                            elif check_first_pref_client(w4_dict,extract_number(prev)) and not (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev))):
                                                target_client = check_first_pref_client(w4_dict,extract_number(prev))
                                                target_client_found = True
                                                remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
           
                                            elif (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev))) and not check_first_pref_client(w4_dict,extract_number(prev)) :
                                                client_2 = check_first_pref_client(w2_dict,extract_number(prev)) 
                                                client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                min_of_wait = min(client_dict[(client_2)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1])#1
                                                if min_of_wait == client_dict[(client_2)]['j_times'][-1]:
                                                    target_client = client_2
                                                    target_client_found = True
                                                    remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
           
                                                    if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                        del event_dict['HOSP_adm_' + target_client]
                                                elif min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                    target_client = client_3
                                                    target_client_found = True
                                                    remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)
                                            elif (check_first_pref_client(w4_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev))) and not check_first_pref_client(w2_dict,extract_number(prev)):
                                                client_4 = check_first_pref_client(w4_dict,extract_number(prev)) 
                                                client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                min_of_wait = min(client_dict[(client_4)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1])#2
                                                
                                                if min_of_wait == client_dict[(client_4)]['j_times'][-1]:#2
                                                    target_client = client_4
                                                    target_client_found = True
                                                    remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
            
                                                   
                                                elif min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                    target_client = client_3
                                                    target_client_found = True
                                                    remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)     
                                            elif (check_first_pref_client(w4_dict,extract_number(prev)) and check_first_pref_client(w2_dict,extract_number(prev))) and not check_first_pref_client(w3_dict,extract_number(prev)):
                                                client_2 = check_first_pref_client(w2_dict,extract_number(prev)) 
                                                client_4 = check_first_pref_client(w4_dict,extract_number(prev)) 
                                                min_of_wait = min(client_dict[(client_2)]['j_times'][-1], client_dict[(client_4)]['j_times'][-1])
                                                if min_of_wait == client_dict[(client_2)]['j_times'][-1]:
                                                    target_client = client_2
                                                    target_client_found = True
                                                    remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
           
                                                    if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                        del event_dict['HOSP_adm_' + target_client]
                                                elif min_of_wait == client_dict[(client_4)]['j_times'][-1]:
                                                    target_client = client_4
                                                    target_client_found = True
                                                    remove_from_wait_list(w4_dict,client_4,current_time,Fairness_list)
                                               
        
        
        
        
                                    # elif Scen_Total_Sharing:
                                    #     if check_first_pref_client(w_tot_dict,extract_number(prev)):
                                    #         target_client = check_first_pref_client(w_tot_dict,extract_number(prev))
                                    #         target_client_found = True
                                    #         remove_from_wait_list(w_tot_dict,target_client,current_time,Fairness_list)
                                    #         if (client_dict[target_client]['journey'][0] == 'EMD' and 'HOSP_adm' in client_dict[target_client]['journey']and 'HOSP_adm_' +target_client in event_dict) or 'ELV_EMDR' in client_dict[target_client]['journey']:
                                    #             del event_dict['HOSP_adm_' + target_client]
                                    #     else:
                                    #         if print_modus:
                                    #             print('no one moves')
        
                                    elif Scen_NO_Sharing or Scen_part_bed_Share:#6
                                        if 'ELV_part_' +str(extract_number(prev)) not in Previous_Client:
                                            if any(item in Previous_Client for item in ['GPR_High', 'EMD','HOS_High']): 
                                                if check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev)) :
                                                    client_2 = check_first_pref_client(w2_dict,extract_number(prev)) 
                                                    client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                    min_of_wait = min(client_dict[(client_2)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1])#@
                                                    if min_of_wait == client_dict[(client_2)]['j_times'][-1]:
                                                        target_client = client_2
                                                        target_client_found = True
                                                        remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
                                                        if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                            del event_dict['HOSP_adm_' + target_client]
                                                    else:
                                                        target_client = client_3
                                                        target_client_found = True
                                                        remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)
                                                elif check_first_pref_client(w3_dict,extract_number(prev)):
                                                    target_client = check_first_pref_client(w3_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                                                    
                                                elif  check_first_pref_client(w2_dict,extract_number(prev)):
                                                    target_client_found = True
                                                    target_client = check_first_pref_client(w2_dict,extract_number(prev))
                                                    remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
                
            
                                                    if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#1
                                                        del event_dict['HOSP_adm_' + target_client]
                                            elif any(item in Previous_Client for item in ['HOS_GRZ']):
                                                if check_first_pref_client(w4_dict,extract_number(prev)):
                                                    target_client = check_first_pref_client(w4_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
                                            
        
                                        elif 'ELV_part_' +str(extract_number(prev)) in Previous_Client:
                                            
                                            if priority:
                                                if (check_first_pref_client(w3_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))): 
                                                    client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                    client_4 = check_first_pref_client(w4_dict,extract_number(prev)) 
                                                    min_of_wait = min(client_dict[(client_4)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1])
                                                    if min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                        target_client = client_3
                                                        target_client_found = True
                                                        remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                
                                                        if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                            del event_dict['HOSP_adm_' + target_client]
                                                    else:
                                                        target_client = client_4
                                                        target_client_found = True
                                                        remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
            
                                                elif check_first_pref_client(w3_dict,extract_number(prev)) and not check_first_pref_client(w4_dict,extract_number(prev)): 
                                                    target_client = check_first_pref_client(w3_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                                                elif check_first_pref_client(w4_dict,extract_number(prev)) and not check_first_pref_client(w3_dict,extract_number(prev)):
                                                    target_client = check_first_pref_client(w4_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
                                                elif check_first_pref_client(w2_dict,extract_number(prev)):
                                                    target_client = check_first_pref_client(w2_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
                                            
                                            else:
                                                if (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))): 
                                                    client_2 = check_first_pref_client(w2_dict,extract_number(prev)) 
                                                    client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                    client_4 = check_first_pref_client(w4_dict,extract_number(prev))
                                                    min_of_wait = min(client_dict[(client_2)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1],client_dict[(client_4)]['j_times'][-1])
                                                    if min_of_wait == client_dict[(client_2)]['j_times'][-1]:
                                                        target_client = client_2
                                                        target_client_found = True
                                                        remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
                
                                                        
                                                    elif min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                        target_client = client_3
                                                        target_client_found = True
                                                        remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)
                                                        if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                            del event_dict['HOSP_adm_' + target_client]
                                                    else:
                                                        target_client = client_4
                                                        target_client_found = True
                                                        remove_from_wait_list(w4_dict,client_4,current_time,Fairness_list)
                                                elif check_first_pref_client(w3_dict,extract_number(prev)) and not (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))):
                                                    target_client = check_first_pref_client(w3_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w3_dict,target_client,current_time,Fairness_list)
                                                    if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                            del event_dict['HOSP_adm_' + target_client]
                                                    
                                                elif check_first_pref_client(w2_dict,extract_number(prev)) and not (check_first_pref_client(w3_dict,extract_number(prev)) and check_first_pref_client(w4_dict,extract_number(prev))):
                                                    target_client = check_first_pref_client(w2_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
               
                                                                                                                                                                                                                                                          
                                                elif check_first_pref_client(w4_dict,extract_number(prev)) and not (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev))):
                                                    target_client = check_first_pref_client(w4_dict,extract_number(prev))
                                                    target_client_found = True
                                                    remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
               
                                                elif (check_first_pref_client(w2_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev))) and not check_first_pref_client(w4_dict,extract_number(prev)) :
                                                    client_2 = check_first_pref_client(w2_dict,extract_number(prev)) 
                                                    client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                    min_of_wait = min(client_dict[(client_2)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1])#1
                                                    if min_of_wait == client_dict[(client_2)]['j_times'][-1]:
                                                        target_client = client_2
                                                        target_client_found = True
                                                        remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
               
                                                        if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                            del event_dict['HOSP_adm_' + target_client]
                                                    elif min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                        target_client = client_3
                                                        target_client_found = True
                                                        remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)
                                                elif (check_first_pref_client(w4_dict,extract_number(prev)) and check_first_pref_client(w3_dict,extract_number(prev))) and not check_first_pref_client(w2_dict,extract_number(prev)):
                                                    client_4 = check_first_pref_client(w4_dict,extract_number(prev)) 
                                                    client_3 = check_first_pref_client(w3_dict,extract_number(prev)) 
                                                    min_of_wait = min(client_dict[(client_4)]['j_times'][-1], client_dict[(client_3)]['j_times'][-1])#2
                                                    
                                                    if min_of_wait == client_dict[(client_4)]['j_times'][-1]:#2
                                                        target_client = client_4
                                                        target_client_found = True
                                                        remove_from_wait_list(w4_dict,target_client,current_time,Fairness_list)
                
                                                       
                                                    elif min_of_wait == client_dict[(client_3)]['j_times'][-1]:
                                                        target_client = client_3
                                                        target_client_found = True
                                                        remove_from_wait_list(w3_dict,client_3,current_time,Fairness_list)     
                                                elif (check_first_pref_client(w4_dict,extract_number(prev)) and check_first_pref_client(w2_dict,extract_number(prev))) and not check_first_pref_client(w3_dict,extract_number(prev)):
                                                    client_2 = check_first_pref_client(w2_dict,extract_number(prev)) 
                                                    client_4 = check_first_pref_client(w4_dict,extract_number(prev)) 
                                                    min_of_wait = min(client_dict[(client_2)]['j_times'][-1], client_dict[(client_4)]['j_times'][-1])
                                                    if min_of_wait == client_dict[(client_2)]['j_times'][-1]:
                                                        target_client = client_2
                                                        target_client_found = True
                                                        remove_from_wait_list(w2_dict,target_client,current_time,Fairness_list)
               
                                                        if (client_dict[target_client]['journey'][0] in ['EMD'] ) and 'HOSP_adm_' +target_client in event_dict:#2
                                                            del event_dict['HOSP_adm_' + target_client]
                                                    elif min_of_wait == client_dict[(client_4)]['j_times'][-1]:
                                                        target_client = client_4
                                                        target_client_found = True
                                                        remove_from_wait_list(w4_dict,client_4,current_time,Fairness_list)
                                                   
            
        
        
        
                                    if target_client_found:
                                        if Scen_NO_Sharing or (Scen_part_bed_Share and sum(n_beds_shared_High_list)==0) or Scen_tr_ward:
            
                                            if  any(item in Previous_Client for item in ['GPR_High', 'EMD', 'HOS_High']):
                                                if Check_space_partial_beds('EMD')<n_beds_High_Complex_list[extract_number(prev)]:
                                                    p_acc_opn = np.random.uniform(0,1)
                
                                                    # als geen weekend of geen avond of p_acc_opn door toeval
                                                    if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time)or p_acc_opn <= p_opn_weekend:
                
                                                        time_until_placement = exp(adm_days) 
                
                                                    else:#6
                
                                                        if math.floor(current_time) % 7 in [6,0]: 
                                                            # als weekend
                
                                                            if math.floor(current_time) % 7 == 0:
                                                                time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                            else:
                                                                time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
                
                                                            if print_modus:
                                                                    print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
                
                                                        elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                            # als avond
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
                
                                                            if print_modus:
                                                                print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
                
                
                                                    move_to_ELV_High(target_client, time_until_placement)
                                                    # print('break 5')
                                                    # print(Previous_Client)
                                                    # print(target_client)
                                                    # break
                                            elif  any(item in Previous_Client for item in ['HOS_GRZ']):
                                                 
                                                #if Check_space_partial_beds('HOS_GRZ')<n_beds_GRZ_list[extract_number(prev)]:
                                                p_acc_opn = np.random.uniform(0,1)
            
                                                # als geen weekend of geen avond of p_acc_opn door toeval
                                                if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time)or p_acc_opn <= p_opn_weekend:
            
                                                    time_until_placement = exp(adm_days) 
            
                                                else:#6
            
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
            
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
            
                                                        if print_modus:
                                                                print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
            
                                                        if print_modus:
                                                            print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
            
            
                                                move_to_ELV_High(target_client, time_until_placement)
            
                                        
                                        elif Scen_shared_beds_Full :
                                    
                                            if count_patients('ELV_High') + count_place_reserved('ELV_High') < n_beds_ELV_High_list[extract_number(prev)]:
                                                p_acc_opn = np.random.uniform(0,1)
                
                                                # als geen weekend of geen avond of p_acc_opn door toeval
                                                if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time)or p_acc_opn <= p_opn_weekend:
                
                                                    time_until_placement = exp(adm_days) 
                
                                                else:#5
                
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
                
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
                
                                                        if print_modus:
                                                                print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
                
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
                
                                                        if print_modus:
                                                            print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
                
                
                                                move_to_ELV_High(target_client, time_until_placement)      
                                        elif Scen_part_bed_Share and sum(n_beds_shared_High_list)>0:
                                            if any(item in Previous_Client for item in ['GPR_High', 'EMD', 'HOS_High']) and 'ELV_part_' +str(extract_number(prev)) not in client_dict[prev]['journey']:
                                                #if Check_space_partial_beds('EMD')<n_beds_High_Complex_list[extract_number(prev)]:
                                                p_acc_opn = np.random.uniform(0,1)
            
                                                # als geen weekend of geen avond of p_acc_opn door toeval
                                                if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time)or p_acc_opn <= p_opn_weekend:
            
                                                    time_until_placement = exp(adm_days) 
            
                                                else:#6
            
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
            
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
            
                                                        if print_modus:
                                                                print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
            
                                                        if print_modus:
                                                            print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
            
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                                    # print('break 5')
                                                    # print(Previous_Client)
                                                # print(target_client)
                                                # break
                                            elif any(item in Previous_Client for item in ['HOS_GRZ']) and 'ELV_part_' +str(extract_number(prev)) not in client_dict[prev]['journey']:#1
                                                #if Check_space_partial_beds('HOS_GRZ')<n_beds_GRZ_list[extract_number(prev)]:
                                                p_acc_opn = np.random.uniform(0,1)
            
                                                # als geen weekend of geen avond of p_acc_opn door toeval
                                                if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time)or p_acc_opn <= p_opn_weekend:
            
                                                    time_until_placement = exp(adm_days) 
            
                                                else:#6
            
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
            
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
            
                                                        if print_modus:
                                                                print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
            
                                                        if print_modus:
                                                            print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
            
            
                                                move_to_ELV_High(target_client, time_until_placement)
                                            elif 'ELV_part_' +str(extract_number(prev)) in client_dict[target_client]['journey'] :#4
                                                #if count_patients('ELV_part') + count_place_reserved('ELV_part') < n_beds_shared_High_list[extract_number(prev)]:
                                                p_acc_opn = np.random.uniform(0,1)
            
                                                # als geen weekend of geen avond of p_acc_opn door toeval
                                                if (math.floor(current_time) % 7 in [1,2,3,4,5] or current_time - math.floor(current_time) <= time_max_opn_ELV and current_time-math.floor(current_time)>=ELV_start_time)or p_acc_opn <= p_opn_weekend:
            
                                                    time_until_placement = exp(adm_days) 
            
                                                else:#5
            
                                                    if math.floor(current_time) % 7 in [6,0]: 
                                                        # als weekend
            
                                                        if math.floor(current_time) % 7 == 0:
                                                            time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days) 
                                                        else:
                                                            time_until_placement = 2 - (current_time - math.floor(current_time))  + exp(adm_days) 
            
                                                        if print_modus:
                                                                print('het is weekend op', current_time, 'dus plaatsing naar ELV over', time_until_placement)
            
                                                    elif current_time - math.floor(current_time) > time_max_opn_ELV or current_time-math.floor(current_time)<ELV_start_time:
                                                        # als avond
                                                        time_until_placement = 1 - (current_time - math.floor(current_time))  + exp(adm_days)         
            
                                                        if print_modus:
                                                            print('het is avond op', current_time, 'dus plaatsing naar ELV over', time_until_placement)  
            
            
                                                move_to_ELV_partial_bed(target_client, time_until_placement)      
                
            
                                        else:
                                            if print_modus:
                                                print('Niemand schuift door naar ELV High')
                        del event_dict[next_event]
                        if prev in output_dict.keys() and prev in client_dict.keys() or n_client<n_clients_for_warming:
                            del client_dict[prev]
                        event_dict = delete_events_with_target_client(event_dict,prev)
                        #update_client_dict(client_dict)
                            
        #         # einde subrun <<<<<<< EVALUATION >>>>>>>>>>>>>
                output_dict = order_journeys(output_dict, n_loc)
                
                    
                Wait_time_ELV_loc= []
                Wait_time_ELV_loc_part= []
                wt_to_ELV_High= []
                ELV_Help= []
                wait_time_ELV_High= []
                wt_to_ELV_Low_p= []
                wait_time_ELV_Low_q= []
                wait_time_ELV_Low_Help_List= []
                wait_time_ELV_Low= []
                wt_to_ELV_High= []
                
                wait_time_from_HOSP= []
                wt_to_ELV_High_q= []
                wt_to_ELV_High_p= []
                wait_time_elv_High= []
                wait_time_from_GPR_High= []
                wt_to_ELV_Low_p= []
                wait_time_ELV_Low_q= []
                wait_time_Help= []
                wait_time_from_GPR_Low= []
                los_mean_p= []
                los_mean_q= []
                los_mean_help= []
                los_list= []
                los_Low_mean_p= []
                los_Low_mean_q= []
                los_Low_help= []
                los_Low_list= []
                tot_cost_ELV_List= []
                tot_cost_ELV_help = []
                los_mean =0
                bez_gr_TRW_mean=0
                wait_time_from_EMD = []
                wt_to_ELV_TOT=[]
                wait_time_ELV_TOT = []
                Wait_time_ELV_loc_1 = []
                wt_to_HOSP=[]
                number_with_HOSP_Adm = []
                number_with_HOSP_Adm_HOSP = []
                with_HOSP_adm_1 = []
                tot_n_eval_via_HOS = []
                perc_with_HOSP_adm_HOSP_list = []
                
                
                
                #print(w1_dict,w2_dict,w3_dict,w_tot_dict,w2_dict_TRW,w3_dict_TRW)
        
                
                # wt voor alleen mensen die direct naar ELV zijn gegaan
                wait_time_ELV_TOT = list({k:v['j_times'][v['journey'].index('ELV_TOT')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_TOT' in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_EMDR')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_EMDR' in v['journey']}.values())
                
                
                
                # wt voor alleen mensen die direct naar ELV zijn gegaan
                wt_to_ELV_High = list({k:v['j_times'][v['journey'].index('ELV_High')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_High' in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_EMDR')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_EMDR' in v['journey']}.values())\
                + list({k:v['j_times'][v['journey'].index('ELV_part')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_part' in v['journey']}.values()) 
                
            
            
                wait_time_ELV_Low_Help_List = list({k:v['j_times'][v['journey'].index('ELV_Low')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_Low' in v['journey']}.values())
                
                
                
                if Scen_part_bed_Share:
                    wait_time_from_HOSP_GRZ = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_GRZ') and 'ELV_High'  in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_part')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_GRZ') and 'ELV_part' in v['journey']}.values())
                    wait_time_from_HOSP_High = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_High') and 'ELV_High' in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_part')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_High') and 'ELV_part'  in v['journey']}.values())
                    
                elif Scen_Total_Sharing:
                    wait_time_from_HOSP_GRZ = list({k:v['j_times'][v['journey'].index('ELV_TOT')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_GRZ') and 'ELV_TOT'  in v['journey']}.values())
                    wait_time_from_HOSP_High = list({k:v['j_times'][v['journey'].index('ELV_TOT')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_High') and 'ELV_TOT'  in v['journey']}.values())
                else:
                    wait_time_from_HOSP_GRZ = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_GRZ') and 'ELV_High'   in v['journey']}.values())
                    wait_time_from_HOSP_High = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        ( v['journey'][0] =='HOS_High') and 'ELV_High'  in v['journey']}.values())
            
                             
                if Scen_part_bed_Share:
                    wait_time_from_EMD = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        v['journey'][0] == 'EMD'and 'ELV_High'  in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_part')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        v['journey'][0] == 'EMD'and 'ELV_part'  in v['journey']}.values()) +list({k:v['j_times'][v['journey'].index('ELV_EMDR')] - v['j_times'][0]for (k,v) in output_dict.items() if 'ELV_EMDR' in v['journey']}.values())
                elif Scen_Total_Sharing:
                    wait_time_from_EMD = list({k:v['j_times'][v['journey'].index('ELV_TOT')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        v['journey'][0] == 'EMD' and 'ELV_TOT' in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_EMDR')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_EMDR' in v['journey']}.values())
                else:
                    wait_time_from_EMD = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                        v['journey'][0] == 'EMD' and 'ELV_High' in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_EMDR')] - v['j_times'][0] for (k,v) in output_dict.items() if 'ELV_EMDR' in v['journey']}.values())
               
        
                
                if Scen_part_bed_Share:
                    wait_time_from_GPR_High = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                    (v['journey'][0] == 'GPR_High') and 'ELV_part' not in v['journey']}.values())+list({k:v['j_times'][v['journey'].index('ELV_part')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                    (v['journey'][0] == 'GPR_High')and 'ELV_High' not in v['journey']}.values())
                elif Scen_Total_Sharing:
                    wait_time_from_GPR_High = list({k:v['j_times'][v['journey'].index('ELV_TOT')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                    v['journey'][0] == 'GPR_High' and 'ELV_TOT' in v['journey']}.values())
                else:
                    wait_time_from_GPR_High = list({k:v['j_times'][v['journey'].index('ELV_High')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                    v['journey'][0] == 'GPR_High' and 'ELV_High' in v['journey']}.values())
        
                    
                if Scen_Total_Sharing:
                    wait_time_from_GPR_Low= list({k:v['j_times'][v['journey'].index('ELV_TOT')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                            v['journey'][0] == 'GPR_Low' and 'ELV_TOT' in v['journey']}.values())
                else:
        
                    wait_time_from_GPR_Low= list({k:v['j_times'][v['journey'].index('ELV_Low')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                            v['journey'][0] == 'GPR_Low' and 'ELV_Low' in v['journey']}.values())
                
        
                
             
                wait_time_to_TRW = list({k:v['j_times'][v['journey'].index('TRW')]-v['j_times'][0] for (k,v) in output_dict.items() if \
                                             'TRW' in v['journey']}.values())
               
                
                
                if len(list({k:v for (k,v) in output_dict.items() if v['journey'][0] in ['HOS_GRZ','HOS_High','GPR_High','EMD','GPR_Low']}.keys())):
                    serv_level = len(list({k: v for (k, v) in output_dict.items() if v['j_times'][-2] - v['j_times'][0] <= 3}.values()))/len(output_dict)
                   
        
                tot_n_eval_via_EMD = len({k:v for (k,v) in output_dict.items() if \
                                  'EMD' in v['journey'] }.values())
                with_HOSP_adm = len({k:v for (k,v) in output_dict.items() if \
                                  'HOSP_adm' in v['journey']}.values())
                if tot_n_eval_via_EMD > 0:
                    
                    perc_with_HOSP_adm_list.append(with_HOSP_adm/tot_n_eval_via_EMD)
                    number_with_HOSP_Adm.append(with_HOSP_adm)
                else:
                    perc_with_HOSP_adm_list.append(0)
                    number_with_HOSP_Adm.append(0)
        
                tot_n_eval_via_HOS = len({k:v for (k,v) in output_dict.items() if \
                                  'HOS_High' or 'HOS_GRZ' in v['journey'] }.values())
                with_HOSP_adm_1 = len({k:v for (k,v) in output_dict.items() if \
                                  'Extra_Hosp_adm' in v['journey']}.values())
                if tot_n_eval_via_HOS > 0:
                    
                    perc_with_HOSP_adm_HOSP_list.append(with_HOSP_adm_1/tot_n_eval_via_HOS)
                    number_with_HOSP_Adm_HOSP.append(with_HOSP_adm_1)
                else:
                    perc_with_HOSP_adm_list.append(0)
                    number_with_HOSP_Adm_HOSP.append(0)
        
                # nr patient replacements
                nr_pat_repl = np.mean(list({k:len((v['journey']))-1 for (k,v) in output_dict.items()\
                                   }.values()))
                nr_pat_repl_list.append(nr_pat_repl)
                    
                
                los_list = list({k:v['j_times'][-1] - v['j_times'][0] for k,v in output_dict.items() if v['journey'][0] in ['HOS_GRZ','HOS_High','GPR_High','EMD']}.values())
           
                los_Low_list = list({k:v['j_times'][-1] - v['j_times'][0] for k,v in output_dict.items() if v['journey'][0] in ['GPR_Low']}.values())
        
                if Preference == 'FCFS':
                    nr_pat_trans_mean = len(list({k:v['j_times'] for (k,v) in output_dict.items() if 'Transfer' in v['journey']}.values()))
                else:
                    nr_pat_trans_mean = len(list({k:v['j_times'] for (k,v) in output_dict.items() if 'Transfer' in v['journey']}.values()))
                #costs
                
                        
                output_dict_save = output_dict.copy()
                output_dict = {}
                                
            print('')
            print('----- Run',loop_nr,'completed! ------')
            print('')
            
            if n_evaluated > 0:
                #plt.hist(abs_aanw_list)
                if Project == 'Check MMC High':
                    wt_ELV_High_final = make_conf_output(wt_to_ELV_High)
        
                    serv_level_final = make_conf_output(serv_level)
                    serv_level_mean = mean(serv_level)
                else:
    
                    wt_HOSP_High_mean = mean(wait_time_from_HOSP_High)
                    wt_HOSP_GRZ_mean = mean(wait_time_from_HOSP_GRZ)
                    wt_GPR_High_mean = mean(wait_time_from_GPR_High)
                    wt_GPR_Low_mean = mean(wait_time_from_GPR_Low)
                    wait_time_to_TRW_mean = mean(wait_time_to_TRW)
                    wait_time_from_EMD_mean = mean(wait_time_from_EMD)
        
                   
                    perc_with_HOSP_adm_mean = mean(perc_with_HOSP_adm_list)
                    Number_with_HOSP_adm_mean = mean(number_with_HOSP_Adm)
                    perc_with_HOSP_adm_mean_HOSP = mean(perc_with_HOSP_adm_HOSP_list)
                    Number_with_HOSP_adm_mean_HOSP = mean(number_with_HOSP_Adm_HOSP)
    
                    
                    nr_pat_repl_mean = mean(nr_pat_repl_list)
                    los_High_mean = mean(los_list)
                    los_Low_mean = mean(los_Low_list)
        
                    if Scen_Total_Sharing != True:
                        wt_ELV_High_mean = mean(wt_to_ELV_High)
                        wt_ELV_Low_mean = mean(wait_time_ELV_Low_Help_List)
                        bez_gr_Low_mean = mean(bez_gr_Low_list)
                        bez_gr_High_mean = mean(bez_gr_list_High)
                        wt_ELV_TOT_mean = (wt_ELV_High_mean+ wt_ELV_Low_mean)/2
                    else: 
        
                        wt_ELV_High_mean = (wt_HOSP_High_mean+wt_HOSP_GRZ_mean +wt_GPR_High_mean+wait_time_from_EMD_mean)/4
                        wt_ELV_Low_mean = wt_GPR_Low_mean
                        bez_gr_Low_mean = 0
                        bez_gr_High_mean = 0
                        wt_ELV_TOT_mean = mean(wait_time_ELV_TOT)
                    bez_gr_Tot_mean = mean(bez_gr_list_Total)
                    bez_gr_TRW_mean = mean(bez_gr_TRW_list)
                    if sum(beds_Emergency_list)>0:
                        bez_gr_EMDR_mean = mean(bez_gr_EMDR_list)
                    len_w3_mean = mean(len_w3_list)
                    len_w4_mean = mean(len_w4_list)
                    len_w1_mean = mean(len_w1_list)
                    len_w2_list_mean = mean(len_w2_list)
                    len_wtot_mean = mean(len_w_total_list)
        
                    serv_level_mean = serv_level
                
                
                
                output_mean_df_temp = pd.DataFrame.from_dict({'Run': [loop_nr],\
                        'Running_time (sec)': round(time.process_time() - start_time),
                        'Project':Project,
                        'Wait_time_ELV_High': wt_ELV_High_mean,
                        'Wait_time_ELV_Low': wt_ELV_Low_mean,
                        'Wait_time_ELV_TOT': wt_ELV_TOT_mean,
                        'Wt_from_HOSP_GRZ': wt_HOSP_GRZ_mean,
                        'Wt_from_HOSP_High': wt_HOSP_High_mean,                                   
                        'Wt_from_GPR_High': wt_GPR_High_mean,
                        'Wt_from_GPR_Low': wt_GPR_Low_mean,                                
                        'Wt_to_TRW': wait_time_to_TRW_mean,
                        'WT_from_EMD':wait_time_from_EMD_mean,
                        'Perc_with_HOSP_adm': perc_with_HOSP_adm_mean,
                        'Number with hosp adm EMD':Number_with_HOSP_adm_mean, 
                        'Perc_with_HOSP_adm_HOSP':perc_with_HOSP_adm_mean_HOSP, 
                        'Number with hosp adm HOSP':Number_with_HOSP_adm_mean_HOSP,              
                        'nr_pat_repl': nr_pat_repl_mean,
                        'los_ELV_High': los_High_mean,
                        'los_ELV_Low': los_Low_mean,
                        'bez_gr_total': bez_gr_Tot_mean,
                        'bez_gr_High':bez_gr_High_mean,
                        'bez_gr_Low':bez_gr_Low_mean,    
                        'bez_gr_TRW': bez_gr_TRW_mean,
                        'bez_gr_EMDR': bez_gr_EMDR_mean,
                        'len_w3': len_w3_mean,
                        'len_w2' : len_w2_list_mean,
                        'len_w1': len_w1_mean,
                        'len_w4': len_w4_mean,
                        'len_wtot': len_wtot_mean,
                        'serv_level': serv_level_mean,
                        'Priority': priority,
                        'Preference': Preference,
                        'Scen_Full_bed_Sharing' : Scen_shared_beds_Full,
                        'Scen_partial_bed_Sharing' : Scen_part_bed_Share,
                        'Scen_NO_bed_Sharing' : Scen_NO_Sharing ,
                        'Scen_Total_Sharing': Scen_Total_Sharing,                                     
                        'Number of transfers between locations': nr_pat_trans_mean,
                        'Number of Locations ELV': n_loc,    
                        'Number of beds ELV_High': str(n_beds_ELV_High_list),
                        'Number of beds ELV_Low': str(n_beds_ELV_Low_list),
                        'Number of beds GRZ':str(n_beds_GRZ_list),
                        'Number of beds High Complex':str(n_beds_High_Complex_list),
                        'Number of shared beds': str(n_beds_shared_High_list),
                        'Number of beds ELV Total':str(n_beds_ELV_total_list),                                     
                        'Number of TRW beds': str(beds_TRW_list),
                        'Fairness': max(Fairness_list),
                                        
                        })
                    
                
                if loop_nr == 0:
                    output_df = output_mean_df_temp
                    
                else:
                    output_df = pd.concat([output_df,output_mean_df_temp])    
                       
                    
                
        #         if loop_nr == 0:
        #             output_df = output_df_temp
        #         else:
        #             output_df = pd.concat([output_df,output_df_temp])
            
        return output_df
    
        
    
    # Button to display the dataframe
with col3:
    if st.button('Start Simulation'):
        # Convert the inputs dictionary to a DataFrame
        df1 = df_tot
        output_df = simulate(df1)
 
        table1_columns = [ 'Wt_from_HOSP_GRZ',
        'Wt_from_HOSP_High', 'Wt_from_GPR_High', 'Wt_from_GPR_Low', 'Wt_to_TRW', 'WT_from_EMD']
        table1_right_names = [ 'Ziekenhuis GRZ',
        'Ziekenhuis Hoog Complex', 'Huisarts Hoog Complex', 'Huisarts Laag Complex', 'Observatie', 'Spoedeisendehulp']
        
        table2_columns = ['Perc_with_HOSP_adm', 'Number with hosp adm EMD', 'Perc_with_HOSP_adm_HOSP',
        'Number with hosp adm HOSP', 'nr_pat_repl']
        table2_right_names = ['Percentage met ziekenhuisopname vanaf spoedeisendehulp', 'Aantal met ziekenhuisopname vanaf spoedeisendehulp', 'Percentage met ziekenhuisopname vanaf het ziekenhuis',
        'Aantal met ziekenhuisopname vanaf het ziekenhuis', 'Aantal verplaatsingen']
        
        table3_columns = ['serv_level', 'los_ELV_High', 'los_ELV_Low', 'bez_gr_total',
        'bez_gr_High', 'bez_gr_Low']
        table3_right_names = ['Service level', 'Gemiddelde verplijfduur Hoog Complex', 'Gemiddelde verblijfduur Laag Complex', 'Bezettingsgraad totaal',
        'Bezettingsgraad Hoog Complex', 'Bezettingsgraad Laag Complex']
        
        table4_columns = ['Number of Locations ELV', 'Number of beds ELV_High', 'Number of beds ELV_Low',
        'Number of beds GRZ', 'Number of beds High Complex', 'Number of shared beds', 'Number of TRW beds', 'Number of beds ELV Total']
        table4_right_names = ['Aantal ELV Locaties', 'Aantal ELV Hoog Complex bedden', 'Aantal ELV Laag Complex bedden',
        'Aantal bedden Geriatrische Zorg', 'Aantal Hoog Complexe bedden', 'Aantal gedeelde bedden', 'Aantal bedden voor observatie', 'Aantal bedden ELV Totaal']
        # Create tables
        table1 = pd.DataFrame(output_df[table1_columns])
        table2 = pd.DataFrame(output_df[table2_columns])
        table3 = pd.DataFrame(output_df[table3_columns])
        table4 = pd.DataFrame(output_df[table4_columns])
        table2['Perc_with_HOSP_adm'] = table2['Perc_with_HOSP_adm']*100
        table2['Perc_with_HOSP_adm_HOSP'] = table2['Perc_with_HOSP_adm_HOSP']*100
        table3['serv_level'] = table3['serv_level']*100
        table3['bez_gr_total'] = table3['bez_gr_total']*100
        table3['bez_gr_High'] = table3['bez_gr_High']*100
        table3['bez_gr_Low'] = table3['bez_gr_Low']*100
        # Hernoem de kolommen
        table1.rename(columns = {'Wt_from_HOSP_GRZ':'Ziekenhuis GRZ', 'Wt_from_HOSP_High':'Ziekenhuis Hoog Complex', 'Wt_from_GPR_High':'Huisarts Hoog Complex', 'Wt_from_GPR_Low':'Huisarts Laag Complex', 'Wt_to_TRW':'Observatie', 'WT_from_EMD':'Spoedeisendehulp'},inplace = True)
        table2.rename(columns = {'Perc_with_HOSP_adm':'Percentage met ziekenhuisopname vanaf spoedeisendehulp (%)', 'Number with hosp adm EMD':'Aantal met ziekenhuisopname vanaf spoedeisendehulp', 'Perc_with_HOSP_adm_HOSP':'Percentage met ziekenhuisopname vanaf het ziekenhuis (%)','Number with hosp adm HOSP':'Aantal met ziekenhuisopname vanaf het ziekenhuis', 'nr_pat_repl':'Aantal verplaatsingen'}, inplace = True)
        table3.rename(columns = {'serv_level':'Service level (Geholpen < 3 dagen) (%)', 'los_ELV_High':'Gemiddelde verplijfduur Hoog Complex', 'los_ELV_Low':'Gemiddelde verblijfduur Laag Complex', 'bez_gr_total':'Bezettingsgraad totaal (%)',
        'bez_gr_High':'Bezettingsgraad Hoog Complex (%)', 'bez_gr_Low':'Bezettingsgraad Laag Complex (%)'}, inplace =True)
        table4.rename(columns = {'Number of Locations ELV':'Aantal ELV Locaties', 'Number of beds ELV_High':'Aantal ELV Hoog Complex bedden', 'Number of beds ELV_Low':'Aantal ELV Laag Complex bedden',
        'Number of beds GRZ':'Aantal bedden Geriatrische Zorg', 'Number of beds High Complex':'Aantal Hoog Complexe bedden', 'Number of shared beds':'Aantal gedeelde bedden', 'Number of TRW beds':'Aantal bedden voor observatie', 'Number of beds ELV Total':'Aantal bedden ELV Totaal'},inplace =True)
        table1.index = ['Wachttijd (dagen)']
        table2.index = ['Percentages en aantallen']
        table3.index = ['Levels']
        table4.index = ['Aantal']
        #st.write(df1)
        #with col3:
        st.write(table1.T)
        st.bar_chart(table1.T, y = 'Wachttijd (dagen)')
        st.write(table2.T)
        st.write(table3.T)
        st.write(table4.T)
   

