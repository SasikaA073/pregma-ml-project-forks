import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

# Define the page title
st.title("Patient's Dashboard")


# Define the column names
columns_1 = ['Patient ID', 'NIC', "Mother's name", 'Mobile Number', 'Month', 'Predicted Risk level']

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
st.table(df[columns_1])

st.divider()

st.subheader("Mother {}'s Health Status")

# Define the columns for the table
columns = ['Patient\'s ID', 'NIC', 'First name', 'Last name', 'Mobile Number', 'Month', 'Current predicted Risk Level']

# Define a function to get the data for the table
def get_data():
    return [{'Patient\'s ID': '1', 'NIC': '1234567890', 'First name': 'John', 'Last name': 'Doe', 'Mobile Number': '1234567890', 'Month': 5, 'Current predicted Risk Level': 'High'}]

# Display the table
st.table(pd.DataFrame(get_data(), columns=columns))

st.subheader("Current Health Report")
# Define the columns for the table
columns = ['Month', 'Predicted Status', 'Actual Status']

# Define the data for the table
data = [['1', 'Low Risk', 'Low Risk'],
    ['2', 'Low Risk', 'Low Risk'],
    ['3', 'Low Risk', 'Low Risk'],
    ['4', 'High Risk', 'High Risk'],
    ['5', 'Low Risk', 'Low Risk'],
    ['6', 'Mid Risk', 'Mid Risk'],
]

data_plot = [['1', '0', '0.5'],
    ['2', '0', '0'],
    ['3', '0', '0'],
    ['4', '1', '0.5'],
    ['5', '0', '0'],
    ['6', '0.5', '1'],
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