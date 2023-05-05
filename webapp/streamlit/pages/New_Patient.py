import streamlit as st
from classes import Patient
from database import *
import pickle

# Load ML model
ml_model_name = "./ml_models/month1_model.pkl"
model = pickle.load(open(ml_model_name, 'rb'))

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
    age = st.text_input(label='Age')
    blood_group = st.selectbox(label='Blood Group', options=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    mobile_number = st.text_input(label='Mobile Number')

    systolicBP = st.text_input(label='Systolic Blood Pressure')
    diastolicBP = st.text_input(label='Diastolic Blood Pressure')
    blood_sugar = st.text_input(label='Blood Sugar Level')
    body_temp = st.text_input(label='Body Temperature (in Celsius))')
    heart_rate = st.text_input(label='Heart Rate (in BPM)')
    month = st.selectbox(label='Month', options=['1'])
    # month = 1

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        
        st.success(f"Mother {patient_id} Registered Successfully".format(first_name))
        # st.balloons()
        st.write("First Name: ", first_name)
        st.write("Last Name: ", last_name)
        st.write("Age: ", age)
        st.write("Blood Group: ", blood_group)
        st.write("Mobile Number: ", mobile_number)

        # write to the database
        month_data = {systolicBP, diastolicBP, blood_sugar, body_temp, heart_rate}
        insert_patient(patient_id, first_name, last_name, nic, age, blood_group, mobile_number, month, month_data)

        st.success(f"{patient_id} Mother's Month {month} results updated Successfully".format(first_name))
        # st.balloons()
        st.write("Systolic Blood Pressure: ")
        st.write("Systolic Blood Pressure: ", systolicBP)   
        st.write("Diastolic Blood Pressure: ", diastolicBP)
        st.write("Blood Sugar Level: ", blood_sugar)
        st.write("Body Temperature (in Celsius): ", body_temp)
        st.write("Heart Rate (in BPM): ", heart_rate)
        st.write("Month: ", month)

        
    


    st.sidebar.success("Let's start monitering after the Registration")