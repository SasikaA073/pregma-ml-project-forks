import streamlit as st
import pandas as pd
import plotly.express as px
from deta import Deta
import os
from dotenv import load_dotenv
from classes import Patient
import pickle
from database import * 

# Load your Deta project key from an environment variable
# load_dotenv(".env")
# DETA_KEY = os.getenv('DETA_PROJECT_KEY') 
DETA_KEY = "d0E7NcjK5X8P_RVUiBBKMe36JY7P9pen6WsDBawji3GTM"

# Initialize Deta with a project key
deta = Deta(DETA_KEY)

# create a DB and connect it
patients_db = deta.Base("patients_db")

# a list of patients data
all_patients_details = get_all_patients()

patient_ids = []
patient_first_names = []
patient_last_names = []
patient_nics = []
patient_ages = []
patient_blood_groups = []
patient_mobile_numbers = []

patient_systolicBPs_1 = []
patient_diastolicBPs_1 = []
patient_blood_sugars_1 = []
patient_body_temps_1 = []
patient_heart_rates_1 = []
patient_predictions_1 = []
patient_dates_1 = []

for i, dict in enumerate(all_patients_details):
    patient_ids.append(dict["key"])
    patient_first_names.append(dict["first_name"])
    patient_last_names.append(dict["last_name"])
    patient_nics.append(dict["nic"])
    patient_ages.append(dict["age"])
    patient_blood_groups.append(dict["blood_group"])
    patient_mobile_numbers.append(dict["mobile_number"])

    patient_systolicBPs_1.append(dict["systolicBP"])
    patient_diastolicBPs_1.append(dict["diastolicBP"])
    patient_blood_sugars_1.append(dict["blood_sugar"])
    patient_body_temps_1.append(dict["body_temp"])
    patient_heart_rates_1.append(dict["heart_rate"])
    patient_predictions_1.append(dict["prediction"])
    # patient_dates_1.append(dict["date"])



st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

# Define the page title
st.title("Patient's Dashboard")


# Define the column names
columns_1 = ['Patient ID', 'NIC',"First name", "Last name",
             "Age", "Blood Group", 'Mobile Number',"month1 systolic blood pressure",
             "month1 diastolic blood pressure", "month1 blood sugar", "month1 body temperature",
             "month1 heart rate", "month1 prediction"]

# Create a sample data frame
data = {
    'Patient ID': patient_ids,
    'NIC': patient_nics,
    "First name": patient_first_names,
    "Last name": patient_last_names,
    "Age": patient_ages,
    "Blood Group": patient_blood_groups,
    'Mobile Number': patient_mobile_numbers,

    "month1 systolic blood pressure": patient_systolicBPs_1,
    "month1 diastolic blood pressure": patient_diastolicBPs_1,
    "month1 blood sugar": patient_blood_sugars_1,
    "month1 body temperature": patient_body_temps_1,
    "month1 heart rate": patient_heart_rates_1,
    "month1 prediction": patient_predictions_1,
    # "month1 date": patient_dates_1,
    }

# if one record is selected, display the details of that record
# selected_indices = st.multiselect('Select rows:', patient_ids.index)

df = pd.DataFrame(data)

# Display the table
st.table(df[columns_1])

st.divider()

st.subheader(f"Mother 's Health Status")

# Define the columns for the table
columns = ['Patient\'s ID', 'NIC', 'First name', 'Last name', 'Mobile Number', 'Month', 'Current predicted Risk Level']

# Define a function to get the data for the table
def get_data():
    return [{'Patient\'s ID': 'p014', 'NIC': '1244545366', 'First name': 'Piyumi', 'Last name': 'Rathnayake', 'Mobile Number': '1245363636', 'Month': 1, 'Current predicted Risk Level': 'Medium'}]

# Display the table
st.table(pd.DataFrame(get_data(), columns=columns))

st.subheader("Current Health Report")
# Define the columns for the table
columns = ['Month', 'Predicted Status', 'Actual Status']

# Define the data for the table
data = [['1', 'Medium Risk', 'Medium Risk'],
    ['2', 'Medium Risk', 'Low Risk'],
    ['3', 'Low Risk', 'Low Risk'],
    ['4', 'High Risk', 'Medium Risk']
]

data_plot = [['1', '1', '1'],
    ['2', '1', '0'],
    ['3', '1', '1'],
    ['4', '2', '1']
]

st.table(pd.DataFrame(data, columns=columns))

# Display the table
df = pd.DataFrame(data_plot, columns=columns)

# Create a line chart for the "Predicted Status" column
fig_pred = px.line(df, x='Month', y=['Predicted Status', 'Actual Status'])

# Create a line chart for the "Actual Status" column
# fig_act = px.line(df, x='Month', y='Actual Status')

# Display the charts using streamlit.plotly_chart()
st.plotly_chart(fig_pred)