import streamlit as st
from classes import Patient
from database import *

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

st.title("Register a New Mother")

with st.form(key='reg_form'):
    patient_id = st.text_input(label='Patient ID').lower()
    first_name = st.text_input(label='First Name')
    last_name = st.text_input(label='Last Name')
    nic = st.text_input(label='NIC')
    date_of_birth = st.date_input(label='Date of Birth')
    blood_group = st.selectbox(label='Blood Group', options=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    mobile_number = st.text_input(label='Mobile Number')

    submit_button = st.form_submit_button(label='Register')

    if submit_button:
        st.success(f"Mother {patient_id} Registered Successfully".format(first_name))
        # st.balloons()
        st.write("First Name: ", first_name)
        st.write("Last Name: ", last_name)
        st.write("Date of Birth: ", date_of_birth)
        st.write("Blood Group: ", blood_group)
        st.write("Mobile Number: ", mobile_number)


        P = Patient(patient_id, first_name, last_name, nic, date_of_birth, blood_group, mobile_number)

        # add a patient to the database
        insert_patient(P.patient_id, P.first_name, P.last_name, P.nic, P.date_of_birth, P.blood_group, P.mobile_number)
st.title("User Profile")

with st.form(key='pred_form'):

    patient_id = st.text_input(label='Patient ID').lower()
    systolicBP = st.text_input(label='Systolic Blood Pressure')
    diastolicBP = st.text_input(label='Diastolic Blood Pressure')
    blood_sugar = st.text_input(label='Blood Sugar Level')
    body_temp = st.text_input(label='Body Temperature (in Celsius))')
    heart_rate = st.text_input(label='Heart Rate (in BPM)')
    month = st.selectbox(label='Month', options=['1', '2', '3', '4', '5', '6'])

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success(f"Mother's Month {month} results updated Successfully".format(first_name))
        # st.balloons()
        st.write("Systolic Blood Pressure: ")
        st.write("Systolic Blood Pressure: ", systolicBP)   
        st.write("Diastolic Blood Pressure: ", diastolicBP)
        st.write("Blood Sugar Level: ", blood_sugar)
        st.write("Body Temperature (in Celsius): ", body_temp)
        st.write("Heart Rate (in BPM): ", heart_rate)
        st.write("Month: ", month)
    


    st.sidebar.success("Let's start monitering after the Registration")