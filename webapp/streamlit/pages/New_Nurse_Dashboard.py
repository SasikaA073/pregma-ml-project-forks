# IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px
from deta import Deta
import os
from dotenv import load_dotenv
from classes import Patient
import pickle
from database2 import * 


DETA_KEY = "d0E7NcjK5X8P_RVUiBBKMe36JY7P9pen6WsDBawji3GTM"

# Initialize Deta with a project key
deta = Deta(DETA_KEY)

# create databses from month 1 to 6

patients_db = deta.Base("patients_db")

# Streamlit interface
st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System",
    page_icon="❤️",
    layout="centered",
)

st.title("Nurse Dashboard")


# a list of patients data
all_patients_details = get_all_patients()

# display the type of all_patients_details
# st.write(type(all_patients_details))


# display all details of all patients in a table
st.markdown("## All Patients")
st.dataframe(all_patients_details)


# diplay buttons horizontally with labels of patient ids from all_patients_details dataframe
st.markdown("## Select a patient")
for patient_record in all_patients_details:
    # display a button for each patient horizontally
    st.button(patient_record["key"])
    
    





    