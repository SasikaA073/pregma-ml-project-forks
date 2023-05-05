import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

# Define the page title
st.title("Patient's Dashboard")


# Define the column names
columns = ['Patient ID', 'NIC', "Mother's name", 'Mobile Number', 'Month', 'Predicted Risk level']

# Create a sample data frame
data = {
    'Patient ID': [1, 2, 3, 4, 5],
    'NIC': ['12345-1234567-1', '23456-2345678-2', '34567-3456789-3', '45678-4567890-4', '56789-5678901-5'],
    "Mother's name": ['Mary', 'John', 'Jane', 'Peter', 'Susan'],
    'Mobile Number': ['123456789', '234567890', '345678901', '456789012', '567890123'],
    'Month': ['1', '2', '4', '1', '3'],
    'Predicted Risk level': ['High', 'Low', 'Medium', 'High', 'Low']
}

df = pd.DataFrame(data)

# Display the table
st.table(df[columns])






